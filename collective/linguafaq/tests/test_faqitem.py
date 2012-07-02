# -*- coding: utf-8 -*-

import unittest2 as unittest

from AccessControl import Unauthorized

from zope.interface.verify import verifyClass, verifyObject

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.linguafaq.content.faqitem import FaqItem
from collective.linguafaq.interfaces import IFaqItem
from collective.linguafaq.testing import INTEGRATION_TESTING


class ContentTypeTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        self.folder = self.portal['test-folder']

        self.folder.invokeFactory('FaqFolder', 'ff')
        self.ff = self.folder['ff']
        self.ff.invokeFactory('FaqItem', 'fi')
        self.fi = self.ff['fi']

    def test_adding(self):
        self.assertTrue(IFaqItem.providedBy(self.fi))
        self.assertTrue(verifyClass(IFaqItem, FaqItem))

    def test_interface(self):
        obj = FaqItem(None)
        self.assertTrue(IFaqItem.providedBy(obj))
        self.assertTrue(verifyObject(IFaqItem, obj))

    def test_unauthorized(self):
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.assertRaises(Unauthorized,
                          self.ff.invokeFactory, 'FaqItem', 'foo')
