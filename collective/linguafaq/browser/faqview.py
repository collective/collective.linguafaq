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
        results = []
        cat = self.portal_catalog
        folder_path = "/".join(self.context.getPhysicalPath())
        items = cat.searchResults(path={'query': folder_path, 'depth': 1}, 
                                sort_on='sortable_title', sort_order='ascending')
        for item in items :
            obj = item.getObject()            
            if obj.Type()=='faqgroup':
                group={}
                group['title']=obj.Title()
                group['url']=obj.absolute_url()
                list_faq=[]
                url = '/'.join(obj.getPhysicalPath())
                faqitems = cat.searchResults( {'portal_type' :'FaqItem','path':url} , 
                                sort_on='sortable_title', sort_order='ascending')
                for faqitem in faqitems:
                    objfaq = faqitem.getObject()
                    list_faq.append({"title": objfaq.Title(), "answer": objfaq.getText(), "url": objfaq.absolute_url()})
                group['faqs'] = list_faq
                group['answer'] = ""
                results.append(group)
            else:
                results.append({"title": obj.Title(), "answer": obj.getText(),"faqs":[], "url": obj.absolute_url()})
        return results
        
    def getAllIndex(self):
        results = []
        cat = self.portal_catalog
        folder_path = "/".join(self.context.getPhysicalPath())
        items = cat.searchResults(path={'query': folder_path, 'depth': 1}, 
                                sort_on='sortable_title', sort_order='ascending')
        for item in items :
            obj = item.getObject()            
            if obj.Type()=='faqgroup':
                group={}
                group['title']=obj.Title()
                group['url']=obj.absolute_url()
                list_faq=[]
                url = '/'.join(obj.getPhysicalPath())
                faqitems = cat.searchResults( {'portal_type' :'FaqItem','path':url} , 
                                sort_on='sortable_title', sort_order='ascending')
                for faqitem in faqitems:
                    objfaq = faqitem.getObject()
                    list_faq.append({"title": objfaq.Title(), "url": objfaq.absolute_url()})
                group['faqs'] = list_faq
                results.append(group)
            else:
                results.append({"title": obj.Title(), "faqs":[], "url": obj.absolute_url()})
        return results
    
