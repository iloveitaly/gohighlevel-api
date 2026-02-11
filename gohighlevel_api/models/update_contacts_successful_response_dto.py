from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_contect_by_id_schema import GetContectByIdSchema


T = TypeVar("T", bound="UpdateContactsSuccessfulResponseDto")


@_attrs_define
class UpdateContactsSuccessfulResponseDto:
    """
    Attributes:
        contact (GetContectByIdSchema | Unset):
        succeded (bool | Unset):  Example: True.
    """

    contact: GetContectByIdSchema | Unset = UNSET
    succeded: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        succeded = self.succeded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if succeded is not UNSET:
            field_dict["succeded"] = succeded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_contect_by_id_schema import GetContectByIdSchema

        d = dict(src_dict)
        _contact = d.pop("contact", UNSET)
        contact: GetContectByIdSchema | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = GetContectByIdSchema.from_dict(_contact)

        succeded = d.pop("succeded", UNSET)

        update_contacts_successful_response_dto = cls(
            contact=contact,
            succeded=succeded,
        )

        update_contacts_successful_response_dto.additional_properties = d
        return update_contacts_successful_response_dto

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
