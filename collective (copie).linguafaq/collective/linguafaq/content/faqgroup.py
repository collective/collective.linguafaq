"""Definition of the FaqGroup content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from collective.linguafaq import linguafaqMessageFactory as _

from collective.linguafaq.interfaces import IFaqGroup
from collective.linguafaq.config import PROJECTNAME

FaqGroupSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
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

FaqGroupSchema['title'].storage = atapi.AnnotationStorage()
FaqGroupSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    FaqGroupSchema,
    folderish=True,
    moveDiscussion=False
)


class FaqGroup(folder.ATFolder):
    """classify faq"""
    implements(IFaqGroup)
    
    meta_type = "FaqGroup"
    schema = FaqGroupSchema
    
    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    
        
atapi.registerType(FaqGroup, PROJECTNAME)
