from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_fields_response_dto import CustomFieldsResponseDTO
from ...models.get_custom_fields_by_object_key_version import GetCustomFieldsByObjectKeyVersion
from ...types import UNSET, Response


def _get_kwargs(
    object_key: str,
    *,
    location_id: str,
    version: GetCustomFieldsByObjectKeyVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    params: dict[str, Any] = {}

    params["locationId"] = location_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/custom-fields/object-key/{object_key}".format(
            object_key=quote(str(object_key), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldsResponseDTO | None:
    if response.status_code == 200:
        response_200 = CustomFieldsResponseDTO.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldsResponseDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_key: str,
    *,
    client: AuthenticatedClient,
    location_id: str,
    version: GetCustomFieldsByObjectKeyVersion,
) -> Response[CustomFieldsResponseDTO]:
    r"""Get Custom Fields By Object Key

     <div>
                      <p> Get Custom Fields By Object Key</p>
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
        object_key (str):
        location_id (str):
        version (GetCustomFieldsByObjectKeyVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsResponseDTO]
    """

    kwargs = _get_kwargs(
        object_key=object_key,
        location_id=location_id,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_key: str,
    *,
    client: AuthenticatedClient,
    location_id: str,
    version: GetCustomFieldsByObjectKeyVersion,
) -> CustomFieldsResponseDTO | None:
    r"""Get Custom Fields By Object Key

     <div>
                      <p> Get Custom Fields By Object Key</p>
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
        object_key (str):
        location_id (str):
        version (GetCustomFieldsByObjectKeyVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsResponseDTO
    """

    return sync_detailed(
        object_key=object_key,
        client=client,
        location_id=location_id,
        version=version,
    ).parsed


async def asyncio_detailed(
    object_key: str,
    *,
    client: AuthenticatedClient,
    location_id: str,
    version: GetCustomFieldsByObjectKeyVersion,
) -> Response[CustomFieldsResponseDTO]:
    r"""Get Custom Fields By Object Key

     <div>
                      <p> Get Custom Fields By Object Key</p>
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
        object_key (str):
        location_id (str):
        version (GetCustomFieldsByObjectKeyVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldsResponseDTO]
    """

    kwargs = _get_kwargs(
        object_key=object_key,
        location_id=location_id,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_key: str,
    *,
    client: AuthenticatedClient,
    location_id: str,
    version: GetCustomFieldsByObjectKeyVersion,
) -> CustomFieldsResponseDTO | None:
    r"""Get Custom Fields By Object Key

     <div>
                      <p> Get Custom Fields By Object Key</p>
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
        object_key (str):
        location_id (str):
        version (GetCustomFieldsByObjectKeyVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldsResponseDTO
    """

    return (
        await asyncio_detailed(
            object_key=object_key,
            client=client,
            location_id=location_id,
            version=version,
        )
    ).parsed
