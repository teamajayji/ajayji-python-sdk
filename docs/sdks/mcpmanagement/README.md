# McpManagement

## Overview

### Available Operations

* [post_api_v1_mcp_connect](#post_api_v1_mcp_connect) - Explicitly connect to an MCP Server
* [post_api_v1_mcp_disconnect](#post_api_v1_mcp_disconnect) - Explicitly disconnect from an MCP Server

## post_api_v1_mcp_connect

Establishes a persistent Server-Sent Events (SSE) connection to an MCP host.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/api/v1/mcp/connect" method="post" path="/api/v1/mcp/connect" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.mcp_management.post_api_v1_mcp_connect(mcp_servers=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `mcp_servers`                                                       | List[*str*]                                                         | :heavy_check_mark:                                                  | A list containing the SSE URI of the MCP server.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostAPIV1McpConnectResponseBody](../../models/postapiv1mcpconnectresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## post_api_v1_mcp_disconnect

Closes the persistent SSE connection to the MCP host and cleans up resources.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/api/v1/mcp/disconnect" method="post" path="/api/v1/mcp/disconnect" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.mcp_management.post_api_v1_mcp_disconnect()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostAPIV1McpDisconnectResponseBody](../../models/postapiv1mcpdisconnectresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |