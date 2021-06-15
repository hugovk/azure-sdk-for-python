# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.synapse.monitoring.core.rest import HttpRequest

from .. import models as _models
from ..rest import monitoring as rest_monitoring

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class MonitoringOperations(object):
    """MonitoringOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.monitoring.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_spark_job_list(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SparkJobListViewResponse"
        """Get list of spark applications for the workspace.

        :keyword x_ms_client_request_id: Can provide a guid, which is helpful for debugging and to
         provide better customer support.
        :paramtype x_ms_client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SparkJobListViewResponse, or the result of cls(response)
        :rtype: ~azure.synapse.monitoring.models.SparkJobListViewResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SparkJobListViewResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        x_ms_client_request_id = kwargs.pop("x_ms_client_request_id", None)  # type: Optional[str]

        request = rest_monitoring.build_get_spark_job_list_request(
            x_ms_client_request_id=x_ms_client_request_id,
            template_url=self.get_spark_job_list.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SparkJobListViewResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_spark_job_list.metadata = {"url": "/monitoring/workloadTypes/spark/Applications"}  # type: ignore

    def get_sql_job_query_string(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SqlQueryStringDataModel"
        """Get SQL OD/DW Query for the workspace.

        :keyword x_ms_client_request_id: Can provide a guid, which is helpful for debugging and to
         provide better customer support.
        :paramtype x_ms_client_request_id: str
        :keyword filter:
        :paramtype filter: str
        :keyword orderby:
        :paramtype orderby: str
        :keyword skip:
        :paramtype skip: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SqlQueryStringDataModel, or the result of cls(response)
        :rtype: ~azure.synapse.monitoring.models.SqlQueryStringDataModel
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SqlQueryStringDataModel"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        x_ms_client_request_id = kwargs.pop("x_ms_client_request_id", None)  # type: Optional[str]
        filter = kwargs.pop("filter", None)  # type: Optional[str]
        orderby = kwargs.pop("orderby", None)  # type: Optional[str]
        skip = kwargs.pop("skip", None)  # type: Optional[str]

        request = rest_monitoring.build_get_sql_job_query_string_request(
            x_ms_client_request_id=x_ms_client_request_id,
            filter=filter,
            orderby=orderby,
            skip=skip,
            template_url=self.get_sql_job_query_string.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("SqlQueryStringDataModel", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_sql_job_query_string.metadata = {"url": "/monitoring/workloadTypes/sql/querystring"}  # type: ignore
