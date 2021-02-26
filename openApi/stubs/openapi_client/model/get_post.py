"""
    Hivemind OpenAPI Specification

    An OpenAPI specification for Hivemind  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.active_votes import ActiveVotes
    from openapi_client.model.beneficiares import Beneficiares
    from openapi_client.model.get_post_stats import GetPostStats
    globals()['ActiveVotes'] = ActiveVotes
    globals()['Beneficiares'] = Beneficiares
    globals()['GetPostStats'] = GetPostStats


class GetPost(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'active_votes': (ActiveVotes,),  # noqa: E501
            'author': (str,),  # noqa: E501
            'author_payout_value': (str,),  # noqa: E501
            'author_reputation': (float,),  # noqa: E501
            'beneficiaries': (Beneficiares,),  # noqa: E501
            'blacklists': ([str],),  # noqa: E501
            'body': (str,),  # noqa: E501
            'category': (str,),  # noqa: E501
            'children': (int,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'curator_payout_value': (str,),  # noqa: E501
            'depth': (int,),  # noqa: E501
            'is_paidout': (bool,),  # noqa: E501
            'json_metadata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'max_accepted_payout': (str,),  # noqa: E501
            'net_rshares': (int,),  # noqa: E501
            'payout': (float,),  # noqa: E501
            'payout_at': (datetime,),  # noqa: E501
            'pending_payout_value': (str,),  # noqa: E501
            'percent_hbd': (int,),  # noqa: E501
            'permlink': (str,),  # noqa: E501
            'post_id': (int,),  # noqa: E501
            'promoted': (str,),  # noqa: E501
            'replies': ([str],),  # noqa: E501
            'stats': (GetPostStats,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'updated': (datetime,),  # noqa: E501
            'url': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'active_votes': 'active_votes',  # noqa: E501
        'author': 'author',  # noqa: E501
        'author_payout_value': 'author_payout_value',  # noqa: E501
        'author_reputation': 'author_reputation',  # noqa: E501
        'beneficiaries': 'beneficiaries',  # noqa: E501
        'blacklists': 'blacklists',  # noqa: E501
        'body': 'body',  # noqa: E501
        'category': 'category',  # noqa: E501
        'children': 'children',  # noqa: E501
        'created': 'created',  # noqa: E501
        'curator_payout_value': 'curator_payout_value',  # noqa: E501
        'depth': 'depth',  # noqa: E501
        'is_paidout': 'is_paidout',  # noqa: E501
        'json_metadata': 'json_metadata',  # noqa: E501
        'max_accepted_payout': 'max_accepted_payout',  # noqa: E501
        'net_rshares': 'net_rshares',  # noqa: E501
        'payout': 'payout',  # noqa: E501
        'payout_at': 'payout_at',  # noqa: E501
        'pending_payout_value': 'pending_payout_value',  # noqa: E501
        'percent_hbd': 'percent_hbd',  # noqa: E501
        'permlink': 'permlink',  # noqa: E501
        'post_id': 'post_id',  # noqa: E501
        'promoted': 'promoted',  # noqa: E501
        'replies': 'replies',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'title': 'title',  # noqa: E501
        'updated': 'updated',  # noqa: E501
        'url': 'url',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, active_votes, author, author_payout_value, author_reputation, beneficiaries, blacklists, body, category, children, created, curator_payout_value, depth, is_paidout, json_metadata, max_accepted_payout, net_rshares, payout, payout_at, pending_payout_value, percent_hbd, permlink, post_id, promoted, replies, stats, title, updated, url, *args, **kwargs):  # noqa: E501
        """GetPost - a model defined in OpenAPI

        Args:
            active_votes (ActiveVotes):
            author (str): account name of the post's author
            author_payout_value (str): HBD paid to the author of the post
            author_reputation (float): author's reputation score
            beneficiaries (Beneficiares):
            blacklists ([str]):
            body (str): post content
            category (str): post category
            children (int): number of children comments
            created (datetime): creation date
            curator_payout_value (str): amount of HBD paid to curators
            depth (int): nesting level
            is_paidout (bool): information whether the post has been paid
            json_metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}):
            max_accepted_payout (str): maximal possible payout
            net_rshares (int): netto rshares, result of rshares allocations
            payout (float): amount of payout
            payout_at (datetime): date of payout
            pending_payout_value (str): pending or paid amount
            percent_hbd (int): percent of HBD, 1000 = 100%
            permlink (str): post's permlink
            post_id (int): id of the post, created from the author and the permlink
            promoted (str): amount of HBD if post is promoted
            replies ([str]):
            stats (GetPostStats):
            title (str): post title
            updated (datetime): date of update
            url (str): end of the url to the post, contains category, author and permlink

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.active_votes = active_votes
        self.author = author
        self.author_payout_value = author_payout_value
        self.author_reputation = author_reputation
        self.beneficiaries = beneficiaries
        self.blacklists = blacklists
        self.body = body
        self.category = category
        self.children = children
        self.created = created
        self.curator_payout_value = curator_payout_value
        self.depth = depth
        self.is_paidout = is_paidout
        self.json_metadata = json_metadata
        self.max_accepted_payout = max_accepted_payout
        self.net_rshares = net_rshares
        self.payout = payout
        self.payout_at = payout_at
        self.pending_payout_value = pending_payout_value
        self.percent_hbd = percent_hbd
        self.permlink = permlink
        self.post_id = post_id
        self.promoted = promoted
        self.replies = replies
        self.stats = stats
        self.title = title
        self.updated = updated
        self.url = url
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
