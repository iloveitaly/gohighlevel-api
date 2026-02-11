from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_notes_version import GetAllNotesVersion
from ...models.get_notes_list_successful_response_dto import GetNotesListSuccessfulResponseDto
from ...types import Response


def _get_kwargs(
    contact_id: str,
    *,
    version: GetAllNotesVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts/{contact_id}/notes".format(
            contact_id=quote(str(contact_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetNotesListSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = GetNotesListSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetNotesListSuccessfulResponseDto]:
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
    version: GetAllNotesVersion,
) -> Response[GetNotesListSuccessfulResponseDto]:
    """Get All Notes

     Get All Notes

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (GetAllNotesVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetNotesListSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
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
    version: GetAllNotesVersion,
) -> GetNotesListSuccessfulResponseDto | None:
    """Get All Notes

     Get All Notes

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (GetAllNotesVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetNotesListSuccessfulResponseDto
    """

    return sync_detailed(
        contact_id=contact_id,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    contact_id: str,
    *,
    client: AuthenticatedClient,
    version: GetAllNotesVersion,
) -> Response[GetNotesListSuccessfulResponseDto]:
    """Get All Notes

     Get All Notes

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (GetAllNotesVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetNotesListSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: str,
    *,
    client: AuthenticatedClient,
    version: GetAllNotesVersion,
) -> GetNotesListSuccessfulResponseDto | None:
    """Get All Notes

     Get All Notes

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (GetAllNotesVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetNotesListSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            version=version,
        )
    ).parsed
