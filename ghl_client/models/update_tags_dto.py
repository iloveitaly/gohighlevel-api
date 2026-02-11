from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTagsDTO")


@_attrs_define
class UpdateTagsDTO:
    """
    Attributes:
        contacts (list[str]): list of contact ids to be processed Example: ['qFSqySFkVvNzOSqgGqFi', 'abcdef',
            'qFSqySFkVvNzOSqgGqFi', '3ualbhnV7j3n3a9r2moD'].
        location_id (str): location id from where the bulk request is executed Example: asdrwHvLUxlfw5SqKVCN.
        tags (list[str]): list of tags to be added or removed Example: ['tag-1', 'tag-2'].
        remove_all_tags (bool | Unset): Option to implement remove all tags. if true, all tags will be removed from the
            contacts. Can only be used with remove type. Example: false.
    """

    contacts: list[str]
    location_id: str
    tags: list[str]
    remove_all_tags: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contacts = self.contacts

        location_id = self.location_id

        tags = self.tags

        remove_all_tags = self.remove_all_tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contacts": contacts,
                "locationId": location_id,
                "tags": tags,
            }
        )
        if remove_all_tags is not UNSET:
            field_dict["removeAllTags"] = remove_all_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contacts = cast(list[str], d.pop("contacts"))

        location_id = d.pop("locationId")

        tags = cast(list[str], d.pop("tags"))

        remove_all_tags = d.pop("removeAllTags", UNSET)

        update_tags_dto = cls(
            contacts=contacts,
            location_id=location_id,
            tags=tags,
            remove_all_tags=remove_all_tags,
        )

        update_tags_dto.additional_properties = d
        return update_tags_dto

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
