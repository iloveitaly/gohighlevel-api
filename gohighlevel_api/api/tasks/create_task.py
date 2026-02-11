from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_task_params import CreateTaskParams
from ...models.create_task_version import CreateTaskVersion
from ...models.task_by_is_successful_response_dto import TaskByIsSuccessfulResponseDto
from ...types import Response


def _get_kwargs(
    contact_id: str,
    *,
    body: CreateTaskParams,
    version: CreateTaskVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contacts/{contact_id}/tasks".format(
            contact_id=quote(str(contact_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TaskByIsSuccessfulResponseDto | None:
    if response.status_code == 201:
        response_201 = TaskByIsSuccessfulResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TaskByIsSuccessfulResponseDto]:
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
    body: CreateTaskParams,
    version: CreateTaskVersion,
) -> Response[TaskByIsSuccessfulResponseDto]:
    """Create Task

     Create Task

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (CreateTaskVersion):
        body (CreateTaskParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TaskByIsSuccessfulResponseDto]
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
    body: CreateTaskParams,
    version: CreateTaskVersion,
) -> TaskByIsSuccessfulResponseDto | None:
    """Create Task

     Create Task

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (CreateTaskVersion):
        body (CreateTaskParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TaskByIsSuccessfulResponseDto
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
    body: CreateTaskParams,
    version: CreateTaskVersion,
) -> Response[TaskByIsSuccessfulResponseDto]:
    """Create Task

     Create Task

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (CreateTaskVersion):
        body (CreateTaskParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TaskByIsSuccessfulResponseDto]
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
    body: CreateTaskParams,
    version: CreateTaskVersion,
) -> TaskByIsSuccessfulResponseDto | None:
    """Create Task

     Create Task

    Args:
        contact_id (str):  Example: sx6wyHhbFdRXh302LLNR.
        version (CreateTaskVersion):
        body (CreateTaskParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TaskByIsSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
