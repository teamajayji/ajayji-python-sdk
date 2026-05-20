# DataIngestionAndTools

## Overview

### Available Operations

* [create_database](#create_database) - Provision a Local Database Tool
* [create_vector_db](#create_vector_db) - Provision a Vector DB Tool
* [execute_tool](#execute_tool) - Execute a Tool Statelessly

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

    res = sdk.data_ingestion_and_tools.create_vector_db(embedding_model="<value>", folder_path="<value>", name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `embedding_model`                                                                                | *str*                                                                                            | :heavy_check_mark:                                                                               | The filename of the active GGUF model to use for embeddings (e.g. `all-MiniLM-L6-v2-gguf.gguf`). |
| `folder_path`                                                                                    | *str*                                                                                            | :heavy_check_mark:                                                                               | The absolute file path to the folder containing documents to index.                              |
| `name`                                                                                           | *str*                                                                                            | :heavy_check_mark:                                                                               | The human-readable name of the new vector DB tool.                                               |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[models.CreateVectorDbResponseBody](../../models/createvectordbresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## execute_tool

Programmatically executes a registered tool (e.g. Database, Vector Store, CoreML model) and returns the JSON result.

### Example Usage

<!-- UsageSnippet language="python" operationID="execute_tool" method="post" path="/tools/execute" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.data_ingestion_and_tools.execute_tool(tool_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tool_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The registered name of the tool to execute.                         |
| `args`                                                              | Dict[str, *Any*]                                                    | :heavy_minus_sign:                                                  | A JSON object containing the arguments required by the tool.        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Dict[str, Any]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |