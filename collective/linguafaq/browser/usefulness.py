from DateTime import DateTime
from zope.annotation.interfaces import IAnnotations
import zope.event

from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage

from collective.linguafaq import linguafaqMessageFactory as _
from collective.linguafaq.event import UsefulnessEvent

STORAGE_KEY = 'usefulness' # key for annotation storage
KEY_USEFUL = 'useful' # see _createVote
KEY_COMMENT = 'comment' # see _createVote
KEY_DATE = 'date' # see _createVote
KEY_IP = 'ip_address' # see _createVote
FORM_FIELD_USEFUL = 'useful' # equals form field in useful.pt
FORM_FIELD_COMMENT = 'comment' # equals form field in useful.pt

class UsefulnessView(BrowserView):
    """Parse the submitted "was this useful"-form.
    """

    def _getVotes(self):
        return IAnnotations(self.context).get(STORAGE_KEY, [])

    def _setVotes(self, votes):
        IAnnotations(self.context)[STORAGE_KEY] = votes

    def _createVote(self, useful, comment=None):
        now = DateTime()
        useful_int = int(useful)
        vote = {
            KEY_USEFUL: useful,
            KEY_COMMENT: comment,
            KEY_DATE: now,
            KEY_IP: self.request.getClientAddr(),
            }
        return vote
        
    def _addVote(self, vote):
        votes = self._getVotes()
        votes.append(vote)
        self._setVotes(votes)
        self.messages.addStatusMessage(_(u'message_thank_you', 
                                            default=u'Thank you for voting!'))
        event = UsefulnessEvent(self.context)
        zope.event.notify(event)

    def __call__(self):
        self.messages = IStatusMessage(self.request)
        form = self.request.form
        if not (form and form.has_key(FORM_FIELD_USEFUL)):
            self.messages.addStatusMessage('No form submitted.')
        else:
            vote = self._createVote(form[FORM_FIELD_USEFUL], 
                                    comment=form.get(FORM_FIELD_COMMENT, None))
            self._addVote(vote)
        self.request.RESPONSE.redirect(self.context.absolute_url())

