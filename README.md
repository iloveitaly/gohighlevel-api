# GoHighLevel API Client

Connect to the GoHighLevel API with a modern, type-safe Python client. This is auto generated based on a API spec which I believe I had an LLM generate. There are probably some bugs, but it's working for me.

Right now, this client focuses on the Contacts and Custom Fields endpoints, giving you typed interfaces for the data you use most often.

## Installation
Add this package to your project using `uv`:

```bash
uv add gohighlevel-api
```

## Usage
I've designed the client to be intuitive. You just need your API token (or Location API Key) to get started.

```python
from gohighlevel_api import AuthenticatedClient
from gohighlevel_api.api.contacts import get_contacts
from gohighlevel_api.models import GetContactsVersion

# Initialize the client with your API key
client = AuthenticatedClient(
    base_url="https://services.leadconnectorhq.com",
    token="YOUR_ACCESS_TOKEN"
)

# Fetch contacts with type safety
with client as c:
    response = get_contacts.sync(client=c, location_id="YOUR_LOCATION_ID")
    
    if response:
        print(f"Found {len(response.contacts)} contacts")
        for contact in response.contacts:
            print(f"{contact.first_name} {contact.last_name}")
```

For async applications, it works just as smoothly:

```python
import asyncio
from gohighlevel_api import AuthenticatedClient
from gohighlevel_api.api.contacts import get_contacts

async def main():
    client = AuthenticatedClient(
        base_url="https://services.leadconnectorhq.com",
        token="YOUR_ACCESS_TOKEN"
    )

    async with client as c:
        response = await get_contacts.asyncio(client=c, location_id="YOUR_LOCATION_ID")
        # Work with your data...

if __name__ == "__main__":
    asyncio.run(main())
```

## Key Concepts

To use this client effectively, here are a few things to know about how the API is structured:

1.  **Module Structure**: Every API endpoint (path + method) becomes a Python module with four functions:
    *   `sync`: Blocking request that returns parsed data (if successful) or `None`.
    *   `sync_detailed`: Blocking request that returns a `Response` object (with status code, headers, etc.).
    *   `asyncio`: Async version of `sync`.
    *   `asyncio_detailed`: Async version of `sync_detailed`.
2.  **Arguments**: All path parameters, query parameters, and request bodies become arguments to these methods.
3.  **Tags**: If an endpoint has tags in the OpenAPI spec, the first tag is used as the module name (e.g., `api.contacts`). Endpoints without tags end up in `api.default`.

## Advanced Usage

### Detailed Responses
Sometimes you need more than just the parsed data—like headers or status codes.

```python
from gohighlevel_api.api.contacts import get_contacts
from gohighlevel_api.types import Response

with client as c:
    # returns a Response object containing status_code, content, headers, and parsed data
    response: Response = get_contacts.sync_detailed(client=c, location_id="YOUR_LOCATION_ID")
    
    if response.status_code == 200:
        print(response.parsed)
```

### SSL Configuration
By default, the client verifies SSL certificates. However, if you are testing against a local server or need a custom certificate bundle, you can configure this:

**Custom Certificate Bundle:**
```python
client = AuthenticatedClient(
    base_url="https://internal.api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

**Disable Verification (Security Risk):**
```python
client = AuthenticatedClient(
    base_url="https://internal.api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

### Customizing the HTTP Client
You have full control over the underlying `httpx` client. This is useful for adding event hooks, logging, or setting proxies.

**Using arguments:**
```python
from gohighlevel_api import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)
```

**Replacing the client entirely:**
You can also supply your own `httpx.Client`. Note that this overrides configuration passed to the constructor (like `base_url`).

```python
import httpx
from gohighlevel_api import Client

client = Client(
    base_url="https://api.example.com",
)

# Note that base_url needs to be re-set here
client.set_httpx_client(httpx.Client(
    base_url="https://api.example.com", 
    proxies="http://localhost:8030"
))
```

## Features
*   **Type-safe Models:** Every request and response is validated against generated Pydantic-style models.
*   **Sync and Async:** Native support for both blocking and `asyncio` workflows.
*   **Selective Schema:** focused coverage for Contacts and Custom Fields to keep the package lightweight.
*   **Auto-generated:** Built directly from GoHighLevel's OpenAPI specs, ensuring accuracy.
*   **Modern Tooling:** Built with `uv` for fast, reliable package management.

## [MIT License](LICENSE.md)
