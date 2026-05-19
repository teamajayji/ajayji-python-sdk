# ToolsAndInfrastructure

## Overview

### Available Operations

* [create_database](#create_database) - Provision a Local Database Tool

## create_database

Ingests a CSV file into the local Sembast database and auto-provisions it as a `toml-database` Tool.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_database" method="post" path="/databases/create" -->
```python
from ajayji_sdk_test import SDK


with SDK() as sdk:

    res = sdk.tools_and_infrastructure.create_database(csv_path="<value>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `csv_path`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The absolute file path to the CSV file on the local machine.        |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The human-readable name of the new database tool.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateDatabaseResponseBody](../../models/createdatabaseresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |