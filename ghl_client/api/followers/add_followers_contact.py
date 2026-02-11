from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_followers_contact_version import AddFollowersContactVersion
from ...models.create_add_followers_successful_response_dto import CreateAddFollowersSuccessfulResponseDto
from ...models.followers_dto import FollowersDTO
from ...types import Response


def _get_kwargs(
    contact_id: str,
    *,
    body: FollowersDTO,
    version: AddFollowersContactVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contacts/{contact_id}/followers".format(
            contact_id=quote(str(contact_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateAddFollowersSuccessfulResponseDto | None:
    if response.status_code == 201:
        response_201 = CreateAddFollowersSuccessfulResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateAddFollowersSuccessfulResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_id: str,
    *,
    client: AuthenticatedClient,
    body: FollowersDTO,
    version: AddFollowersContactVersion,
) -> Response[CreateAddFollowersSuccessfulResponseDto]:
    """Add Followers

     Add Followers

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302Lunr.
        version (AddFollowersContactVersion):
        body (FollowersDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAddFollowersSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contact_id: str,
    *,
    client: AuthenticatedClient,
    body: FollowersDTO,
    version: AddFollowersContactVersion,
) -> CreateAddFollowersSuccessfulResponseDto | None:
    """Add Followers

     Add Followers

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302Lunr.
        version (AddFollowersContactVersion):
        body (FollowersDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAddFollowersSuccessfulResponseDto
    """

    return sync_detailed(
        contact_id=contact_id,
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    contact_id: str,
    *,
    client: AuthenticatedClient,
    body: FollowersDTO,
    version: AddFollowersContactVersion,
) -> Response[CreateAddFollowersSuccessfulResponseDto]:
    """Add Followers

     Add Followers

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302Lunr.
        version (AddFollowersContactVersion):
        body (FollowersDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAddFollowersSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: str,
    *,
    client: AuthenticatedClient,
    body: FollowersDTO,
    version: AddFollowersContactVersion,
) -> CreateAddFollowersSuccessfulResponseDto | None:
    """Add Followers

     Add Followers

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302Lunr.
        version (AddFollowersContactVersion):
        body (FollowersDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAddFollowersSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
