from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_body_v2dto import SearchBodyV2DTO
from ...models.search_contacts_advanced_version import SearchContactsAdvancedVersion
from ...types import Response


def _get_kwargs(
    *,
    body: SearchBodyV2DTO,
    version: SearchContactsAdvancedVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contacts/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchBodyV2DTO,
    version: SearchContactsAdvancedVersion,
) -> Response[Any]:
    """Search Contacts

     Search contacts based on combinations of advanced filters. Documentation Link -
    https://doc.clickup.com/8631005/d/h/87cpx-158396/6e629989abe7fad

    Args:
        version (SearchContactsAdvancedVersion):
        body (SearchBodyV2DTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchBodyV2DTO,
    version: SearchContactsAdvancedVersion,
) -> Response[Any]:
    """Search Contacts

     Search contacts based on combinations of advanced filters. Documentation Link -
    https://doc.clickup.com/8631005/d/h/87cpx-158396/6e629989abe7fad

    Args:
        version (SearchContactsAdvancedVersion):
        body (SearchBodyV2DTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
