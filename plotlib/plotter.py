# -*- coding: utf-8 -*-

import os
from pyecharts import Bar
from .vps import VPS

def plot(title, vpsList, labelSize):
    if len(vpsList) == 0:
        return

    bar = Bar(title)
    attrs = vpsList[0].getAttrs()

    for vps in vpsList:
        values = []
        for attr in reversed(attrs):
            values.append(vps.getData(attr))
        bar.add(vps.getName(), list(reversed(attrs)), values, is_convert = True, yaxis_label_textsize = labelSize)

    bar.render()
    os.system('snapshot render.html')
    os.remove('render.html')
