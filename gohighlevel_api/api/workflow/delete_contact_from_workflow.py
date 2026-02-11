from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contacts_workflow_successful_response_dto import ContactsWorkflowSuccessfulResponseDto
from ...models.create_workflow_dto import CreateWorkflowDto
from ...models.delete_contact_from_workflow_version import DeleteContactFromWorkflowVersion
from ...types import Response


def _get_kwargs(
    contact_id: str,
    workflow_id: str,
    *,
    body: CreateWorkflowDto,
    version: DeleteContactFromWorkflowVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/contacts/{contact_id}/workflow/{workflow_id}".format(
            contact_id=quote(str(contact_id), safe=""),
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactsWorkflowSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = ContactsWorkflowSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContactsWorkflowSuccessfulResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateWorkflowDto,
    version: DeleteContactFromWorkflowVersion,
) -> Response[ContactsWorkflowSuccessfulResponseDto]:
    """Delete Contact from Workflow

     Delete Contact from Workflow

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        workflow_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (DeleteContactFromWorkflowVersion):
        body (CreateWorkflowDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsWorkflowSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        workflow_id=workflow_id,
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contact_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateWorkflowDto,
    version: DeleteContactFromWorkflowVersion,
) -> ContactsWorkflowSuccessfulResponseDto | None:
    """Delete Contact from Workflow

     Delete Contact from Workflow

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        workflow_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (DeleteContactFromWorkflowVersion):
        body (CreateWorkflowDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsWorkflowSuccessfulResponseDto
    """

    return sync_detailed(
        contact_id=contact_id,
        workflow_id=workflow_id,
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    contact_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateWorkflowDto,
    version: DeleteContactFromWorkflowVersion,
) -> Response[ContactsWorkflowSuccessfulResponseDto]:
    """Delete Contact from Workflow

     Delete Contact from Workflow

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        workflow_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (DeleteContactFromWorkflowVersion):
        body (CreateWorkflowDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsWorkflowSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        workflow_id=workflow_id,
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateWorkflowDto,
    version: DeleteContactFromWorkflowVersion,
) -> ContactsWorkflowSuccessfulResponseDto | None:
    """Delete Contact from Workflow

     Delete Contact from Workflow

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        workflow_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (DeleteContactFromWorkflowVersion):
        body (CreateWorkflowDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsWorkflowSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            workflow_id=workflow_id,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
