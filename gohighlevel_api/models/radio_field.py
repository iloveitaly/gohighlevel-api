from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadioField")


@_attrs_define
class RadioField:
    """
    Attributes:
        id (str):  Example: 6dvNaf7VhkQ9snc5vnjJ.
        field_value (str | Unset):  Example: My Selected Option.
        key (str | Unset):  Example: my_custom_field.
    """

    id: str
    field_value: str | Unset = UNSET
    key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_value = self.field_value

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if field_value is not UNSET:
            field_dict["fieldValue"] = field_value
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        field_value = d.pop("fieldValue", UNSET)

        key = d.pop("key", UNSET)

        radio_field = cls(
            id=id,
            field_value=field_value,
            key=key,
        )

        radio_field.additional_properties = d
        return radio_field

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
