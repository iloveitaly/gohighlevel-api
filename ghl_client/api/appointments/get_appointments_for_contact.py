from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_appointments_for_contact_version import GetAppointmentsForContactVersion
from ...models.get_events_successful_response_dto import GetEventsSuccessfulResponseDto
from ...types import Response


def _get_kwargs(
    contact_id: str,
    *,
    version: GetAppointmentsForContactVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts/{contact_id}/appointments".format(
            contact_id=quote(str(contact_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetEventsSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = GetEventsSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetEventsSuccessfulResponseDto]:
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
    version: GetAppointmentsForContactVersion,
) -> Response[GetEventsSuccessfulResponseDto]:
    """Get Appointments for Contact

     Get Appointments for Contact

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (GetAppointmentsForContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventsSuccessfulResponseDto]
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
    version: GetAppointmentsForContactVersion,
) -> GetEventsSuccessfulResponseDto | None:
    """Get Appointments for Contact

     Get Appointments for Contact

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (GetAppointmentsForContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventsSuccessfulResponseDto
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
    version: GetAppointmentsForContactVersion,
) -> Response[GetEventsSuccessfulResponseDto]:
    """Get Appointments for Contact

     Get Appointments for Contact

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (GetAppointmentsForContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventsSuccessfulResponseDto]
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
    version: GetAppointmentsForContactVersion,
) -> GetEventsSuccessfulResponseDto | None:
    """Get Appointments for Contact

     Get Appointments for Contact

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (GetAppointmentsForContactVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventsSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            version=version,
        )
    ).parsed
