"""

    Define add-on settings.

"""


from zope import schema
from five import grok
from Products.CMFCore.interfaces import ISiteRoot

from plone.z3cform import layout
from plone.directives import form
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from collective.mobifyjs import _

class ISettings(form.Schema):
    """ Define settings data structure """

    mobify_library_url = schema.TextLine(
        title=_(u'Mobify.js library URL'),
        default=u'//cdn.mobify.com/mobifyjs/build/mobify-2.0.5.min.js'
    )

    mobify_resize_backend = schema.TextLine(
        title=_(u'Resize backend'),
        description=_(u'Leave empty to use the default Mobify.js resize backend.')
    )

class SettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = ISettings
    label = u"collective.mobifyjs settings"

class SettingsView(grok.View):
    """
    View which wrap the settings form using ControlPanelFormWrapper to a HTML boilerplate frame.
    """
    grok.name("collective.mobifyjs-settings")
    grok.context(ISiteRoot)

    def render(self):
        view_factor = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
        view = view_factor(self.context, self.request)
        return view()

