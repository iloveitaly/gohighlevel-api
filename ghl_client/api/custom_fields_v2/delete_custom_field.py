from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_folder_delete_response_dto import CustomFolderDeleteResponseDto
from ...models.delete_custom_field_version import DeleteCustomFieldVersion
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    version: DeleteCustomFieldVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/custom-fields/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFolderDeleteResponseDto | None:
    if response.status_code == 200:
        response_200 = CustomFolderDeleteResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFolderDeleteResponseDto]:
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
    version: DeleteCustomFieldVersion,
) -> Response[CustomFolderDeleteResponseDto]:
    r"""Delete Custom Field By Id

     <div>
        <p> Delete Custom Field By Id </p>
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
              Only supports Custom Objects and Company (Business) today. Will be extended to other
    Standard Objects in the future.
              </strong>
            </span>
        </div>
      </div>

    Args:
        id (str):
        version (DeleteCustomFieldVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFolderDeleteResponseDto]
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
    version: DeleteCustomFieldVersion,
) -> CustomFolderDeleteResponseDto | None:
    r"""Delete Custom Field By Id

     <div>
        <p> Delete Custom Field By Id </p>
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
              Only supports Custom Objects and Company (Business) today. Will be extended to other
    Standard Objects in the future.
              </strong>
            </span>
        </div>
      </div>

    Args:
        id (str):
        version (DeleteCustomFieldVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFolderDeleteResponseDto
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
    version: DeleteCustomFieldVersion,
) -> Response[CustomFolderDeleteResponseDto]:
    r"""Delete Custom Field By Id

     <div>
        <p> Delete Custom Field By Id </p>
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
              Only supports Custom Objects and Company (Business) today. Will be extended to other
    Standard Objects in the future.
              </strong>
            </span>
        </div>
      </div>

    Args:
        id (str):
        version (DeleteCustomFieldVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFolderDeleteResponseDto]
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
    version: DeleteCustomFieldVersion,
) -> CustomFolderDeleteResponseDto | None:
    r"""Delete Custom Field By Id

     <div>
        <p> Delete Custom Field By Id </p>
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
              Only supports Custom Objects and Company (Business) today. Will be extended to other
    Standard Objects in the future.
              </strong>
            </span>
        </div>
      </div>

    Args:
        id (str):
        version (DeleteCustomFieldVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFolderDeleteResponseDto
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            version=version,
        )
    ).parsed
