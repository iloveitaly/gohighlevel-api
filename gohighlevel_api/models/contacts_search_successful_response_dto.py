from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_search_schema import ContactsSearchSchema


T = TypeVar("T", bound="ContactsSearchSuccessfulResponseDto")


@_attrs_define
class ContactsSearchSuccessfulResponseDto:
    """
    Attributes:
        contacts (list[ContactsSearchSchema] | Unset):
        count (float | Unset):  Example: 10.
    """

    contacts: list[ContactsSearchSchema] | Unset = UNSET
    count: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_search_schema import ContactsSearchSchema

        d = dict(src_dict)
        _contacts = d.pop("contacts", UNSET)
        contacts: list[ContactsSearchSchema] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = ContactsSearchSchema.from_dict(contacts_item_data)

                contacts.append(contacts_item)

        count = d.pop("count", UNSET)

        contacts_search_successful_response_dto = cls(
            contacts=contacts,
            count=count,
        )

        contacts_search_successful_response_dto.additional_properties = d
        return contacts_search_successful_response_dto

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
