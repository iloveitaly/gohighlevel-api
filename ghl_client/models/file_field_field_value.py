from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileFieldFieldValue")


@_attrs_define
class FileFieldFieldValue:
    """
    Example:
        {'f31175d4-2b06-4fc6-b7bc-74cd814c68cb': {'documentId': 'w2M9qTZ0ZJz8rGt02jdJ', 'meta': {'encoding': '7bit',
            'fieldname': '1HeGizb13P0odwgOgKSs', 'mimetype': 'image/jpeg', 'originalname': 'IMG_20231215_164412935.jpg',
            'size': 1786611, 'uuid': 'f31175d4-2b06-4fc6-b7bc-74cd814c68cb'}, 'url':
            'https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ'}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_field_field_value = cls()

        file_field_field_value.additional_properties = d
        return file_field_field_value

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
