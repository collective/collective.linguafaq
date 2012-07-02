# -*- coding: utf-8 -*-

import unittest2 as unittest

from AccessControl import Unauthorized

from zope.interface.verify import verifyClass, verifyObject

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.linguafaq.content.faqgroup import FaqGroup
from collective.linguafaq.interfaces import IFaqGroup
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
        self.ff.invokeFactory('FaqGroup', 'fg')
        self.fg = self.ff['fg']

    def test_adding(self):
        self.assertTrue(IFaqGroup.providedBy(self.fg))
        self.assertTrue(verifyClass(IFaqGroup, FaqGroup))

    def test_interface(self):
        obj = FaqGroup(None)
        self.assertTrue(IFaqGroup.providedBy(obj))
        self.assertTrue(verifyObject(IFaqGroup, obj))

    def test_unauthorized(self):
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.assertRaises(Unauthorized,
                          self.ff.invokeFactory, 'FaqGroup', 'foo')

    def test_allowed_content_types(self):
        types = ['FaqItem']
        self.assertListEqual(self.fg.getLocallyAllowedTypes(), types)
        self.assertListEqual(self.fg.getImmediatelyAddableTypes(), types)
        self.assertRaises(ValueError,
                          self.fg.invokeFactory, 'Document', 'foo')
        try:
            self.fg.invokeFactory('FaqItem', 'foo')
        except Unauthorized:
            self.fail()
