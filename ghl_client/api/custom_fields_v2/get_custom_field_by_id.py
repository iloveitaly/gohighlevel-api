from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_successful_response_dto import CustomFieldSuccessfulResponseDto
from ...models.get_custom_field_by_id_version import GetCustomFieldByIdVersion
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    version: GetCustomFieldByIdVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/custom-fields/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldSuccessfulResponseDto | None:
    if response.status_code == 200:
        response_200 = CustomFieldSuccessfulResponseDto.from_dict(response.json())

        return response_200

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
    id: str,
    *,
    client: AuthenticatedClient,
    version: GetCustomFieldByIdVersion,
) -> Response[CustomFieldSuccessfulResponseDto]:
    r"""Get Custom Field / Folder By Id

     <div>
                      <p> Get Custom Field / Folder By Id.</p>
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
        id (str):
        version (GetCustomFieldByIdVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    version: GetCustomFieldByIdVersion,
) -> CustomFieldSuccessfulResponseDto | None:
    r"""Get Custom Field / Folder By Id

     <div>
                      <p> Get Custom Field / Folder By Id.</p>
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
        id (str):
        version (GetCustomFieldByIdVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldSuccessfulResponseDto
    """

    return sync_detailed(
        id=id,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    version: GetCustomFieldByIdVersion,
) -> Response[CustomFieldSuccessfulResponseDto]:
    r"""Get Custom Field / Folder By Id

     <div>
                      <p> Get Custom Field / Folder By Id.</p>
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
        id (str):
        version (GetCustomFieldByIdVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldSuccessfulResponseDto]
    """

    kwargs = _get_kwargs(
        id=id,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    version: GetCustomFieldByIdVersion,
) -> CustomFieldSuccessfulResponseDto | None:
    r"""Get Custom Field / Folder By Id

     <div>
                      <p> Get Custom Field / Folder By Id.</p>
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
        id (str):
        version (GetCustomFieldByIdVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldSuccessfulResponseDto
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            version=version,
        )
    ).parsed
