'''
Created on 7 sie 2015

@author: KNIEMCZY
'''
class TestCase:
    def __init__(self,name):
        self.name = name
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):#,restult):
#         result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self, name)
    def testMethod(self):
#         self.wasRun = True
        self.log = self.log + "testMethod "
    def setUp(self):
#         self.wasRun = None
#         self.wasSetUp = True
        self.log = "setUp "
    def tearDown(self):
        self.log = self.log + "tearDown "

class TestCaseTest(TestCase):
    def setUp(self):
        pass
#     def testRunning(self):
#         self.test.run()
#         assert(self.test.wasRun)
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)
        
TestCaseTest("testTemplateMethod").run()
# TestCaseTest("testRunning").run()
