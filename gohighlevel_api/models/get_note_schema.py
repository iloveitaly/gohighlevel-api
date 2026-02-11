from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNoteSchema")


@_attrs_define
class GetNoteSchema:
    """
    Attributes:
        body (str | Unset):  Example: lorem ipsum.
        contact_id (str | Unset):  Example: TUcmRxWrjqzJS8EjkxNK.
        date_added (str | Unset):  Example: 2021-07-08T12:02:11.285Z.
        id (str | Unset):  Example: HGPcayliwcdoUFzvbTok.
        user_id (str | Unset):  Example: TUcmRxWrjqzJS8EjkxNK.
    """

    body: str | Unset = UNSET
    contact_id: str | Unset = UNSET
    date_added: str | Unset = UNSET
    id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        contact_id = self.contact_id

        date_added = self.date_added

        id = self.id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if date_added is not UNSET:
            field_dict["dateAdded"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body", UNSET)

        contact_id = d.pop("contactId", UNSET)

        date_added = d.pop("dateAdded", UNSET)

        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        get_note_schema = cls(
            body=body,
            contact_id=contact_id,
            date_added=date_added,
            id=id,
            user_id=user_id,
        )

        get_note_schema.additional_properties = d
        return get_note_schema

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
