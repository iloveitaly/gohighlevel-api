from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contacts_search_successful_response_dto import ContactsSearchSuccessfulResponseDto
from ...models.get_contacts_version import GetContactsVersion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    location_id: str,
    start_after_id: str | Unset = UNSET,
    start_after: float | Unset = UNSET,
    query: str | Unset = UNSET,
    limit: float | Unset = 20.0,
    version: GetContactsVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    params: dict[str, Any] = {}

    params["locationId"] = location_id

    params["startAfterId"] = start_after_id

    params["startAfter"] = start_after

    params["query"] = query

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts/",
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
    *,
    client: AuthenticatedClient,
    location_id: str,
    start_after_id: str | Unset = UNSET,
    start_after: float | Unset = UNSET,
    query: str | Unset = UNSET,
    limit: float | Unset = 20.0,
    version: GetContactsVersion,
) -> Response[ContactsSearchSuccessfulResponseDto]:
    """Get Contacts

     Get Contacts

     **Note:** This API endpoint is deprecated. Please use the [Search
    Contacts](https://highlevel.stoplight.io/docs/integrations/dbe4f3a00a106-search-contacts) endpoint
    instead.

    Args:
        location_id (str):  Example: ve9EPM428h8vShlRW1KT.
        start_after_id (str | Unset):  Example: UIaE1WjAwWKdlyD7osQI.
        start_after (float | Unset):  Example: 1603870249758.
        query (str | Unset):  Example: John.
        limit (float | Unset):  Default: 20.0. Example: 20.
        version (GetContactsVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsSearchSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        start_after_id=start_after_id,
        start_after=start_after,
        query=query,
        limit=limit,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    location_id: str,
    start_after_id: str | Unset = UNSET,
    start_after: float | Unset = UNSET,
    query: str | Unset = UNSET,
    limit: float | Unset = 20.0,
    version: GetContactsVersion,
) -> ContactsSearchSuccessfulResponseDto | None:
    """Get Contacts

     Get Contacts

     **Note:** This API endpoint is deprecated. Please use the [Search
    Contacts](https://highlevel.stoplight.io/docs/integrations/dbe4f3a00a106-search-contacts) endpoint
    instead.

    Args:
        location_id (str):  Example: ve9EPM428h8vShlRW1KT.
        start_after_id (str | Unset):  Example: UIaE1WjAwWKdlyD7osQI.
        start_after (float | Unset):  Example: 1603870249758.
        query (str | Unset):  Example: John.
        limit (float | Unset):  Default: 20.0. Example: 20.
        version (GetContactsVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsSearchSuccessfulResponseDto
    """

    return sync_detailed(
        client=client,
        location_id=location_id,
        start_after_id=start_after_id,
        start_after=start_after,
        query=query,
        limit=limit,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    location_id: str,
    start_after_id: str | Unset = UNSET,
    start_after: float | Unset = UNSET,
    query: str | Unset = UNSET,
    limit: float | Unset = 20.0,
    version: GetContactsVersion,
) -> Response[ContactsSearchSuccessfulResponseDto]:
    """Get Contacts

     Get Contacts

     **Note:** This API endpoint is deprecated. Please use the [Search
    Contacts](https://highlevel.stoplight.io/docs/integrations/dbe4f3a00a106-search-contacts) endpoint
    instead.

    Args:
        location_id (str):  Example: ve9EPM428h8vShlRW1KT.
        start_after_id (str | Unset):  Example: UIaE1WjAwWKdlyD7osQI.
        start_after (float | Unset):  Example: 1603870249758.
        query (str | Unset):  Example: John.
        limit (float | Unset):  Default: 20.0. Example: 20.
        version (GetContactsVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsSearchSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        start_after_id=start_after_id,
        start_after=start_after,
        query=query,
        limit=limit,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    location_id: str,
    start_after_id: str | Unset = UNSET,
    start_after: float | Unset = UNSET,
    query: str | Unset = UNSET,
    limit: float | Unset = 20.0,
    version: GetContactsVersion,
) -> ContactsSearchSuccessfulResponseDto | None:
    """Get Contacts

     Get Contacts

     **Note:** This API endpoint is deprecated. Please use the [Search
    Contacts](https://highlevel.stoplight.io/docs/integrations/dbe4f3a00a106-search-contacts) endpoint
    instead.

    Args:
        location_id (str):  Example: ve9EPM428h8vShlRW1KT.
        start_after_id (str | Unset):  Example: UIaE1WjAwWKdlyD7osQI.
        start_after (float | Unset):  Example: 1603870249758.
        query (str | Unset):  Example: John.
        limit (float | Unset):  Default: 20.0. Example: 20.
        version (GetContactsVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsSearchSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            location_id=location_id,
            start_after_id=start_after_id,
            start_after=start_after,
            query=query,
            limit=limit,
            version=version,
        )
    ).parsed
