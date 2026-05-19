# StatelessExecution

## Overview

### Available Operations

* [ask](#ask) - Ask the active LLM a question statelessly

## ask

Executes a query against the currently loaded active model. Bypasses Persona parsing unless an agent_id is provided.

### Example Usage

<!-- UsageSnippet language="python" operationID="ask" method="post" path="/ask" -->
```python
from ajayji_sdk_test import SDK


with SDK() as sdk:

    res = sdk.stateless_execution.ask(query="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The prompt to send to the local model.                              |
| `agent_id`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Optional ID of the Persona to route this query through.             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AskResponseBody](../../models/askresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |