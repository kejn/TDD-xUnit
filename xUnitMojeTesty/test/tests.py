'''
Created on 7 sie 2015

@author: KNIEMCZY
'''
class WasRun:
    def __init__(self,name):
        self.wasRun = None
    def testMethod(self):
        self.wasRun = True

test = WasRun("testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)