<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
from ajayji import SDK
import asyncio

async def main():

    async with SDK() as sdk:

        res = await sdk.mcp_management.post_api_v1_mcp_connect_async(mcp_servers=[
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ])

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->