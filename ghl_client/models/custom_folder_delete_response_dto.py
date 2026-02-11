from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomFolderDeleteResponseDto")


@_attrs_define
class CustomFolderDeleteResponseDto:
    """
    Attributes:
        id (str):  Example: 3v34PM428h8vShlRW1KT.
        key (str):  Example: custom_object.pet.name.
        succeded (bool):  Example: True.
    """

    id: str
    key: str
    succeded: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        succeded = self.succeded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key": key,
                "succeded": succeded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        succeded = d.pop("succeded")

        custom_folder_delete_response_dto = cls(
            id=id,
            key=key,
            succeded=succeded,
        )

        custom_folder_delete_response_dto.additional_properties = d
        return custom_folder_delete_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
