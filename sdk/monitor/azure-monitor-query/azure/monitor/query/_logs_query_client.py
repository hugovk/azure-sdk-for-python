#
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING, Any, Union, Sequence, Dict, Optional
from azure.core.exceptions import HttpResponseError

from ._generated._monitor_query_client import MonitorQueryClient

from ._generated.models import BatchRequest, QueryBody as LogsQueryBody
from ._helpers import get_authentication_policy, process_error, construct_iso8601, order_results
from ._models import LogsQueryResult, LogsBatchQuery, LogsBatchQueryResult

if TYPE_CHECKING:
    from azure.core.credentials import TokenCredential
    from datetime import timedelta


class LogsQueryClient(object):
    """LogsQueryClient

    .. admonition:: Example:

    .. literalinclude:: ../samples/sample_log_query_client.py
        :start-after: [START client_auth_with_token_cred]
        :end-before: [END client_auth_with_token_cred]
        :language: python
        :dedent: 0
        :caption: Creating the LogsQueryClient with a TokenCredential.

    :param credential: The credential to authenticate the client.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword endpoint: The endpoint to connect to. Defaults to 'https://api.loganalytics.io'.
    :paramtype endpoint: str
    """

    def __init__(self, credential, **kwargs):
        # type: (TokenCredential, Any) -> None

        self._endpoint = kwargs.pop('endpoint', 'https://api.loganalytics.io/v1')
        self._client = MonitorQueryClient(
            credential=credential,
            authentication_policy=get_authentication_policy(credential),
            base_url=self._endpoint,
            **kwargs
        )
        self._query_op = self._client.query

    def query(self, workspace_id, query, timespan=None, **kwargs):
        # type: (str, str, Optional[timedelta], Any) -> LogsQueryResult
        """Execute an Analytics query.

        Executes an Analytics query for data.

        :param workspace_id: ID of the workspace. This is Workspace ID from the Properties blade in the
         Azure portal.
        :type workspace_id: str
        :param query: The Analytics query. Learn more about the `Analytics query syntax
         <https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/>`_.
        :type query: str
        :param timespan: The timespan for which to query the data. This can be a timedelta,
         a timedelta and a start datetime, or a start datetime/end datetime.
        :type timespan: ~datetime.timedelta or tuple[~datetime.datetime, ~datetime.timedelta]
         or tuple[~datetime.datetime, ~datetime.datetime]
        :keyword int server_timeout: the server timeout in seconds. The default timeout is 3 minutes,
         and the maximum timeout is 10 minutes.
        :keyword bool include_statistics: To get information about query statistics.
        :keyword bool include_visualization: In the query language, it is possible to specify different
         visualization options. By default, the API does not return information regarding the type of
         visualization to show. If your client requires this information, specify the preference
        :keyword additional_workspaces: A list of workspaces that are included in the query.
         These can be qualified workspace names, workspace Ids, or Azure resource Ids.
        :paramtype additional_workspaces: list[str]
        :return: QueryResults, or the result of cls(response)
        :rtype: ~azure.monitor.query.LogsQueryResult
        :raises: ~azure.core.exceptions.HttpResponseError

        .. admonition:: Example:

        .. literalinclude:: ../samples/sample_log_query_client.py
            :start-after: [START send_logs_query]
            :end-before: [END send_logs_query]
            :language: python
            :dedent: 0
            :caption: Get a response for a single Log Query
        """
        timespan = construct_iso8601(timespan)
        include_statistics = kwargs.pop("include_statistics", False)
        include_visualization = kwargs.pop("include_visualization", False)
        server_timeout = kwargs.pop("server_timeout", None)
        workspaces = kwargs.pop("additional_workspaces", None)

        prefer = ""
        if server_timeout:
            prefer += "wait=" + str(server_timeout)
        if include_statistics:
            if len(prefer) > 0:
                prefer += ","
            prefer += "include-statistics=true"
        if include_visualization:
            if len(prefer) > 0:
                prefer += ","
            prefer += "include-render=true"

        body = LogsQueryBody(
            query=query,
            timespan=timespan,
            workspaces=workspaces,
            **kwargs
        )

        try:
            return LogsQueryResult._from_generated(self._query_op.execute( # pylint: disable=protected-access
                workspace_id=workspace_id,
                body=body,
                prefer=prefer,
                **kwargs
            ))
        except HttpResponseError as e:
            process_error(e)

    def query_batch(self, queries, **kwargs):
        # type: (Union[Sequence[Dict], Sequence[LogsBatchQuery]], Any) -> Sequence[LogsBatchQueryResult]
        """Execute a list of analytics queries. Each request can be either a LogQueryRequest
        object or an equivalent serialized model.

        The response is returned in the same order as that of the requests sent.

        :param queries: The list of queries that should be processed
        :type queries: list[dict] or list[~azure.monitor.query.LogsBatchQuery]
        :return: List of LogsBatchQueryResult, or the result of cls(response)
        :rtype: ~list[~azure.monitor.query.LogsBatchQueryResult]
        :raises: ~azure.core.exceptions.HttpResponseError

        .. admonition:: Example:

        .. literalinclude:: ../samples/sample_batch_query.py
            :start-after: [START send_query_batch]
            :end-before: [END send_query_batch]
            :language: python
            :dedent: 0
            :caption: Get a response for multiple Log Queries.
        """
        try:
            queries = [LogsBatchQuery(**q) for q in queries]
        except (KeyError, TypeError):
            pass
        queries = [q._to_generated() for q in queries] # pylint: disable=protected-access
        try:
            request_order = [req.id for req in queries]
        except AttributeError:
            request_order = [req['id'] for req in queries]
        batch = BatchRequest(requests=queries)
        generated = self._query_op.batch(batch, **kwargs)
        return order_results(
            request_order,
            [
                LogsBatchQueryResult._from_generated(rsp) for rsp in generated.responses # pylint: disable=protected-access
            ])

    def close(self):
        # type: () -> None
        """Close the :class:`~azure.monitor.query.LogsQueryClient` session."""
        return self._client.close()

    def __enter__(self):
        # type: () -> LogsQueryClient
        self._client.__enter__()  # pylint:disable=no-member
        return self

    def __exit__(self, *args):
        # type: (*Any) -> None
        self._client.__exit__(*args)  # pylint:disable=no-member
