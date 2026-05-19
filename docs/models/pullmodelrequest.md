# PullModelRequest


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `repo`                                                  | *str*                                                   | :heavy_check_mark:                                      | The Hugging Face repository (e.g., `unsloth/gemma-2b`). |
| `file_name`                                             | *str*                                                   | :heavy_check_mark:                                      | The exact filename to download (e.g., `model.gguf`).    |
| `huggingface_config_id`                                 | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | Optional ID for an authenticated Hugging Face token.    |