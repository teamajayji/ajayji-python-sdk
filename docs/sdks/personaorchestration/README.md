# PersonaOrchestration

## Overview

### Available Operations

* [invoke_persona](#invoke_persona) - Invoke a Persona Webhook

## invoke_persona

Executes a full orchestration pipeline (Tools, JS Parsers, CoreML) for a specific Persona using a JSON payload.

### Example Usage

<!-- UsageSnippet language="python" operationID="invoke_persona" method="post" path="/personas/{id}/invoke" -->
```python
from ajayji_sdk_test import SDK


with SDK() as sdk:

    res = sdk.persona_orchestration.invoke_persona(id="<id>", request_body={
        "key": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique ID of the ChatPersona to invoke.                         |
| `request_body`                                                      | Dict[str, *Any*]                                                    | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InvokePersonaResponseBody](../../models/invokepersonaresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |