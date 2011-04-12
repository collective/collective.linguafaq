from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.linguafaq import linguafaqMessageFactory as _


class IOnefaqView(Interface):
    """
    One faq view interface
    """

    def onefaq():
        """ onefaq method"""


class OnefaqView(BrowserView):
    """
    One faq browser view
    """
    implements(IOnefaqView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def onefaq(self):
        """
        onefaq method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}
