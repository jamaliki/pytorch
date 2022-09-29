# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class ExternalProperties(object):
    """The top-level element of an external property file."""

    addresses: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "addresses"}
    )
    artifacts: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "artifacts"}
    )
    conversion: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "conversion"}
    )
    driver: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "driver"}
    )
    extensions: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "extensions"}
    )
    externalized_properties: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "externalizedProperties"}
    )
    graphs: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "graphs"}
    )
    guid: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "guid"}
    )
    invocations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "invocations"}
    )
    logical_locations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "logicalLocations"}
    )
    policies: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "policies"}
    )
    properties: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    results: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "results"}
    )
    run_guid: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "runGuid"}
    )
    schema: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "schema"}
    )
    taxonomies: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "taxonomies"}
    )
    thread_flow_locations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "threadFlowLocations"}
    )
    translations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "translations"}
    )
    version: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "version"}
    )
    web_requests: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "webRequests"}
    )
    web_responses: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "webResponses"}
    )


# flake8: noqa
