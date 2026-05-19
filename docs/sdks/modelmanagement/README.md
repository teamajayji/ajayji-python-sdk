# ModelManagement

## Overview

### Available Operations

* [pull_model](#pull_model) - Download a model from Hugging Face

## pull_model

Triggers a background download of a model to local storage.

### Example Usage

<!-- UsageSnippet language="python" operationID="pull_model" method="post" path="/pull" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.model_management.pull_model(file_name="example.file", repo="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_name`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The exact filename to download (e.g., `model.gguf`).                |
| `repo`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The Hugging Face repository (e.g., `unsloth/gemma-2b`).             |
| `huggingface_config_id`                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Optional ID for an authenticated Hugging Face token.                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PullModelResponseBody](../../models/pullmodelresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |