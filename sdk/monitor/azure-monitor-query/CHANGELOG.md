# Release History

## 1.0.0b4 (Unreleased)

### Features Added

### Breaking Changes

- Rename `batch_query` to `query_batch`.
- Rename `LogsBatchQueryRequest` to `LogsBatchQuery`.
- `include_render` is now renamed to `include_visualization` in the query API.
- `LogsQueryResult` and `LogsBatchQueryResult` now return `visualization` instead of `render`.
- `start_time`, `duration` and `end_time` are now replaced with a single param called `timespan`
- `resourceregion` is renamed to `resource_region` in the MetricResult type.
- `top` is renamed to `max_results` in the metric's `query` API.
- `metric_namespace_name` is renamed to `fully_qualified_namespace`
- `is_dimension_required` is renamed to `dimension_required`
- `time_grain` is renamed to `granularity`

### Bugs Fixed

- `include_statistics` and `include_visualization` args can now work together.

### Other Changes

## 1.0.0b3 (2021-08-09)

### Features Added

- Added enum `AggregationType` which can be used to specify aggregations in the query API.
- Added `LogsBatchQueryResult` model that is returned for a logs batch query.
- Added `error` attribute to `LogsQueryResult`.

### Breaking Changes

- `aggregation` param in the query API is renamed to `aggregations`
- `batch_query` API now returns a list of responses.
- `LogsBatchResults` model is now removed.
- `LogsQueryRequest` is renamed to `LogsBatchQueryRequest`
- `LogsQueryResults` is now renamed to `LogsQueryResult`
- `LogsBatchQueryResult` now has 4 additional attributes - `tables`, `error`, `statistics` and `render` instead of `body` attribute.

## 1.0.0b2 (2021-07-06)

### Breaking Changes

- `workspaces`, `workspace_ids`, `qualified_names` and `azure_resource_ids` are now merged into a single `additional_workspaces` list in the query API.
- The `LogQueryRequest` object now takes in a `workspace_id` and `additional_workspaces` instead of `workspace`.
- `aggregation` param is now a list instead of a string in the `query` method.
- `duration` must now be provided as a timedelta instead of a string.


## 1.0.0b1 (2021-06-10)

  **Features**
  - Version (1.0.0b1) is the first preview of our efforts to create a user-friendly and Pythonic client library for Azure Monitor Query.
  For more information about this, and preview releases of other Azure SDK libraries, please visit https://azure.github.io/azure-sdk/releases/latest/python.html.
  - Added `~azure.monitor.query.LogsQueryClient` to query log analytics along with `~azure.monitor.query.aio.LogsQueryClient`.
  - Implements the `~azure.monitor.query.MetricsQueryClient` for querying metrics, listing namespaces and metric definitions along with `~azure.monitor.query.aio.MetricsQueryClient`.
