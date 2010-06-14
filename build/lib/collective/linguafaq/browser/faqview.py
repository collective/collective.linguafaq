from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.linguafaq import linguafaqMessageFactory as _


class IfaqView(Interface):
    """
    faq_view view interface
    """

    def getAllFaq():
        """ getAllFaq method"""

    def getAllSubfolder():
        """ getAllFaq method"""
        

class faqView(BrowserView):
    """
    faq_view browser view
    """
    implements(IfaqView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

       
    def getAllFaq(self):
        results=[]
        cat = self.portal_catalog
        path = "/".join(self.context.getPhysicalPath())
        items = cat.searchResults( {'portal_type' :'FaqItem','path':path} )
        for item in items :
            obj = item.getObject()
            results.append({"title":obj.Title(),"answer":obj.getAnswer()})
        
        return results
        
    def getAllSubfolder(self):
        results=[]
        cat = self.portal_catalog
        folder_path = "/".join(self.context.getPhysicalPath())
        items = cat.searchResults(path={'query': folder_path, 'depth': 1})
        for item in items :
            obj = item.getObject()
            lurl = '/'.join(obj.getPhysicalPath())
            hrefurl = '%s%s' %(self.context.portal_url(),lurl)
            results.append({"title":obj.Title(), "type":obj.Type(), "faqurl": hrefurl})
            if obj.Type()=='faqgroup':
                faqitems= cat.searchResults( {'portal_type' :'FaqItem','path':lurl} )
                for faqitem in faqitems :
                    objitem = faqitem.getObject()
                    lurl = '/'.join(objitem.getPhysicalPath())
                    hrefurl = '%s%s' %(self.context.portal_url(),lurl)
                    results.append({"title":objitem.Title(),"type":objitem.Type(), "faqurl":hrefurl})
        return results
    
