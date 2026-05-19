# ModelManagement

## Overview

### Available Operations

* [convert_model](#convert_model) - Convert Model to CoreML
* [pull_model](#pull_model) - Download a model from Hugging Face

## convert_model

Headless conversion of a model (e.g., .h5, .pt) to an Apple CoreML `.mlpackage` via the streaming service.

### Example Usage

<!-- UsageSnippet language="python" operationID="convert_model" method="post" path="/models/convert" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.model_management.convert_model(input_mapping="<value>", name="<value>", output_mapping="<value>", source_file_path="<value>", type_="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `input_mapping`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The name of the input tensor/layer.                                 |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Name to register the resulting tool as.                             |
| `output_mapping`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The name of the output tensor/layer.                                |
| `source_file_path`                                                  | *str*                                                               | :heavy_check_mark:                                                  | Absolute path to the source model file.                             |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The type of model (e.g., 'image', 'text').                          |
| `height`                                                            | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | Target height for image models.                                     |
| `width`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | Target width for image models.                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

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