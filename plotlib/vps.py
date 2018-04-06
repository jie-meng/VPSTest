# -*- coding: utf-8 -*-

class VPS(object):

    def __init__(self, name):
        self.__name = name
        self.__data = {}

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def setData(self, attrName, value):
        self.__data[attrName] = value

    def getData(self, attrName):
        return self.__data[attrName]

    def getAttrs(self):
        return list(self.__data.keys())