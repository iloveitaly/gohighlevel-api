from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_association_type import CreateAssociationType
from ...models.create_association_version import CreateAssociationVersion
from ...models.update_tags_dto import UpdateTagsDTO
from ...models.update_tags_response_dto import UpdateTagsResponseDTO
from ...types import Response


def _get_kwargs(
    type_: CreateAssociationType,
    *,
    body: UpdateTagsDTO,
    version: CreateAssociationVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contacts/bulk/tags/update/{type_}".format(
            type_=quote(str(type_), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateTagsResponseDTO | None:
    if response.status_code == 201:
        response_201 = UpdateTagsResponseDTO.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateTagsResponseDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: CreateAssociationType,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTagsDTO,
    version: CreateAssociationVersion,
) -> Response[UpdateTagsResponseDTO]:
    """Update Contacts Tags

     Allows you to update tags to multiple contacts at once, you can add or remove tags from the contacts

    Args:
        type_ (CreateAssociationType):
        version (CreateAssociationVersion):
        body (UpdateTagsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTagsResponseDTO]
    """

    kwargs = _get_kwargs(
        type_=type_,
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: CreateAssociationType,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTagsDTO,
    version: CreateAssociationVersion,
) -> UpdateTagsResponseDTO | None:
    """Update Contacts Tags

     Allows you to update tags to multiple contacts at once, you can add or remove tags from the contacts

    Args:
        type_ (CreateAssociationType):
        version (CreateAssociationVersion):
        body (UpdateTagsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTagsResponseDTO
    """

    return sync_detailed(
        type_=type_,
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    type_: CreateAssociationType,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTagsDTO,
    version: CreateAssociationVersion,
) -> Response[UpdateTagsResponseDTO]:
    """Update Contacts Tags

     Allows you to update tags to multiple contacts at once, you can add or remove tags from the contacts

    Args:
        type_ (CreateAssociationType):
        version (CreateAssociationVersion):
        body (UpdateTagsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTagsResponseDTO]
    """

    kwargs = _get_kwargs(
        type_=type_,
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: CreateAssociationType,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTagsDTO,
    version: CreateAssociationVersion,
) -> UpdateTagsResponseDTO | None:
    """Update Contacts Tags

     Allows you to update tags to multiple contacts at once, you can add or remove tags from the contacts

    Args:
        type_ (CreateAssociationType):
        version (CreateAssociationVersion):
        body (UpdateTagsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTagsResponseDTO
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
