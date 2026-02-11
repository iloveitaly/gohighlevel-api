from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contacts_search_successful_response_dto import ContactsSearchSuccessfulResponseDto
from ...models.get_contacts_by_business_id_version import GetContactsByBusinessIdVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    business_id: str,
    *,
    limit: str | Unset = "25",
    location_id: str,
    skip: str | Unset = "0",
    query: str | Unset = UNSET,
    version: GetContactsByBusinessIdVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["locationId"] = location_id

    params["skip"] = skip

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts/business/{business_id}".format(
            business_id=quote(str(business_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactsSearchSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = ContactsSearchSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContactsSearchSuccessfulResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    *,
    client: AuthenticatedClient,
    limit: str | Unset = "25",
    location_id: str,
    skip: str | Unset = "0",
    query: str | Unset = UNSET,
    version: GetContactsByBusinessIdVersion,
) -> Response[ContactsSearchSuccessfulResponseDto]:
    """Get Contacts By BusinessId

     Get Contacts By BusinessId

    Args:
        business_id (str):
        limit (str | Unset):  Default: '25'. Example: 10.
        location_id (str):  Example: 5DP4iH6HLkQsiKESj6rh.
        skip (str | Unset):  Default: '0'. Example: 10.
        query (str | Unset):  Example: contact name.
        version (GetContactsByBusinessIdVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsSearchSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        limit=limit,
        location_id=location_id,
        skip=skip,
        query=query,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    *,
    client: AuthenticatedClient,
    limit: str | Unset = "25",
    location_id: str,
    skip: str | Unset = "0",
    query: str | Unset = UNSET,
    version: GetContactsByBusinessIdVersion,
) -> ContactsSearchSuccessfulResponseDto | None:
    """Get Contacts By BusinessId

     Get Contacts By BusinessId

    Args:
        business_id (str):
        limit (str | Unset):  Default: '25'. Example: 10.
        location_id (str):  Example: 5DP4iH6HLkQsiKESj6rh.
        skip (str | Unset):  Default: '0'. Example: 10.
        query (str | Unset):  Example: contact name.
        version (GetContactsByBusinessIdVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsSearchSuccessfulResponseDto
    """

    return sync_detailed(
        business_id=business_id,
        client=client,
        limit=limit,
        location_id=location_id,
        skip=skip,
        query=query,
        version=version,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    *,
    client: AuthenticatedClient,
    limit: str | Unset = "25",
    location_id: str,
    skip: str | Unset = "0",
    query: str | Unset = UNSET,
    version: GetContactsByBusinessIdVersion,
) -> Response[ContactsSearchSuccessfulResponseDto]:
    """Get Contacts By BusinessId

     Get Contacts By BusinessId

    Args:
        business_id (str):
        limit (str | Unset):  Default: '25'. Example: 10.
        location_id (str):  Example: 5DP4iH6HLkQsiKESj6rh.
        skip (str | Unset):  Default: '0'. Example: 10.
        query (str | Unset):  Example: contact name.
        version (GetContactsByBusinessIdVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsSearchSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        limit=limit,
        location_id=location_id,
        skip=skip,
        query=query,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    *,
    client: AuthenticatedClient,
    limit: str | Unset = "25",
    location_id: str,
    skip: str | Unset = "0",
    query: str | Unset = UNSET,
    version: GetContactsByBusinessIdVersion,
) -> ContactsSearchSuccessfulResponseDto | None:
    """Get Contacts By BusinessId

     Get Contacts By BusinessId

    Args:
        business_id (str):
        limit (str | Unset):  Default: '25'. Example: 10.
        location_id (str):  Example: 5DP4iH6HLkQsiKESj6rh.
        skip (str | Unset):  Default: '0'. Example: 10.
        query (str | Unset):  Example: contact name.
        version (GetContactsByBusinessIdVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsSearchSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            client=client,
            limit=limit,
            location_id=location_id,
            skip=skip,
            query=query,
            version=version,
        )
    ).parsed
