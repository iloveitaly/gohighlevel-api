from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_duplicate_contact_version import GetDuplicateContactVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    location_id: str,
    number: str | Unset = UNSET,
    email: str | Unset = UNSET,
    version: GetDuplicateContactVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    params: dict[str, Any] = {}

    params["locationId"] = location_id

    params["number"] = number

    params["email"] = email

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts/search/duplicate",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
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
    location_id: str,
    number: str | Unset = UNSET,
    email: str | Unset = UNSET,
    version: GetDuplicateContactVersion,
) -> Response[Any]:
    """Get Duplicate Contact

     Get Duplicate Contact.<br/><br/>If `Allow Duplicate Contact` is disabled under Settings, the global
    unique identifier will be used for searching the contact. If the setting is enabled, first priority
    for search is `email` and the second priority will be `phone`.

    Args:
        location_id (str):  Example: sadadya1u12basyhasd.
        number (str | Unset):  Example: +1423164516.
        email (str | Unset):  Example: abc@abc.com.
        version (GetDuplicateContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        number=number,
        email=email,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    location_id: str,
    number: str | Unset = UNSET,
    email: str | Unset = UNSET,
    version: GetDuplicateContactVersion,
) -> Response[Any]:
    """Get Duplicate Contact

     Get Duplicate Contact.<br/><br/>If `Allow Duplicate Contact` is disabled under Settings, the global
    unique identifier will be used for searching the contact. If the setting is enabled, first priority
    for search is `email` and the second priority will be `phone`.

    Args:
        location_id (str):  Example: sadadya1u12basyhasd.
        number (str | Unset):  Example: +1423164516.
        email (str | Unset):  Example: abc@abc.com.
        version (GetDuplicateContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        number=number,
        email=email,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
