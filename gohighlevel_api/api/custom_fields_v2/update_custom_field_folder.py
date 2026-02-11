from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.i_custom_field_folder import ICustomFieldFolder
from ...models.update_custom_field_folder_version import UpdateCustomFieldFolderVersion
from ...models.update_folder import UpdateFolder
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateFolder,
    version: UpdateCustomFieldFolderVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/custom-fields/folder/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ICustomFieldFolder | None:
    if response.status_code == 200:
        response_200 = ICustomFieldFolder.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ICustomFieldFolder]:
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
    body: UpdateFolder,
    version: UpdateCustomFieldFolderVersion,
) -> Response[ICustomFieldFolder]:
    r"""Update Custom Field Folder Name

     <div>
        <p> Create Custom Field Folder </p>
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
        version (UpdateCustomFieldFolderVersion):
        body (UpdateFolder):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ICustomFieldFolder]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: UpdateFolder,
    version: UpdateCustomFieldFolderVersion,
) -> ICustomFieldFolder | None:
    r"""Update Custom Field Folder Name

     <div>
        <p> Create Custom Field Folder </p>
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
        version (UpdateCustomFieldFolderVersion):
        body (UpdateFolder):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ICustomFieldFolder
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFolder,
    version: UpdateCustomFieldFolderVersion,
) -> Response[ICustomFieldFolder]:
    r"""Update Custom Field Folder Name

     <div>
        <p> Create Custom Field Folder </p>
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
        version (UpdateCustomFieldFolderVersion):
        body (UpdateFolder):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ICustomFieldFolder]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateFolder,
    version: UpdateCustomFieldFolderVersion,
) -> ICustomFieldFolder | None:
    r"""Update Custom Field Folder Name

     <div>
        <p> Create Custom Field Folder </p>
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
        version (UpdateCustomFieldFolderVersion):
        body (UpdateFolder):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ICustomFieldFolder
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
