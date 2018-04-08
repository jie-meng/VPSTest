# -*- coding: utf-8 -*-

import plotlib.output_parser.geekbench as GeekbenchParser
import plotlib.plotter as plotter

class GeekBenchPlotter(object):

    def __init__(self, name):
        self.__name = name
        self.__vpsList = []
        self.__isMultiCore = False

    def getName(self):
        return self.__name

    def setIsMultiCore(self, multiOrSingle):
        self.__isMultiCore = multiOrSingle

    def isMultiCore(self):
        return self.__isMultiCore

    def addFile(self, fileName):
        self.__vpsList.append(GeekbenchParser.parse(fileName))

    def plot(self):
        ls = []
        for x in self.__vpsList:
            ls.append(x[1] if self.isMultiCore() else x[0])

        plotter.plot(self.__name, ls, 10)
