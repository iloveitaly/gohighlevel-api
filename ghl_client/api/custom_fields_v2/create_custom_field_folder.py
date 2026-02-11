from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_custom_field_folder_version import CreateCustomFieldFolderVersion
from ...models.create_folder import CreateFolder
from ...models.i_custom_field_folder import ICustomFieldFolder
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFolder,
    version: CreateCustomFieldFolderVersion,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Version"] = str(version)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/custom-fields/folder",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ICustomFieldFolder | None:
    if response.status_code == 201:
        response_201 = ICustomFieldFolder.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: CreateFolder,
    version: CreateCustomFieldFolderVersion,
) -> Response[ICustomFieldFolder]:
    r"""Create Custom Field Folder

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
        version (CreateCustomFieldFolderVersion):
        body (CreateFolder):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ICustomFieldFolder]
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
    body: CreateFolder,
    version: CreateCustomFieldFolderVersion,
) -> ICustomFieldFolder | None:
    r"""Create Custom Field Folder

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
        version (CreateCustomFieldFolderVersion):
        body (CreateFolder):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ICustomFieldFolder
    """

    return sync_detailed(
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFolder,
    version: CreateCustomFieldFolderVersion,
) -> Response[ICustomFieldFolder]:
    r"""Create Custom Field Folder

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
        version (CreateCustomFieldFolderVersion):
        body (CreateFolder):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ICustomFieldFolder]
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
    body: CreateFolder,
    version: CreateCustomFieldFolderVersion,
) -> ICustomFieldFolder | None:
    r"""Create Custom Field Folder

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
        version (CreateCustomFieldFolderVersion):
        body (CreateFolder):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ICustomFieldFolder
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            version=version,
        )
    ).parsed
