from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from collective.linguafaq import linguafaqMessageFactory as _


class IFaqItem(Interface):
    """one question and one answer"""

    # -*- schema definition goes here -*-
    
    answer = schema.Text(
        title=_(u"Answer"),
        required=True,
        description=_(u"a answer for a question"),
    )
  
#
