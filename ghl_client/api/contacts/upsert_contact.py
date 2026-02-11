from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upsert_contact_dto import UpsertContactDto
from ...models.upsert_contact_version import UpsertContactVersion
from ...models.upsert_contacts_successful_response_dto import UpsertContactsSuccessfulResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: UpsertContactDto,
    version: UpsertContactVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contacts/upsert",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpsertContactsSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = UpsertContactsSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpsertContactsSuccessfulResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpsertContactDto,
    version: UpsertContactVersion,
) -> Response[UpsertContactsSuccessfulResponseDto]:
    r"""Upsert Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a><br/><br/>The Upsert API will adhere to the configuration defined under
    the “Allow Duplicate Contact” setting at the Location level. If the setting is configured to check
    both Email and Phone, the API will attempt to identify an existing contact based on the priority
    sequence specified in the setting, and will create or update the contact accordingly.<br/><br/>If
    two separate contacts already exist—one with the same email and another with the same phone—and an
    upsert request includes both the email and phone, the API will update the contact that matches the
    first field in the configured sequence, and ignore the second field to prevent duplication.

    Args:
        version (UpsertContactVersion):
        body (UpsertContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpsertContactsSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UpsertContactDto,
    version: UpsertContactVersion,
) -> UpsertContactsSuccessfulResponseDto | None:
    r"""Upsert Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a><br/><br/>The Upsert API will adhere to the configuration defined under
    the “Allow Duplicate Contact” setting at the Location level. If the setting is configured to check
    both Email and Phone, the API will attempt to identify an existing contact based on the priority
    sequence specified in the setting, and will create or update the contact accordingly.<br/><br/>If
    two separate contacts already exist—one with the same email and another with the same phone—and an
    upsert request includes both the email and phone, the API will update the contact that matches the
    first field in the configured sequence, and ignore the second field to prevent duplication.

    Args:
        version (UpsertContactVersion):
        body (UpsertContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpsertContactsSuccessfulResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpsertContactDto,
    version: UpsertContactVersion,
) -> Response[UpsertContactsSuccessfulResponseDto]:
    r"""Upsert Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a><br/><br/>The Upsert API will adhere to the configuration defined under
    the “Allow Duplicate Contact” setting at the Location level. If the setting is configured to check
    both Email and Phone, the API will attempt to identify an existing contact based on the priority
    sequence specified in the setting, and will create or update the contact accordingly.<br/><br/>If
    two separate contacts already exist—one with the same email and another with the same phone—and an
    upsert request includes both the email and phone, the API will update the contact that matches the
    first field in the configured sequence, and ignore the second field to prevent duplication.

    Args:
        version (UpsertContactVersion):
        body (UpsertContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpsertContactsSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpsertContactDto,
    version: UpsertContactVersion,
) -> UpsertContactsSuccessfulResponseDto | None:
    r"""Upsert Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a><br/><br/>The Upsert API will adhere to the configuration defined under
    the “Allow Duplicate Contact” setting at the Location level. If the setting is configured to check
    both Email and Phone, the API will attempt to identify an existing contact based on the priority
    sequence specified in the setting, and will create or update the contact accordingly.<br/><br/>If
    two separate contacts already exist—one with the same email and another with the same phone—and an
    upsert request includes both the email and phone, the API will update the contact that matches the
    first field in the configured sequence, and ignore the second field to prevent duplication.

    Args:
        version (UpsertContactVersion):
        body (UpsertContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpsertContactsSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            version=version,
        )
    ).parsed
