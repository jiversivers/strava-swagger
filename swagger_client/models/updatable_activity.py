# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class UpdatableActivity(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'commute': 'bool',
        'trainer': 'bool',
        'hide_from_home': 'bool',
        'description': 'str',
        'name': 'str',
        'type': 'ActivityType',
        'sport_type': 'SportType',
        'gear_id': 'str'
    }

    attribute_map = {
        'commute': 'commute',
        'trainer': 'trainer',
        'hide_from_home': 'hide_from_home',
        'description': 'description',
        'name': 'name',
        'type': 'type',
        'sport_type': 'sport_type',
        'gear_id': 'gear_id'
    }

    def __init__(self, commute=None, trainer=None, hide_from_home=None, description=None, name=None, type=None, sport_type=None, gear_id=None, _configuration=None):  # noqa: E501
        """UpdatableActivity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._commute = None
        self._trainer = None
        self._hide_from_home = None
        self._description = None
        self._name = None
        self._type = None
        self._sport_type = None
        self._gear_id = None
        self.discriminator = None

        if commute is not None:
            self.commute = commute
        if trainer is not None:
            self.trainer = trainer
        if hide_from_home is not None:
            self.hide_from_home = hide_from_home
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if sport_type is not None:
            self.sport_type = sport_type
        if gear_id is not None:
            self.gear_id = gear_id

    @property
    def commute(self):
        """Gets the commute of this UpdatableActivity.  # noqa: E501

        Whether this activity is a commute  # noqa: E501

        :return: The commute of this UpdatableActivity.  # noqa: E501
        :rtype: bool
        """
        return self._commute

    @commute.setter
    def commute(self, commute):
        """Sets the commute of this UpdatableActivity.

        Whether this activity is a commute  # noqa: E501

        :param commute: The commute of this UpdatableActivity.  # noqa: E501
        :type: bool
        """

        self._commute = commute

    @property
    def trainer(self):
        """Gets the trainer of this UpdatableActivity.  # noqa: E501

        Whether this activity was recorded on a training machine  # noqa: E501

        :return: The trainer of this UpdatableActivity.  # noqa: E501
        :rtype: bool
        """
        return self._trainer

    @trainer.setter
    def trainer(self, trainer):
        """Sets the trainer of this UpdatableActivity.

        Whether this activity was recorded on a training machine  # noqa: E501

        :param trainer: The trainer of this UpdatableActivity.  # noqa: E501
        :type: bool
        """

        self._trainer = trainer

    @property
    def hide_from_home(self):
        """Gets the hide_from_home of this UpdatableActivity.  # noqa: E501

        Whether this activity is muted  # noqa: E501

        :return: The hide_from_home of this UpdatableActivity.  # noqa: E501
        :rtype: bool
        """
        return self._hide_from_home

    @hide_from_home.setter
    def hide_from_home(self, hide_from_home):
        """Sets the hide_from_home of this UpdatableActivity.

        Whether this activity is muted  # noqa: E501

        :param hide_from_home: The hide_from_home of this UpdatableActivity.  # noqa: E501
        :type: bool
        """

        self._hide_from_home = hide_from_home

    @property
    def description(self):
        """Gets the description of this UpdatableActivity.  # noqa: E501

        The description of the activity  # noqa: E501

        :return: The description of this UpdatableActivity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatableActivity.

        The description of the activity  # noqa: E501

        :param description: The description of this UpdatableActivity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdatableActivity.  # noqa: E501

        The name of the activity  # noqa: E501

        :return: The name of this UpdatableActivity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatableActivity.

        The name of the activity  # noqa: E501

        :param name: The name of this UpdatableActivity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this UpdatableActivity.  # noqa: E501

        Deprecated. Prefer to use sport_type. In a request where both type and sport_type are present, this field will be ignored  # noqa: E501

        :return: The type of this UpdatableActivity.  # noqa: E501
        :rtype: ActivityType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdatableActivity.

        Deprecated. Prefer to use sport_type. In a request where both type and sport_type are present, this field will be ignored  # noqa: E501

        :param type: The type of this UpdatableActivity.  # noqa: E501
        :type: ActivityType
        """

        self._type = type

    @property
    def sport_type(self):
        """Gets the sport_type of this UpdatableActivity.  # noqa: E501


        :return: The sport_type of this UpdatableActivity.  # noqa: E501
        :rtype: SportType
        """
        return self._sport_type

    @sport_type.setter
    def sport_type(self, sport_type):
        """Sets the sport_type of this UpdatableActivity.


        :param sport_type: The sport_type of this UpdatableActivity.  # noqa: E501
        :type: SportType
        """

        self._sport_type = sport_type

    @property
    def gear_id(self):
        """Gets the gear_id of this UpdatableActivity.  # noqa: E501

        Identifier for the gear associated with the activity. ‘none’ clears gear from activity  # noqa: E501

        :return: The gear_id of this UpdatableActivity.  # noqa: E501
        :rtype: str
        """
        return self._gear_id

    @gear_id.setter
    def gear_id(self, gear_id):
        """Sets the gear_id of this UpdatableActivity.

        Identifier for the gear associated with the activity. ‘none’ clears gear from activity  # noqa: E501

        :param gear_id: The gear_id of this UpdatableActivity.  # noqa: E501
        :type: str
        """

        self._gear_id = gear_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdatableActivity, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatableActivity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatableActivity):
            return True

        return self.to_dict() != other.to_dict()
