#!/usr/bin/python3
"""
    module
"""
import numpy as np

def fun(event, data, instance):
    act = event["type"]
    but = event["button"]
    if act == "drag":
        pos = data["pos_arr"]
        if but == 4:
            try:
                col = data["dict"]["color"]
                if instance.arr.shape[2] == 4:
                    col = np.array([col[0], col[1], col[2], 255], dtype=np.uint8)
                instance.arr[tuple(pos[::-1])] = col
                for i in range(10):
                    pos[0] += 1
                    instance.arr[tuple(pos[::-1])] = col
            except:
                pass
    instance.update_arr()

out = {
    "name": "draw",
    "f": fun
}

