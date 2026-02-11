from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateFolder")


@_attrs_define
class CreateFolder:
    """
    Attributes:
        location_id (str): Location Id Example: ve9EPM428h8vShlRW1KT.
        name (str): Field name Example: Name.
        object_key (str): The key for your custom object. This key uniquely identifies the custom object. Example:
            "custom_object.pet" for a custom object related to pets. Example: custom_object.pet.
    """

    location_id: str
    name: str
    object_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_id = self.location_id

        name = self.name

        object_key = self.object_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locationId": location_id,
                "name": name,
                "objectKey": object_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location_id = d.pop("locationId")

        name = d.pop("name")

        object_key = d.pop("objectKey")

        create_folder = cls(
            location_id=location_id,
            name=name,
            object_key=object_key,
        )

        create_folder.additional_properties = d
        return create_folder

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
