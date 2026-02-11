from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_custom_field import ICustomField


T = TypeVar("T", bound="CustomFieldSuccessfulResponseDto")


@_attrs_define
class CustomFieldSuccessfulResponseDto:
    """
    Attributes:
        field (ICustomField | Unset):
    """

    field: ICustomField | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_custom_field import ICustomField

        d = dict(src_dict)
        _field = d.pop("field", UNSET)
        field: ICustomField | Unset
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = ICustomField.from_dict(_field)

        custom_field_successful_response_dto = cls(
            field=field,
        )

        custom_field_successful_response_dto.additional_properties = d
        return custom_field_successful_response_dto

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
