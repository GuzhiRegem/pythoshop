#!/usr/bin/python3
"""
    module
"""
import display
import numpy as np
from PIL import Image
from PyQt5.QtWidgets import QApplication, QLabel
from multiprocessing import Process, Manager, Value
from tools import t_lis
from file_tools import open_image, save_image
from window_tools import Window
import sys

g_data = Manager().dict()
g_data["idx"] = 1
g_data["color"] = np.array([0, 0, 0])
lis_of_keys = list(t_lis.keys())
print(g_data)

def change_idx(index):
    g_data["idx"] = index

def change_color(col):
    g_data["color"] = np.array(col)

def p_f(lis):
    app = QApplication([])
    w = Window(
        lis=lis,
        idx_changer=change_idx,
        color_changer=change_color
    )
    w.show()
    app.exec_()

def fun(event, data, instance):
    idx_ = int(g_data["idx"])
    data["dict"] = g_data
    t_lis[lis_of_keys[idx_]](event, data, instance)


arr = open_image("download.png")
print(arr)
p = Process(target=p_f, args=(lis_of_keys, ))
p.start()
display.start({
    "array": arr,
    "handler": fun
})
p.terminate()
save_image(arr, "out.png")
sys.exit()
p.join()

