import PackageSnippet1 as pkg1
import unittest

class TestCV2X(unittest.TestCase): 
    
    def test_module1_hello(self):
        self.assertTrue(pkg1.subpackage1.moduleA.fun_a())
    
    def test_module2_hello(self):
        self.assertTrue(pkg1.subpackage2.moduleB.fun_b())
    
if __name__ == '__main__':
    unittest.main() 


