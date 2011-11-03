from zope.component import getMultiAdapter

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class LinkToContactFormViewlet(ViewletBase):
    render = ViewPageTemplateFile('linktocontactform.pt')

    def update(self):
        self.contact_action = self._getContactAction()
        
    def _getContactAction(self):
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')
        site_actions = context_state.actions('site_actions')
        contact_actions = [ action for action in site_actions if action['id'] == 'contact' ]
        if len(contact_actions) != 1:
            return None
        return contact_actions[0]
