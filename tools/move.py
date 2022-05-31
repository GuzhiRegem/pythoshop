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
        if but == 4:
            instance.move_to(dif)
        if but == 8: 
            instance.rotate(dif[0])

out = {
    "name": "move",
    "f": fun
}

