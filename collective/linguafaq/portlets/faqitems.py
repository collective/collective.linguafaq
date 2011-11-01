from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from Products.CMFCore import permissions
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider

from collective.linguafaq import linguafaqMessageFactory as _
from collective.linguafaq.interfaces import IFaqItem

class IFaqItems(IPortletDataProvider):
    pass

class Assignment(base.Assignment):
    implements(IFaqItems)

    @property
    def title(self):
        return _(u"FAQ items")

class AddForm(base.AddForm):
    form_fields = form.Fields(IFaqItems)
    label = _(u"Add FAQ items portlet")
    description = _(u"This portlet lists FAQ items.")

    def create(self, data):
        return Assignment()

class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('faqitems.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        plone_tools = getMultiAdapter((context, self.request), name=u'plone_tools')
        self.catalog = plone_tools.catalog()

    def render(self):
        return self._template()

    @property
    def available(self):
        """Show the portlet only if there are FAQ items
        """
        return len(self._data())

    def faqitems(self):
        return self._data()

    @property
    def title(self):
        return Assignment().title

    # @memoize
    def _data(self):
        """Returns a list of FAQ Items
        """
        query = {
            'object_provides': IFaqItem.__identifier__,
            'sort_on' : 'modified',
            }
        results = self.catalog.searchResults(**query)
        return results
