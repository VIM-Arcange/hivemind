"""
    Hivemind OpenAPI Specification

    An OpenAPI specification for Hivemind  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.community_context import CommunityContext
from openapi_client.model.list_community_roles import ListCommunityRoles
globals()['CommunityContext'] = CommunityContext
globals()['ListCommunityRoles'] = ListCommunityRoles
from openapi_client.model.community import Community


class TestCommunity(unittest.TestCase):
    """Community unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommunity(self):
        """Test Community"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Community()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
