import unittest

import robotsuite
from collective.mobifyjs.testing import COLLECTIVE_MOBIFYJS_ROBOT_TESTING
from plone.testing import layered


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite('test_functional.robot'),
                layer=COLLECTIVE_MOBIFYJS_ROBOT_TESTING),
    ])
    return suite