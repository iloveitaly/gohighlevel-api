from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_field_field_value import FileFieldFieldValue


T = TypeVar("T", bound="FileField")


@_attrs_define
class FileField:
    """
    Attributes:
        id (str):  Example: 6dvNaf7VhkQ9snc5vnjJ.
        field_value (FileFieldFieldValue | Unset):  Example: {'f31175d4-2b06-4fc6-b7bc-74cd814c68cb': {'documentId':
            'w2M9qTZ0ZJz8rGt02jdJ', 'meta': {'encoding': '7bit', 'fieldname': '1HeGizb13P0odwgOgKSs', 'mimetype':
            'image/jpeg', 'originalname': 'IMG_20231215_164412935.jpg', 'size': 1786611, 'uuid':
            'f31175d4-2b06-4fc6-b7bc-74cd814c68cb'}, 'url':
            'https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ'}}.
        key (str | Unset):  Example: my_custom_field.
    """

    id: str
    field_value: FileFieldFieldValue | Unset = UNSET
    key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_value, Unset):
            field_value = self.field_value.to_dict()

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
        from ..models.file_field_field_value import FileFieldFieldValue

        d = dict(src_dict)
        id = d.pop("id")

        _field_value = d.pop("fieldValue", UNSET)
        field_value: FileFieldFieldValue | Unset
        if isinstance(_field_value, Unset):
            field_value = UNSET
        else:
            field_value = FileFieldFieldValue.from_dict(_field_value)

        key = d.pop("key", UNSET)

        file_field = cls(
            id=id,
            field_value=field_value,
            key=key,
        )

        file_field.additional_properties = d
        return file_field

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
