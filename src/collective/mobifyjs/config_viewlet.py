"""

    Viewlets for storing Mobify.js settings in meta elements

"""

# Zope imports
from Acquisition import aq_inner
from zope.component import getUtility, ComponentLookupError

from zope.interface import Interface
from five import grok

# Plone imports
from plone.app.layout.viewlets.interfaces import IHtmlHead
from plone.registry.interfaces import IRegistry

from collective.mobifyjs.settings import ISettings

# The viewlets in this file are rendered on every content item type
grok.context(Interface)

# Use templates directory to search for templates.
grok.templatedir('templates')

class MobifyConfigViewlet(grok.Viewlet):
    """ A viewlet which will include some custom code in <head> if the condition is met """

    grok.viewletmanager(IHtmlHead)

    def get_settings(self):
        """
        Get collective.mobifyjs Site Setup settings
        """
        try:

            # Will raise an exception if plone.app.registry is not quick installed
            registry = getUtility(IRegistry)

            # Will raise exception if your product add-on installer has not been run
            settings = registry.forInterface(ISettings)
        except (KeyError, ComponentLookupError):
            # Registry schema and actual values do not match
            # Quick installer has not been run or need to rerun
            # to update registry.xml values to database
            return None

        return settings
