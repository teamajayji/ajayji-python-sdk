# ExecuteToolRequestBody


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `args`                                                       | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | A JSON object containing the arguments required by the tool. |
| `tool_name`                                                  | *str*                                                        | :heavy_check_mark:                                           | The registered name of the tool to execute.                  |