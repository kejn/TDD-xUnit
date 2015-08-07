'''
Created on 7 sie 2015

@author: KNIEMCZY
'''
class TestCase:
    def __init__(self,name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self, name)
    def testMethod(self):
        self.wasRun = True
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = True

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)
        
TestCaseTest("testSetUp").run()
TestCaseTest("testRunning").run()
