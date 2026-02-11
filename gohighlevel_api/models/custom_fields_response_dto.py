from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_custom_field import ICustomField


T = TypeVar("T", bound="CustomFieldsResponseDTO")


@_attrs_define
class CustomFieldsResponseDTO:
    """
    Attributes:
        fields (list[ICustomField] | Unset): Custom Fields for the object.
        folders (list[ICustomField] | Unset): Custom Fields folder for the object.
    """

    fields: list[ICustomField] | Unset = UNSET
    folders: list[ICustomField] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        folders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if folders is not UNSET:
            field_dict["folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_custom_field import ICustomField

        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: list[ICustomField] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = ICustomField.from_dict(fields_item_data)

                fields.append(fields_item)

        _folders = d.pop("folders", UNSET)
        folders: list[ICustomField] | Unset = UNSET
        if _folders is not UNSET:
            folders = []
            for folders_item_data in _folders:
                folders_item = ICustomField.from_dict(folders_item_data)

                folders.append(folders_item)

        custom_fields_response_dto = cls(
            fields=fields,
            folders=folders,
        )

        custom_fields_response_dto.additional_properties = d
        return custom_fields_response_dto

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
