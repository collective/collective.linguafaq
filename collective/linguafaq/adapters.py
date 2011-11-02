from zope.component import adapts 
 
from Products.CMFPlone import PloneMessageFactory
from Products.CMFCore.interfaces import IContentish

from plone.stringinterp import _ as PloneStringInterpMessageFactory
from plone.stringinterp.adapters import BaseSubstitution
from plone.stringinterp.interfaces import IStringSubstitution 

from collective.linguafaq import linguafaqMessageFactory as _
from collective.linguafaq.config import KEY_USEFUL, KEY_COMMENT
from collective.linguafaq.manager import UsefulnessManager

class usefulnessRatingCommentSubstitution(BaseSubstitution):
    adapts(IContentish)

    category = PloneStringInterpMessageFactory(u'All Content')
    description = _(u'label_comment', default=u'Comment')

    def safe_call(self):
        manager = UsefulnessManager(self.context)
        last_vote_comment = manager.getVotes()[-1].get(KEY_COMMENT)
        return last_vote_comment

class usefulnessRatingValueSubstitution(BaseSubstitution):
    adapts(IContentish)

    category = PloneStringInterpMessageFactory(u'All Content')
    description = _(u'label_value', default=u'Rating')

    def safe_call(self):
        manager = UsefulnessManager(self.context)
        last_vote_value = manager.getVotes()[-1].get(KEY_USEFUL)
        if last_vote_value:
            value = PloneMessageFactory('Yes')
        else:
            value = PloneMessageFactory('No')
        return value