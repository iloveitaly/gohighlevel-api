from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactsWorkflowSuccessfulResponseDto")


@_attrs_define
class ContactsWorkflowSuccessfulResponseDto:
    """
    Attributes:
        succeded (bool | Unset):  Example: True.
    """

    succeded: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        succeded = self.succeded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if succeded is not UNSET:
            field_dict["succeded"] = succeded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        succeded = d.pop("succeded", UNSET)

        contacts_workflow_successful_response_dto = cls(
            succeded=succeded,
        )

        contacts_workflow_successful_response_dto.additional_properties = d
        return contacts_workflow_successful_response_dto

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
