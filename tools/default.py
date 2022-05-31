#!/usr/bin/python3
"""
    module
"""

def fun(event, data, instance):
    act = event["type"]
    but = event["button"]
    if act == "scroll":
        instance.zoom_in(data["dy"])
    if act == "drag":
        pos = data["pos_arr"]
        dif = data["dif_uv"] - data["pos_uv"]
        if but == 8:
            instance.move_to(dif)
        if but == -1: 
            instance.rotate(dif[0])
        if but == 4:
            try:
                instance.arr[tuple(pos[::-1])] = [255, 255, 255]
            except:
                pass
    instance.update_arr()

out = {
    "name": "default",
    "f": fun
}

