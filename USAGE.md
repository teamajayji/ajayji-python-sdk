<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from ajayji_sdk_test import SDK


with SDK() as sdk:

    res = sdk.stateless_execution.ask(query="<value>")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
from ajayji_sdk_test import SDK
import asyncio

async def main():

    async with SDK() as sdk:

        res = await sdk.stateless_execution.ask_async(query="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->