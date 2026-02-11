from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldsInputStringSchema")


@_attrs_define
class CustomFieldsInputStringSchema:
    """
    Attributes:
        field_value (str | Unset):  Example: 9039160788.
        id (str | Unset): Pass either `id` or `key` of custom field Example: 6dvNaf7VhkQ9snc5vnjJ.
        key (str | Unset): Pass either `id` or `key` of custom field Example: my_custom_field.
    """

    field_value: str | Unset = UNSET
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_value = self.field_value

        id = self.id

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_value is not UNSET:
            field_dict["fieldValue"] = field_value
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_value = d.pop("fieldValue", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        custom_fields_input_string_schema = cls(
            field_value=field_value,
            id=id,
            key=key,
        )

        custom_fields_input_string_schema.additional_properties = d
        return custom_fields_input_string_schema

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
