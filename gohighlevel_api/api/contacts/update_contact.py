from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_contact_dto import UpdateContactDto
from ...models.update_contact_version import UpdateContactVersion
from ...models.update_contacts_successful_response_dto import UpdateContactsSuccessfulResponseDto
from ...types import Response


def _get_kwargs(
    contact_id: str,
    *,
    body: UpdateContactDto,
    version: UpdateContactVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/contacts/{contact_id}".format(
            contact_id=quote(str(contact_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateContactsSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = UpdateContactsSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateContactsSuccessfulResponseDto]:
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
    body: UpdateContactDto,
    version: UpdateContactVersion,
) -> Response[UpdateContactsSuccessfulResponseDto]:
    r"""Update Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a>

    Args:
        contact_id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (UpdateContactVersion):
        body (UpdateContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateContactsSuccessfulResponseDto]
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
    body: UpdateContactDto,
    version: UpdateContactVersion,
) -> UpdateContactsSuccessfulResponseDto | None:
    r"""Update Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a>

    Args:
        contact_id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (UpdateContactVersion):
        body (UpdateContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateContactsSuccessfulResponseDto
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
    body: UpdateContactDto,
    version: UpdateContactVersion,
) -> Response[UpdateContactsSuccessfulResponseDto]:
    r"""Update Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a>

    Args:
        contact_id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (UpdateContactVersion):
        body (UpdateContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateContactsSuccessfulResponseDto]
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
    body: UpdateContactDto,
    version: UpdateContactVersion,
) -> UpdateContactsSuccessfulResponseDto | None:
    r"""Update Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a>

    Args:
        contact_id (str):  Example: ocQHyuzHvysMo5N5VsXc.
        version (UpdateContactVersion):
        body (UpdateContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateContactsSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
