# ConvertModelRequestBody


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `height`                                   | *OptionalNullable[int]*                    | :heavy_minus_sign:                         | Target height for image models.            |
| `input_mapping`                            | *str*                                      | :heavy_check_mark:                         | The name of the input tensor/layer.        |
| `name`                                     | *str*                                      | :heavy_check_mark:                         | Name to register the resulting tool as.    |
| `output_mapping`                           | *str*                                      | :heavy_check_mark:                         | The name of the output tensor/layer.       |
| `source_file_path`                         | *str*                                      | :heavy_check_mark:                         | Absolute path to the source model file.    |
| `type`                                     | *str*                                      | :heavy_check_mark:                         | The type of model (e.g., 'image', 'text'). |
| `width`                                    | *OptionalNullable[int]*                    | :heavy_minus_sign:                         | Target width for image models.             |