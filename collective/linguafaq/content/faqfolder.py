"""Definition of the FaqFolder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from collective.linguafaq.interfaces import IFaqFolder
from collective.linguafaq.config import PROJECTNAME

FaqFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

FaqFolderSchema['title'].storage = atapi.AnnotationStorage()
FaqFolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    FaqFolderSchema,
    folderish=True,
    moveDiscussion=False
)


class FaqFolder(folder.ATFolder):
    """Description of the Example Type"""
    implements(IFaqFolder)

    meta_type = "FaqFolder"
    schema = FaqFolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(FaqFolder, PROJECTNAME)
