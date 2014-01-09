from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.testing import z2

from zope.configuration import xmlconfig

class CollectivemobifyjsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.mobifyjs
        self.loadZCML(package=collective.mobifyjs)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'collective.mobifyjs:default')


        from Products.CMFPlone.utils import _createObjectByType
        _createObjectByType('Document', portal, id='test-mobifyjs', title='Test Mobify.js')

        portal['test-mobifyjs'].setText(
            '<img src="https://plone.org/logo.png" alt="Plone logo"/>',
            mimetype='text/html'
        )


COLLECTIVE_MOBIFYJS_FIXTURE = CollectivemobifyjsLayer()
COLLECTIVE_MOBIFYJS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_MOBIFYJS_FIXTURE,),
    name="CollectivemobifyjsLayer:Integration"
)
COLLECTIVE_MOBIFYJS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_MOBIFYJS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectivemobifyjsLayer:Functional"
)
COLLECTIVE_MOBIFYJS_ROBOT_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_MOBIFYJS_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name="collective.mobifyjs:Robot"
)