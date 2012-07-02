# -*- coding: utf-8 -*-

import unittest2 as unittest

from AccessControl import Unauthorized

from zope.interface.verify import verifyClass, verifyObject

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.linguafaq.content.faqfolder import FaqFolder
from collective.linguafaq.interfaces import IFaqFolder
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

    def test_adding(self):
        self.assertTrue(IFaqFolder.providedBy(self.ff))
        self.assertTrue(verifyClass(IFaqFolder, FaqFolder))

    def test_interface(self):
        obj = FaqFolder(None)
        self.assertTrue(IFaqFolder.providedBy(obj))
        self.assertTrue(verifyObject(IFaqFolder, obj))

    def test_unauthorized(self):
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.assertRaises(Unauthorized,
                          self.folder.invokeFactory, 'FaqFolder', 'foo')

    def test_allowed_content_types(self):
        types = ['FaqGroup', 'FaqItem']
        self.assertListEqual(self.ff.getLocallyAllowedTypes(), types)
        self.assertListEqual(self.ff.getImmediatelyAddableTypes(), types)
        self.assertRaises(ValueError,
                          self.ff.invokeFactory, 'Document', 'foo')
        try:
            self.ff.invokeFactory('FaqGroup', 'foo')
            self.ff.invokeFactory('FaqItem', 'bar')
        except Unauthorized:
            self.fail()
