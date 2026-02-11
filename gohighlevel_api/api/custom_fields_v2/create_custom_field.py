from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_custom_field_version import CreateCustomFieldVersion
from ...models.create_custom_fields_dto import CreateCustomFieldsDTO
from ...models.custom_field_successful_response_dto import CustomFieldSuccessfulResponseDto
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCustomFieldsDTO,
    version: CreateCustomFieldVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/custom-fields/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldSuccessfulResponseDto | None:
    if response.status_code == 201:
        response_201 = CustomFieldSuccessfulResponseDto.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldSuccessfulResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCustomFieldsDTO,
    version: CreateCustomFieldVersion,
) -> Response[CustomFieldSuccessfulResponseDto]:
    r"""Create Custom Field

     <div>
                      <p> Create Custom Field </p>
                      <div>
                        <span style= \"display: inline-block;
                                    width: 25px; height: 25px;
                                    background-color: yellow;
                                    color: black;
                                    font-weight: bold;
                                    font-size: 24px;
                                    text-align: center;
                                    line-height: 22px;
                                    border: 2px solid black;
                                    border-radius: 10%;
                                    margin-right: 10px;\">
                                    !
                          </span>
                          <span>
                            <strong>
                            Only supports Custom Objects and Company (Business) today. Will be extended
    to other Standard Objects in the future.
                            </strong>
                          </span>
                      </div>
                    </div>

    Args:
        version (CreateCustomFieldVersion):
        body (CreateCustomFieldsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldSuccessfulResponseDto]
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
    body: CreateCustomFieldsDTO,
    version: CreateCustomFieldVersion,
) -> CustomFieldSuccessfulResponseDto | None:
    r"""Create Custom Field

     <div>
                      <p> Create Custom Field </p>
                      <div>
                        <span style= \"display: inline-block;
                                    width: 25px; height: 25px;
                                    background-color: yellow;
                                    color: black;
                                    font-weight: bold;
                                    font-size: 24px;
                                    text-align: center;
                                    line-height: 22px;
                                    border: 2px solid black;
                                    border-radius: 10%;
                                    margin-right: 10px;\">
                                    !
                          </span>
                          <span>
                            <strong>
                            Only supports Custom Objects and Company (Business) today. Will be extended
    to other Standard Objects in the future.
                            </strong>
                          </span>
                      </div>
                    </div>

    Args:
        version (CreateCustomFieldVersion):
        body (CreateCustomFieldsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldSuccessfulResponseDto
    """

    return sync_detailed(
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCustomFieldsDTO,
    version: CreateCustomFieldVersion,
) -> Response[CustomFieldSuccessfulResponseDto]:
    r"""Create Custom Field

     <div>
                      <p> Create Custom Field </p>
                      <div>
                        <span style= \"display: inline-block;
                                    width: 25px; height: 25px;
                                    background-color: yellow;
                                    color: black;
                                    font-weight: bold;
                                    font-size: 24px;
                                    text-align: center;
                                    line-height: 22px;
                                    border: 2px solid black;
                                    border-radius: 10%;
                                    margin-right: 10px;\">
                                    !
                          </span>
                          <span>
                            <strong>
                            Only supports Custom Objects and Company (Business) today. Will be extended
    to other Standard Objects in the future.
                            </strong>
                          </span>
                      </div>
                    </div>

    Args:
        version (CreateCustomFieldVersion):
        body (CreateCustomFieldsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldSuccessfulResponseDto]
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
    body: CreateCustomFieldsDTO,
    version: CreateCustomFieldVersion,
) -> CustomFieldSuccessfulResponseDto | None:
    r"""Create Custom Field

     <div>
                      <p> Create Custom Field </p>
                      <div>
                        <span style= \"display: inline-block;
                                    width: 25px; height: 25px;
                                    background-color: yellow;
                                    color: black;
                                    font-weight: bold;
                                    font-size: 24px;
                                    text-align: center;
                                    line-height: 22px;
                                    border: 2px solid black;
                                    border-radius: 10%;
                                    margin-right: 10px;\">
                                    !
                          </span>
                          <span>
                            <strong>
                            Only supports Custom Objects and Company (Business) today. Will be extended
    to other Standard Objects in the future.
                            </strong>
                          </span>
                      </div>
                    </div>

    Args:
        version (CreateCustomFieldVersion):
        body (CreateCustomFieldsDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            version=version,
        )
    ).parsed
