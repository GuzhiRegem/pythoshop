#!/usr/bin/python3
"""
    module
"""
import numpy as np
from PIL import Image
from glumpy import app, gl, glm, gloo, data
from math import cos, sin, pi

def fun(event, data, instance):
    print(event)
    print(data)



class Display:
    def __init__(
        self,
        array,
        handler=fun,
        vertex_src="shade.vert",
        fragment_src="shade.frag",
        screen_size=(700, 700)
    ):
        with open(vertex_src, "r") as f:
            vertex = f.read()
        with open(fragment_src, "r") as f:
            fragment = f.read()
        self.quad = gloo.Program(vertex, fragment, count=4)
        self.screen_size = np.array(screen_size)
        self.handler = handler
        self.set_image(array)
        

        self.quad['position'] = [ (-1,-1),   (-1,+1),   (+1,-1),   (+1,+1)   ]
        self.quad['theta'] = 0
        self.quad['offset'] = np.array([0, 0])
        self.quad['scale'] = 1.0
        self.quad['texcoord'] = np.array([[0,0], [0, 1], [+1, 0], [1, 1]])
        self.window = app.Window()
        self.window.set_size(screen_size[0], screen_size[1])

    def update_arr(self):
        self.quad["tex"] = self.arr

    def set_image(self, array):
        self.quad["tex"] = array
        self.quad['ratio'] = np.array([
            array.shape[1],
            array.shape[0]
        ]) / max(array.shape)
        self.arr = array

    def pos_to_uv(self, x, y):
        out = np.array([x, y], dtype=np.float64)
        out = ((out / self.screen_size) * 2.0) - np.array([1, 1])
        out *= self.quad["scale"]
        out[1] *= -1
        return out

    def pos_to_arr(self, x, y):
        out = self.pos_to_uv(x, y)
        dif = out - self.quad["offset"]
        a = self.quad["theta"]
        rot = np.array([[cos(a), -sin(a)], [sin(a), cos(a)]])
        dif = np.dot(dif, rot)
        dif *= (700/525)
        dif *= np.array([1, 1]) / self.quad["ratio"]
        dif = (dif + np.array([1, 1])) * 0.5
        dif *= np.array([self.arr.shape[1], self.arr.shape[0]])
        return dif.astype(np.int64)

    def zoom_in(self, n):
        self.quad['scale'] *= (2**(-n/50))

    def move_to(self, pos):
        self.quad["offset"] += pos

    def rotate(self, amount):
        amount *= 1 / self.quad["scale"]
        self.quad["theta"] += amount
        amount *= -1
        rot = np.array([[cos(amount), -sin(amount)], [sin(amount), cos(amount)]])
        self.quad["offset"] = np.dot(self.quad["offset"], rot)


def start(options):
    ins = Display(**options)
    window = ins.window
        
    @window.event
    def on_draw(dt):
        window.clear()
        ins.quad.draw(gl.GL_TRIANGLE_STRIP)
    
    @window.event
    def on_mouse_scroll(x, y, dx, dy):
        ins.handler({
            "type": "scroll",
            "button": 0
        }, {
            "x": x,
            "y": y,
            "dx": dx,
            "dy": dy
        }, ins)
    
    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons):
        pos1 = ins.pos_to_uv(x, y)
        pos2 = ins.pos_to_arr(x, y)
        pos3 = ins.pos_to_uv(x + dx, y + dy)
        pos4 = ins.pos_to_arr(x + dx, y + dy)
        ins.handler({
            "type": "drag",
            "button": buttons
        }, {
            "pos_uv": pos1,
            "pos_arr": pos2,
            "dif_uv": pos3,
            "dif_arr": pos4
        }, ins)

    @window.event
    def on_mouse_press(x, y, button):
        pos1 = ins.pos_to_uv(x, y)
        pos2 = ins.pos_to_arr(x, y)
        ins.handler({
            "type": "press",
            "button": button
        }, {
            "pos_uv": pos1,
            "pos_arr": pos2
        }, ins)
    
    @window.event
    def on_mouse_release(x, y, button):
        pos1 = ins.pos_to_uv(x, y)
        pos2 = ins.pos_to_arr(x, y)
        ins.handler({
            "type": "release",
            "button": button
        }, {
            "pos_uv": pos1,
            "pos_arr": pos2
        }, ins)
    
    app.run()
