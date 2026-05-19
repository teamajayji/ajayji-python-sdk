# DataIngestionAndTools

## Overview

### Available Operations

* [create_database](#create_database) - Provision a Local Database Tool
* [create_vector_db](#create_vector_db) - Provision a Vector DB Tool

## create_database

Ingests a CSV file into the local Sembast database and auto-provisions it as a `toml-database` Tool.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_database" method="post" path="/databases/create" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.data_ingestion_and_tools.create_database(csv_path="<value>", name="<value>")

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

## create_vector_db

Indexes a local folder of documents into a Vector Database and auto-provisions it as a `toml-vector-store` Tool.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_vector_db" method="post" path="/vector-dbs/create" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.data_ingestion_and_tools.create_vector_db(folder_path="<value>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_path`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The absolute file path to the folder containing documents to index. |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The human-readable name of the new vector DB tool.                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateVectorDbResponseBody](../../models/createvectordbresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |