from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_remove_contact_from_business_version import AddRemoveContactFromBusinessVersion
from ...models.contacts_bulk_upate_response import ContactsBulkUpateResponse
from ...models.contacts_business_update import ContactsBusinessUpdate
from ...types import Response


def _get_kwargs(
    *,
    body: ContactsBusinessUpdate,
    version: AddRemoveContactFromBusinessVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contacts/bulk/business",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactsBulkUpateResponse | None:
    if response.status_code == 200:
        response_200 = ContactsBulkUpateResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContactsBulkUpateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ContactsBusinessUpdate,
    version: AddRemoveContactFromBusinessVersion,
) -> Response[ContactsBulkUpateResponse]:
    """Add/Remove Contacts From Business

     Add/Remove Contacts From Business . Passing a `null` businessId will remove the businessId from the
    contacts

    Args:
        version (AddRemoveContactFromBusinessVersion):
        body (ContactsBusinessUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsBulkUpateResponse]
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
    client: AuthenticatedClient | Client,
    body: ContactsBusinessUpdate,
    version: AddRemoveContactFromBusinessVersion,
) -> ContactsBulkUpateResponse | None:
    """Add/Remove Contacts From Business

     Add/Remove Contacts From Business . Passing a `null` businessId will remove the businessId from the
    contacts

    Args:
        version (AddRemoveContactFromBusinessVersion):
        body (ContactsBusinessUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsBulkUpateResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ContactsBusinessUpdate,
    version: AddRemoveContactFromBusinessVersion,
) -> Response[ContactsBulkUpateResponse]:
    """Add/Remove Contacts From Business

     Add/Remove Contacts From Business . Passing a `null` businessId will remove the businessId from the
    contacts

    Args:
        version (AddRemoveContactFromBusinessVersion):
        body (ContactsBusinessUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsBulkUpateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ContactsBusinessUpdate,
    version: AddRemoveContactFromBusinessVersion,
) -> ContactsBulkUpateResponse | None:
    """Add/Remove Contacts From Business

     Add/Remove Contacts From Business . Passing a `null` businessId will remove the businessId from the
    contacts

    Args:
        version (AddRemoveContactFromBusinessVersion):
        body (ContactsBusinessUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsBulkUpateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            version=version,
        )
    ).parsed
