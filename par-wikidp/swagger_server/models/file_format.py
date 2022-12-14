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
from swagger_server.models.developer_information import DeveloperInformation
from swagger_server.models.document_information import DocumentInformation
from swagger_server.models.external_signature_information import ExternalSignatureInformation
from swagger_server.models.identifier_information import IdentifierInformation
from swagger_server.models.internal_signature_information import InternalSignatureInformation
from swagger_server.models.par_identifier import ParIdentifier
from swagger_server.models.provenance_information import ProvenanceInformation
from swagger_server.models.registry_version_information import RegistryVersionInformation
from swagger_server.models.related_format_information import RelatedFormatInformation
from swagger_server import util


class FileFormat(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, aliases: List[str]=None, binary_file_format: str=None, byte_orders: List[str]=None, description: str=None, developers: List[DeveloperInformation]=None, disclosure: str=None, documents: List[DocumentInformation]=None, external_signatures: List[ExternalSignatureInformation]=None, families: List[str]=None, id: ParIdentifier=None, identifiers: List[IdentifierInformation]=None, internal_signatures: List[InternalSignatureInformation]=None, last_updated_date: str=None, local_last_modified_date: str=None, name: str=None, note: str=None, provenance: ProvenanceInformation=None, registry_versions: List[RegistryVersionInformation]=None, related_formats: List[RelatedFormatInformation]=None, release_date: str=None, risk: str=None, technical_environment: str=None, types: List[str]=None, version: str=None, withdrawn_date: str=None):  # noqa: E501
        """FileFormat - a model defined in Swagger

        :param aliases: The aliases of this FileFormat.  # noqa: E501
        :type aliases: List[str]
        :param binary_file_format: The binary_file_format of this FileFormat.  # noqa: E501
        :type binary_file_format: str
        :param byte_orders: The byte_orders of this FileFormat.  # noqa: E501
        :type byte_orders: List[str]
        :param description: The description of this FileFormat.  # noqa: E501
        :type description: str
        :param developers: The developers of this FileFormat.  # noqa: E501
        :type developers: List[DeveloperInformation]
        :param disclosure: The disclosure of this FileFormat.  # noqa: E501
        :type disclosure: str
        :param documents: The documents of this FileFormat.  # noqa: E501
        :type documents: List[DocumentInformation]
        :param external_signatures: The external_signatures of this FileFormat.  # noqa: E501
        :type external_signatures: List[ExternalSignatureInformation]
        :param families: The families of this FileFormat.  # noqa: E501
        :type families: List[str]
        :param id: The id of this FileFormat.  # noqa: E501
        :type id: ParIdentifier
        :param identifiers: The identifiers of this FileFormat.  # noqa: E501
        :type identifiers: List[IdentifierInformation]
        :param internal_signatures: The internal_signatures of this FileFormat.  # noqa: E501
        :type internal_signatures: List[InternalSignatureInformation]
        :param last_updated_date: The last_updated_date of this FileFormat.  # noqa: E501
        :type last_updated_date: str
        :param local_last_modified_date: The local_last_modified_date of this FileFormat.  # noqa: E501
        :type local_last_modified_date: str
        :param name: The name of this FileFormat.  # noqa: E501
        :type name: str
        :param note: The note of this FileFormat.  # noqa: E501
        :type note: str
        :param provenance: The provenance of this FileFormat.  # noqa: E501
        :type provenance: ProvenanceInformation
        :param registry_versions: The registry_versions of this FileFormat.  # noqa: E501
        :type registry_versions: List[RegistryVersionInformation]
        :param related_formats: The related_formats of this FileFormat.  # noqa: E501
        :type related_formats: List[RelatedFormatInformation]
        :param release_date: The release_date of this FileFormat.  # noqa: E501
        :type release_date: str
        :param risk: The risk of this FileFormat.  # noqa: E501
        :type risk: str
        :param technical_environment: The technical_environment of this FileFormat.  # noqa: E501
        :type technical_environment: str
        :param types: The types of this FileFormat.  # noqa: E501
        :type types: List[str]
        :param version: The version of this FileFormat.  # noqa: E501
        :type version: str
        :param withdrawn_date: The withdrawn_date of this FileFormat.  # noqa: E501
        :type withdrawn_date: str
        """
        self.swagger_types = {
            'aliases': List[str],
            'binary_file_format': str,
            'byte_orders': List[str],
            'description': str,
            'developers': List[DeveloperInformation],
            'disclosure': str,
            'documents': List[DocumentInformation],
            'external_signatures': List[ExternalSignatureInformation],
            'families': List[str],
            'id': ParIdentifier,
            'identifiers': List[IdentifierInformation],
            'internal_signatures': List[InternalSignatureInformation],
            'last_updated_date': str,
            'local_last_modified_date': str,
            'name': str,
            'note': str,
            'provenance': ProvenanceInformation,
            'registry_versions': List[RegistryVersionInformation],
            'related_formats': List[RelatedFormatInformation],
            'release_date': str,
            'risk': str,
            'technical_environment': str,
            'types': List[str],
            'version': str,
            'withdrawn_date': str
        }

        self.attribute_map = {
            'aliases': 'aliases',
            'binary_file_format': 'binaryFileFormat',
            'byte_orders': 'byteOrders',
            'description': 'description',
            'developers': 'developers',
            'disclosure': 'disclosure',
            'documents': 'documents',
            'external_signatures': 'externalSignatures',
            'families': 'families',
            'id': 'id',
            'identifiers': 'identifiers',
            'internal_signatures': 'internalSignatures',
            'last_updated_date': 'lastUpdatedDate',
            'local_last_modified_date': 'localLastModifiedDate',
            'name': 'name',
            'note': 'note',
            'provenance': 'provenance',
            'registry_versions': 'registryVersions',
            'related_formats': 'relatedFormats',
            'release_date': 'releaseDate',
            'risk': 'risk',
            'technical_environment': 'technicalEnvironment',
            'types': 'types',
            'version': 'version',
            'withdrawn_date': 'withdrawnDate'
        }

        self._aliases = aliases
        self._binary_file_format = binary_file_format
        self._byte_orders = byte_orders
        self._description = description
        self._developers = developers
        self._disclosure = disclosure
        self._documents = documents
        self._external_signatures = external_signatures
        self._families = families
        self._id = id
        self._identifiers = identifiers
        self._internal_signatures = internal_signatures
        self._last_updated_date = last_updated_date
        self._local_last_modified_date = local_last_modified_date
        self._name = name
        self._note = note
        self._provenance = provenance
        self._registry_versions = registry_versions
        self._related_formats = related_formats
        self._release_date = release_date
        self._risk = risk
        self._technical_environment = technical_environment
        self._types = types
        self._version = version
        self._withdrawn_date = withdrawn_date

    @classmethod
    def from_dict(cls, dikt) -> 'FileFormat':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileFormat of this FileFormat.  # noqa: E501
        :rtype: FileFormat
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aliases(self) -> List[str]:
        """Gets the aliases of this FileFormat.


        :return: The aliases of this FileFormat.
        :rtype: List[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases: List[str]):
        """Sets the aliases of this FileFormat.


        :param aliases: The aliases of this FileFormat.
        :type aliases: List[str]
        """

        self._aliases = aliases

    @property
    def binary_file_format(self) -> str:
        """Gets the binary_file_format of this FileFormat.


        :return: The binary_file_format of this FileFormat.
        :rtype: str
        """
        return self._binary_file_format

    @binary_file_format.setter
    def binary_file_format(self, binary_file_format: str):
        """Sets the binary_file_format of this FileFormat.


        :param binary_file_format: The binary_file_format of this FileFormat.
        :type binary_file_format: str
        """

        self._binary_file_format = binary_file_format

    @property
    def byte_orders(self) -> List[str]:
        """Gets the byte_orders of this FileFormat.


        :return: The byte_orders of this FileFormat.
        :rtype: List[str]
        """
        return self._byte_orders

    @byte_orders.setter
    def byte_orders(self, byte_orders: List[str]):
        """Sets the byte_orders of this FileFormat.


        :param byte_orders: The byte_orders of this FileFormat.
        :type byte_orders: List[str]
        """

        self._byte_orders = byte_orders

    @property
    def description(self) -> str:
        """Gets the description of this FileFormat.


        :return: The description of this FileFormat.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this FileFormat.


        :param description: The description of this FileFormat.
        :type description: str
        """

        self._description = description

    @property
    def developers(self) -> List[DeveloperInformation]:
        """Gets the developers of this FileFormat.


        :return: The developers of this FileFormat.
        :rtype: List[DeveloperInformation]
        """
        return self._developers

    @developers.setter
    def developers(self, developers: List[DeveloperInformation]):
        """Sets the developers of this FileFormat.


        :param developers: The developers of this FileFormat.
        :type developers: List[DeveloperInformation]
        """

        self._developers = developers

    @property
    def disclosure(self) -> str:
        """Gets the disclosure of this FileFormat.


        :return: The disclosure of this FileFormat.
        :rtype: str
        """
        return self._disclosure

    @disclosure.setter
    def disclosure(self, disclosure: str):
        """Sets the disclosure of this FileFormat.


        :param disclosure: The disclosure of this FileFormat.
        :type disclosure: str
        """

        self._disclosure = disclosure

    @property
    def documents(self) -> List[DocumentInformation]:
        """Gets the documents of this FileFormat.


        :return: The documents of this FileFormat.
        :rtype: List[DocumentInformation]
        """
        return self._documents

    @documents.setter
    def documents(self, documents: List[DocumentInformation]):
        """Sets the documents of this FileFormat.


        :param documents: The documents of this FileFormat.
        :type documents: List[DocumentInformation]
        """

        self._documents = documents

    @property
    def external_signatures(self) -> List[ExternalSignatureInformation]:
        """Gets the external_signatures of this FileFormat.


        :return: The external_signatures of this FileFormat.
        :rtype: List[ExternalSignatureInformation]
        """
        return self._external_signatures

    @external_signatures.setter
    def external_signatures(self, external_signatures: List[ExternalSignatureInformation]):
        """Sets the external_signatures of this FileFormat.


        :param external_signatures: The external_signatures of this FileFormat.
        :type external_signatures: List[ExternalSignatureInformation]
        """

        self._external_signatures = external_signatures

    @property
    def families(self) -> List[str]:
        """Gets the families of this FileFormat.


        :return: The families of this FileFormat.
        :rtype: List[str]
        """
        return self._families

    @families.setter
    def families(self, families: List[str]):
        """Sets the families of this FileFormat.


        :param families: The families of this FileFormat.
        :type families: List[str]
        """

        self._families = families

    @property
    def id(self) -> ParIdentifier:
        """Gets the id of this FileFormat.


        :return: The id of this FileFormat.
        :rtype: ParIdentifier
        """
        return self._id

    @id.setter
    def id(self, id: ParIdentifier):
        """Sets the id of this FileFormat.


        :param id: The id of this FileFormat.
        :type id: ParIdentifier
        """

        self._id = id

    @property
    def identifiers(self) -> List[IdentifierInformation]:
        """Gets the identifiers of this FileFormat.


        :return: The identifiers of this FileFormat.
        :rtype: List[IdentifierInformation]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers: List[IdentifierInformation]):
        """Sets the identifiers of this FileFormat.


        :param identifiers: The identifiers of this FileFormat.
        :type identifiers: List[IdentifierInformation]
        """

        self._identifiers = identifiers

    @property
    def internal_signatures(self) -> List[InternalSignatureInformation]:
        """Gets the internal_signatures of this FileFormat.


        :return: The internal_signatures of this FileFormat.
        :rtype: List[InternalSignatureInformation]
        """
        return self._internal_signatures

    @internal_signatures.setter
    def internal_signatures(self, internal_signatures: List[InternalSignatureInformation]):
        """Sets the internal_signatures of this FileFormat.


        :param internal_signatures: The internal_signatures of this FileFormat.
        :type internal_signatures: List[InternalSignatureInformation]
        """

        self._internal_signatures = internal_signatures

    @property
    def last_updated_date(self) -> str:
        """Gets the last_updated_date of this FileFormat.


        :return: The last_updated_date of this FileFormat.
        :rtype: str
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date: str):
        """Sets the last_updated_date of this FileFormat.


        :param last_updated_date: The last_updated_date of this FileFormat.
        :type last_updated_date: str
        """

        self._last_updated_date = last_updated_date

    @property
    def local_last_modified_date(self) -> str:
        """Gets the local_last_modified_date of this FileFormat.


        :return: The local_last_modified_date of this FileFormat.
        :rtype: str
        """
        return self._local_last_modified_date

    @local_last_modified_date.setter
    def local_last_modified_date(self, local_last_modified_date: str):
        """Sets the local_last_modified_date of this FileFormat.


        :param local_last_modified_date: The local_last_modified_date of this FileFormat.
        :type local_last_modified_date: str
        """

        self._local_last_modified_date = local_last_modified_date

    @property
    def name(self) -> str:
        """Gets the name of this FileFormat.


        :return: The name of this FileFormat.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this FileFormat.


        :param name: The name of this FileFormat.
        :type name: str
        """

        self._name = name

    @property
    def note(self) -> str:
        """Gets the note of this FileFormat.


        :return: The note of this FileFormat.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note: str):
        """Sets the note of this FileFormat.


        :param note: The note of this FileFormat.
        :type note: str
        """

        self._note = note

    @property
    def provenance(self) -> ProvenanceInformation:
        """Gets the provenance of this FileFormat.


        :return: The provenance of this FileFormat.
        :rtype: ProvenanceInformation
        """
        return self._provenance

    @provenance.setter
    def provenance(self, provenance: ProvenanceInformation):
        """Sets the provenance of this FileFormat.


        :param provenance: The provenance of this FileFormat.
        :type provenance: ProvenanceInformation
        """

        self._provenance = provenance

    @property
    def registry_versions(self) -> List[RegistryVersionInformation]:
        """Gets the registry_versions of this FileFormat.


        :return: The registry_versions of this FileFormat.
        :rtype: List[RegistryVersionInformation]
        """
        return self._registry_versions

    @registry_versions.setter
    def registry_versions(self, registry_versions: List[RegistryVersionInformation]):
        """Sets the registry_versions of this FileFormat.


        :param registry_versions: The registry_versions of this FileFormat.
        :type registry_versions: List[RegistryVersionInformation]
        """

        self._registry_versions = registry_versions

    @property
    def related_formats(self) -> List[RelatedFormatInformation]:
        """Gets the related_formats of this FileFormat.


        :return: The related_formats of this FileFormat.
        :rtype: List[RelatedFormatInformation]
        """
        return self._related_formats

    @related_formats.setter
    def related_formats(self, related_formats: List[RelatedFormatInformation]):
        """Sets the related_formats of this FileFormat.


        :param related_formats: The related_formats of this FileFormat.
        :type related_formats: List[RelatedFormatInformation]
        """

        self._related_formats = related_formats

    @property
    def release_date(self) -> str:
        """Gets the release_date of this FileFormat.


        :return: The release_date of this FileFormat.
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date: str):
        """Sets the release_date of this FileFormat.


        :param release_date: The release_date of this FileFormat.
        :type release_date: str
        """

        self._release_date = release_date

    @property
    def risk(self) -> str:
        """Gets the risk of this FileFormat.


        :return: The risk of this FileFormat.
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk: str):
        """Sets the risk of this FileFormat.


        :param risk: The risk of this FileFormat.
        :type risk: str
        """

        self._risk = risk

    @property
    def technical_environment(self) -> str:
        """Gets the technical_environment of this FileFormat.


        :return: The technical_environment of this FileFormat.
        :rtype: str
        """
        return self._technical_environment

    @technical_environment.setter
    def technical_environment(self, technical_environment: str):
        """Sets the technical_environment of this FileFormat.


        :param technical_environment: The technical_environment of this FileFormat.
        :type technical_environment: str
        """

        self._technical_environment = technical_environment

    @property
    def types(self) -> List[str]:
        """Gets the types of this FileFormat.


        :return: The types of this FileFormat.
        :rtype: List[str]
        """
        return self._types

    @types.setter
    def types(self, types: List[str]):
        """Sets the types of this FileFormat.


        :param types: The types of this FileFormat.
        :type types: List[str]
        """

        self._types = types

    @property
    def version(self) -> str:
        """Gets the version of this FileFormat.


        :return: The version of this FileFormat.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this FileFormat.


        :param version: The version of this FileFormat.
        :type version: str
        """

        self._version = version

    @property
    def withdrawn_date(self) -> str:
        """Gets the withdrawn_date of this FileFormat.


        :return: The withdrawn_date of this FileFormat.
        :rtype: str
        """
        return self._withdrawn_date

    @withdrawn_date.setter
    def withdrawn_date(self, withdrawn_date: str):
        """Sets the withdrawn_date of this FileFormat.


        :param withdrawn_date: The withdrawn_date of this FileFormat.
        :type withdrawn_date: str
        """

        self._withdrawn_date = withdrawn_date
