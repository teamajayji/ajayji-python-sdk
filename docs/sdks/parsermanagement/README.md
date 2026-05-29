# ParserManagement

## Overview

### Available Operations

* [create_parser](#create_parser) - Create a Javascript Parser
* [list_parsers](#list_parsers) - List all available Parsers
* [test_parser](#test_parser) - Test a Javascript Parser

## create_parser

Provisions a new Javascript parser script for modifying inputs, outputs, and tool calls.

### Example Usage

<!-- UsageSnippet language="python" operationID="create_parser" method="post" path="/api/v1/parsers" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.parser_management.create_parser(name="<value>", script="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The display name of the parser.                                     |
| `script`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The raw Javascript containing a `parse(rawInput)` function.         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | An optional description of what the parser does.                    |
| `file_path`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Optional filepath associated with this parser.                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateParserResponseBody](../../models/createparserresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## list_parsers

Retrieves a list of all provisioned Javascript parsers in the local database.

### Example Usage

<!-- UsageSnippet language="python" operationID="list_parsers" method="get" path="/parsers/list" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.parser_management.list_parsers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListParsersResponseBody](../../models/listparsersresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## test_parser

Executes a Javascript parsing script statelessly to validate its output against a test input.

### Example Usage

<!-- UsageSnippet language="python" operationID="test_parser" method="post" path="/api/v1/parsers/test" -->
```python
from ajayji import SDK


with SDK() as sdk:

    res = sdk.parser_management.test_parser(raw_input="<value>", script="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `raw_input`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The raw string (usually JSON) to feed into the parser.              |
| `script`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The raw Javascript containing a `parse(rawInput)` function.         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TestParserResponseBody](../../models/testparserresponsebody.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |