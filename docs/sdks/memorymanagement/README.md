# MemoryManagement

## Overview

### Available Operations

* [load_model](#load_model) - Load a model into active memory
* [stop_model](#stop_model) - Unload the active model from memory

## load_model

Manually loads a specified model file into Mac RAM/VRAM.

### Example Usage

<!-- UsageSnippet language="python" operationID="load_model" method="post" path="/run" -->
```python
from ajayji_sdk_test import SDK


with SDK() as sdk:

    res = sdk.memory_management.load_model(file_name="example.file")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The filename of the model (e.g. `llama-3-8b.gguf`).                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LoadModelResponseBody](../../models/loadmodelresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## stop_model

Clears the active model from RAM, freeing up system resources.

### Example Usage

<!-- UsageSnippet language="python" operationID="stop_model" method="post" path="/stop" -->
```python
from ajayji_sdk_test import SDK


with SDK() as sdk:

    res = sdk.memory_management.stop_model()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StopModelResponseBody](../../models/stopmodelresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |