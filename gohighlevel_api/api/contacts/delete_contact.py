from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_contact_version import DeleteContactVersion
from ...models.delete_contacts_successful_response_dto import DeleteContactsSuccessfulResponseDto
from ...types import Response


def _get_kwargs(
    contact_id: str,
    *,
    version: DeleteContactVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/contacts/{contact_id}".format(
            contact_id=quote(str(contact_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteContactsSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = DeleteContactsSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteContactsSuccessfulResponseDto]:
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
    version: DeleteContactVersion,
) -> Response[DeleteContactsSuccessfulResponseDto]:
    """Delete Contact

     Delete Contact

    Args:
        contact_id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (DeleteContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteContactsSuccessfulResponseDto]
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
    version: DeleteContactVersion,
) -> DeleteContactsSuccessfulResponseDto | None:
    """Delete Contact

     Delete Contact

    Args:
        contact_id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (DeleteContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteContactsSuccessfulResponseDto
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
    version: DeleteContactVersion,
) -> Response[DeleteContactsSuccessfulResponseDto]:
    """Delete Contact

     Delete Contact

    Args:
        contact_id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (DeleteContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteContactsSuccessfulResponseDto]
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
    version: DeleteContactVersion,
) -> DeleteContactsSuccessfulResponseDto | None:
    """Delete Contact

     Delete Contact

    Args:
        contact_id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (DeleteContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteContactsSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            version=version,
        )
    ).parsed
