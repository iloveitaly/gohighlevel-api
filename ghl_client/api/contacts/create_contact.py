from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_contact_dto import CreateContactDto
from ...models.create_contact_version import CreateContactVersion
from ...models.create_contacts_successful_response_dto import CreateContactsSuccessfulResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: CreateContactDto,
    version: CreateContactVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contacts/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateContactsSuccessfulResponseDto | None:
    if response.status_code == 201:
        response_201 = CreateContactsSuccessfulResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateContactsSuccessfulResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateContactDto,
    version: CreateContactVersion,
) -> Response[CreateContactsSuccessfulResponseDto]:
    r"""Create Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a>

    Args:
        version (CreateContactVersion):
        body (CreateContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateContactsSuccessfulResponseDto]
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
    body: CreateContactDto,
    version: CreateContactVersion,
) -> CreateContactsSuccessfulResponseDto | None:
    r"""Create Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a>

    Args:
        version (CreateContactVersion):
        body (CreateContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateContactsSuccessfulResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateContactDto,
    version: CreateContactVersion,
) -> Response[CreateContactsSuccessfulResponseDto]:
    r"""Create Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a>

    Args:
        version (CreateContactVersion):
        body (CreateContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateContactsSuccessfulResponseDto]
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
    body: CreateContactDto,
    version: CreateContactVersion,
) -> CreateContactsSuccessfulResponseDto | None:
    r"""Create Contact

     Please find the list of acceptable values for the `country` field  <a
    href=\"https://highlevel.stoplight.io/docs/integrations/ZG9jOjI4MzUzNDIy-country-list\"
    target=\"_blank\">here</a>

    Args:
        version (CreateContactVersion):
        body (CreateContactDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateContactsSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            version=version,
        )
    ).parsed
