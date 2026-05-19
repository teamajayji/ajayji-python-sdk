# AskRequestBody


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `agent_id`                                              | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | Optional ID of the Persona to route this query through. |
| `query`                                                 | *str*                                                   | :heavy_check_mark:                                      | The prompt to send to the local model.                  |