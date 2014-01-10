from Products.CMFCore.utils import getToolByName
import unittest2 as unittest
from zope.component import getMultiAdapter

from plone.app.testing import login
from plone.app.testing import SITE_OWNER_NAME
from plone.registry import Registry

from collective.mobifyjs.settings import ISettings, SettingsView, RESIZE_URL

from collective.mobifyjs.testing import \
    COLLECTIVE_MOBIFYJS_INTEGRATION_TESTING

class TestSettings(unittest.TestCase):

    layer = COLLECTIVE_MOBIFYJS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = Registry()
        self.registry.registerInterface(ISettings)

    def test_setup(self):
        pq = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(pq.isProductInstalled('collective.mobifyjs'))

    def test_registry(self):
        settings = self.registry.forInterface(ISettings)

        self.assertEquals(settings.mobify_library_url, RESIZE_URL)
        self.assertEquals(settings.mobify_resize_backend, None)

    def test_controlpanel_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name="collective.mobifyjs-settings")

        self.assertEqual(view.__class__, SettingsView)
        self.failUnless(view())

