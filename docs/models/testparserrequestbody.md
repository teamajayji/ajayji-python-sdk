# TestParserRequestBody


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `raw_input`                                                 | *str*                                                       | :heavy_check_mark:                                          | The raw string (usually JSON) to feed into the parser.      |
| `script`                                                    | *str*                                                       | :heavy_check_mark:                                          | The raw Javascript containing a `parse(rawInput)` function. |