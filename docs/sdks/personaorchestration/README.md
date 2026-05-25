# PersonaOrchestration

## Overview

### Available Operations

* [create_persona](#create_persona) - Create or Update a Persona
* [invoke_persona](#invoke_persona) - Invoke a Persona Webhook

## create_persona

Creates a new Persona or updates an existing one, optionally registering MCP servers for bi-directional tool execution.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_persona" method="post" path="/api/v1/personas" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.persona_orchestration.create_persona(agent_id="<id>", agent_name="<value>", model="Charger")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                          | *str*                                                                                               | :heavy_check_mark:                                                                                  | The unique ID for this Persona.                                                                     |
| `agent_name`                                                                                        | *str*                                                                                               | :heavy_check_mark:                                                                                  | The human-readable name of the Persona.                                                             |
| `model`                                                                                             | *str*                                                                                               | :heavy_check_mark:                                                                                  | The filename of the LLM to use (e.g., llama-3-8b.gguf).                                             |
| `mcp_servers`                                                                                       | List[*str*]                                                                                         | :heavy_minus_sign:                                                                                  | A list of MCP Server SSE URIs (e.g., http://127.0.0.1:8000/sse) to connect to during orchestration. |
| `system_prompt`                                                                                     | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Optional system prompt to override the default.                                                     |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.CreatePersonaResponseBody](../../models/createpersonaresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## invoke_persona

Executes a full orchestration pipeline (Tools, JS Parsers, CoreML) for a specific Persona using a JSON payload.

### Example Usage

<!-- UsageSnippet language="python" operationID="invoke_persona" method="post" path="/api/v1/personas/{id}/invoke" -->
```python
from ajayji import SDK


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