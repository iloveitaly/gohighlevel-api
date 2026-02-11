from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_create_update_note_successful_response_dto import GetCreateUpdateNoteSuccessfulResponseDto
from ...models.notes_dto import NotesDTO
from ...models.update_note_version import UpdateNoteVersion
from ...types import Response


def _get_kwargs(
    contact_id: str,
    id: str,
    *,
    body: NotesDTO,
    version: UpdateNoteVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/contacts/{contact_id}/notes/{id}".format(
            contact_id=quote(str(contact_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCreateUpdateNoteSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = GetCreateUpdateNoteSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCreateUpdateNoteSuccessfulResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: NotesDTO,
    version: UpdateNoteVersion,
) -> Response[GetCreateUpdateNoteSuccessfulResponseDto]:
    """Update Note

     Update Note

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (UpdateNoteVersion):
        body (NotesDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreateUpdateNoteSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        id=id,
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contact_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: NotesDTO,
    version: UpdateNoteVersion,
) -> GetCreateUpdateNoteSuccessfulResponseDto | None:
    """Update Note

     Update Note

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (UpdateNoteVersion):
        body (NotesDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreateUpdateNoteSuccessfulResponseDto
    """

    return sync_detailed(
        contact_id=contact_id,
        id=id,
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    contact_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: NotesDTO,
    version: UpdateNoteVersion,
) -> Response[GetCreateUpdateNoteSuccessfulResponseDto]:
    """Update Note

     Update Note

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (UpdateNoteVersion):
        body (NotesDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreateUpdateNoteSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        id=id,
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: NotesDTO,
    version: UpdateNoteVersion,
) -> GetCreateUpdateNoteSuccessfulResponseDto | None:
    """Update Note

     Update Note

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (UpdateNoteVersion):
        body (NotesDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreateUpdateNoteSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            id=id,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
