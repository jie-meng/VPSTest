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

if __name__ == "__main__":
    vps = VPS('aws.t2.micro')
    vps.setData('Dhrystone 2 using register variables', 2767.7)
    vps.setData('Double-Precision Whetstone', 707.5)
    vps.setData('Execl Throughput', 914.8)
    vps.setData('File Copy 1024 bufsize 2000 maxblocks', 1720.8)
    vps.setData('File Copy 256 bufsize 500 maxblocks', 1070.4)
    vps.setData('File Copy 4096 bufsize 8000 maxblocks', 4012.2)
    vps.setData('Pipe Throughput', 764.5)

    print(vps.getAttrs())
