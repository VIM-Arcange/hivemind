# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ListAllSubscriptionsRequestParams(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account=None):  # noqa: E501
        """ListAllSubscriptionsRequestParams - a model defined in OpenAPI

        :param account: The account of this ListAllSubscriptionsRequestParams.  # noqa: E501
        :type account: str
        """
        self.openapi_types = {
            'account': str
        }

        self.attribute_map = {
            'account': 'account'
        }

        self._account = account

    @classmethod
    def from_dict(cls, dikt) -> 'ListAllSubscriptionsRequestParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListAllSubscriptionsRequest_params of this ListAllSubscriptionsRequestParams.  # noqa: E501
        :rtype: ListAllSubscriptionsRequestParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account(self):
        """Gets the account of this ListAllSubscriptionsRequestParams.

        account name  # noqa: E501

        :return: The account of this ListAllSubscriptionsRequestParams.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ListAllSubscriptionsRequestParams.

        account name  # noqa: E501

        :param account: The account of this ListAllSubscriptionsRequestParams.
        :type account: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account
