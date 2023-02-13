import unittest

from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLogInPage
from test_cases.framework import Test


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(Test))
   test_suite.addTest(makeSuite(TestLogInPage))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())