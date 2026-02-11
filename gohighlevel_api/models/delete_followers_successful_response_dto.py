from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteFollowersSuccessfulResponseDto")


@_attrs_define
class DeleteFollowersSuccessfulResponseDto:
    """
    Attributes:
        followers (list[str] | Unset):  Example: ['sx6wyHhbFdRXh302Lunr', 'sx6wyHhbFdRXh302LLss'].
        followers_removed (list[str] | Unset):  Example: ['Mx6wyHhbFdRXh302Luer', 'Ka6wyHhbFdRXh302LLsAm'].
    """

    followers: list[str] | Unset = UNSET
    followers_removed: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followers: list[str] | Unset = UNSET
        if not isinstance(self.followers, Unset):
            followers = self.followers

        followers_removed: list[str] | Unset = UNSET
        if not isinstance(self.followers_removed, Unset):
            followers_removed = self.followers_removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if followers is not UNSET:
            field_dict["followers"] = followers
        if followers_removed is not UNSET:
            field_dict["followersRemoved"] = followers_removed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        followers = cast(list[str], d.pop("followers", UNSET))

        followers_removed = cast(list[str], d.pop("followersRemoved", UNSET))

        delete_followers_successful_response_dto = cls(
            followers=followers,
            followers_removed=followers_removed,
        )

        delete_followers_successful_response_dto.additional_properties = d
        return delete_followers_successful_response_dto

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
