"""Definition of the FaqItem content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata


# -*- Message Factory Imported Here -*-
from collective.linguafaq import linguafaqMessageFactory as _

from collective.linguafaq.interfaces import IFaqItem
from collective.linguafaq.config import PROJECTNAME

FaqItemSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'answer',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"faqanswer"),
            description=_(u"faqanswerdesc"),
        ),
        required=True,
    ),
    
    atapi.BooleanField('excludeFromNav',
        required = False,
        languageIndependent = True,
        schemata = 'default', # moved to 'default' for folders
        widget = atapi.BooleanWidget(
            description=_(u'help_exclude_from_nav', default=u'If selected, this item will not appear in the navigation tree'),
            label = _(u'label_exclude_from_nav', default=u'Exclude from navigation'),
            visible={'view' : 'hidden',
                     'edit' : 'visible'},
        ),
        default=True,
    ),
    
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

FaqItemSchema['title'].storage = atapi.AnnotationStorage()
FaqItemSchema['title'].widget.label = _(u"faqquestion")
FaqItemSchema['title'].widget.description = _(u"faqquestiondesc")
#FaqItemSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(FaqItemSchema, moveDiscussion=False)


class FaqItem(base.ATCTContent):
    """one question and one answer"""
    implements(IFaqItem)
    
    meta_type = "FaqItem"
    schema = FaqItemSchema

    title = atapi.ATFieldProperty('title')
    #description = atapi.ATFieldProperty('description')

        
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    answer = atapi.ATFieldProperty('answer')


atapi.registerType(FaqItem, PROJECTNAME)
