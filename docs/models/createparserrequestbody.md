# CreateParserRequestBody


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `description`                                               | *OptionalNullable[str]*                                     | :heavy_minus_sign:                                          | An optional description of what the parser does.            |
| `file_path`                                                 | *OptionalNullable[str]*                                     | :heavy_minus_sign:                                          | Optional filepath associated with this parser.              |
| `name`                                                      | *str*                                                       | :heavy_check_mark:                                          | The display name of the parser.                             |
| `script`                                                    | *str*                                                       | :heavy_check_mark:                                          | The raw Javascript containing a `parse(rawInput)` function. |