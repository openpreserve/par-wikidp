#!/usr/bin/python3
# coding: UTF-8
#
# PAR Consortium
# Copyright (C) 2020
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InputToolArgument(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, type: str=None, value: str=None):  # noqa: E501
        """InputToolArgument - a model defined in Swagger

        :param description: The description of this InputToolArgument.  # noqa: E501
        :type description: str
        :param type: The type of this InputToolArgument.  # noqa: E501
        :type type: str
        :param value: The value of this InputToolArgument.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'description': str,
            'type': str,
            'value': str
        }

        self.attribute_map = {
            'description': 'description',
            'type': 'type',
            'value': 'value'
        }

        self._description = description
        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'InputToolArgument':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InputToolArgument of this InputToolArgument.  # noqa: E501
        :rtype: InputToolArgument
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> str:
        """Gets the description of this InputToolArgument.


        :return: The description of this InputToolArgument.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this InputToolArgument.


        :param description: The description of this InputToolArgument.
        :type description: str
        """

        self._description = description

    @property
    def type(self) -> str:
        """Gets the type of this InputToolArgument.


        :return: The type of this InputToolArgument.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this InputToolArgument.


        :param type: The type of this InputToolArgument.
        :type type: str
        """

        self._type = type

    @property
    def value(self) -> str:
        """Gets the value of this InputToolArgument.


        :return: The value of this InputToolArgument.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this InputToolArgument.


        :param value: The value of this InputToolArgument.
        :type value: str
        """

        self._value = value
