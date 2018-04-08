# -*- coding: utf-8 -*-

import os
from plotlib.unixbenchplotter import UnixBenchPlotter
from plotlib.geekbenchplotter import GeekBenchPlotter

def plotUnixBench(isMultiCore, files):
    unixbench_plotter = UnixBenchPlotter('UnixBench' + ('_Multi_Core' if isMultiCore else '_Single_Core'))
    unixbench_plotter.setIsMultiCore(isMultiCore)

    for f in files:
        unixbench_plotter.addFile(f)

    unixbench_plotter.plot()

    os.rename('output.png', unixbench_plotter.getName().replace(' ', '_') + '.png')
    print('Rename output.png to {}'.format(unixbench_plotter.getName() + '.png'))

def plotGeekBench(isMultiCore, files):
    geekbench_plotter = GeekBenchPlotter('GeekBench' + ('_Multi_Core' if isMultiCore else '_Single_Core'))
    geekbench_plotter.setIsMultiCore(isMultiCore)

    for f in files:
        geekbench_plotter.addFile(f)

    geekbench_plotter.plot()

    os.rename('output.png', geekbench_plotter.getName().replace(' ', '_') + '.png')
    print('Rename output.png to {}'.format(geekbench_plotter.getName() + '.png'))

def findFiles(path, pred = None, ls = None):
    if ls == None:
        ls = []

    for p in os.listdir(path):
        p = os.path.join(path, p)
        if os.path.isfile(p):
            if not pred or pred(p):
                ls.append(p)

    return ls

if __name__ == "__main__":
    path = input('Please input vps test output files directory:\n')
    print('\n')

    # unixbench
    unixbench_files = findFiles(path, lambda f : 'unixbench' in f and f.endswith('.txt'))

    plotUnixBench(True, unixbench_files)
    plotUnixBench(False, unixbench_files)

    # geekbench
    geekbench_files = findFiles(path, lambda f : 'geekbench' in f and f.endswith('.html'))

    plotGeekBench(True, geekbench_files)
    plotGeekBench(False, geekbench_files)

    print('\ndone!')
