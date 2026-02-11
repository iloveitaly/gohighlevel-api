from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_delete_cantacts_campaigns_successful_response_dto import (
    CreateDeleteCantactsCampaignsSuccessfulResponseDto,
)
from ...models.remove_contact_from_campaign_version import RemoveContactFromCampaignVersion
from ...types import Response


def _get_kwargs(
    contact_id: str,
    campaign_id: str,
    *,
    version: RemoveContactFromCampaignVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/contacts/{contact_id}/campaigns/{campaign_id}".format(
            contact_id=quote(str(contact_id), safe=""),
            campaign_id=quote(str(campaign_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateDeleteCantactsCampaignsSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = CreateDeleteCantactsCampaignsSuccessfulResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateDeleteCantactsCampaignsSuccessfulResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_id: str,
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    version: RemoveContactFromCampaignVersion,
) -> Response[CreateDeleteCantactsCampaignsSuccessfulResponseDto]:
    """Remove Contact From Campaign

     Remove Contact From Campaign

    Args:
        contact_id (str):  Example: 3bZD1nQzbul0MCancbQD.
        campaign_id (str):  Example: Y2I9XM7aO1hncuSOlc9L.
        version (RemoveContactFromCampaignVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDeleteCantactsCampaignsSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        campaign_id=campaign_id,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contact_id: str,
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    version: RemoveContactFromCampaignVersion,
) -> CreateDeleteCantactsCampaignsSuccessfulResponseDto | None:
    """Remove Contact From Campaign

     Remove Contact From Campaign

    Args:
        contact_id (str):  Example: 3bZD1nQzbul0MCancbQD.
        campaign_id (str):  Example: Y2I9XM7aO1hncuSOlc9L.
        version (RemoveContactFromCampaignVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDeleteCantactsCampaignsSuccessfulResponseDto
    """

    return sync_detailed(
        contact_id=contact_id,
        campaign_id=campaign_id,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    contact_id: str,
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    version: RemoveContactFromCampaignVersion,
) -> Response[CreateDeleteCantactsCampaignsSuccessfulResponseDto]:
    """Remove Contact From Campaign

     Remove Contact From Campaign

    Args:
        contact_id (str):  Example: 3bZD1nQzbul0MCancbQD.
        campaign_id (str):  Example: Y2I9XM7aO1hncuSOlc9L.
        version (RemoveContactFromCampaignVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDeleteCantactsCampaignsSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        campaign_id=campaign_id,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: str,
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    version: RemoveContactFromCampaignVersion,
) -> CreateDeleteCantactsCampaignsSuccessfulResponseDto | None:
    """Remove Contact From Campaign

     Remove Contact From Campaign

    Args:
        contact_id (str):  Example: 3bZD1nQzbul0MCancbQD.
        campaign_id (str):  Example: Y2I9XM7aO1hncuSOlc9L.
        version (RemoveContactFromCampaignVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDeleteCantactsCampaignsSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            campaign_id=campaign_id,
            client=client,
            version=version,
        )
    ).parsed
