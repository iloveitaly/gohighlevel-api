from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactsMetaSchema")


@_attrs_define
class ContactsMetaSchema:
    """
    Attributes:
        current_page (float | Unset):  Example: 2.
        next_page (float | Unset):  Example: 3.
        next_page_url (str | Unset):  Example: http://localhost:5058/contacts/?locationId=ve9EPM428h8vShlRW1KT&startAfte
            r=1631087949919&startAfterId=yd0jdjOavGk2o6Nh5Ndb.
        prev_page (float | None | Unset):  Example: 1.
        start_after (float | Unset):  Example: 1631087949919.
        start_after_id (str | Unset):  Example: yd0jdjOavGk2o6Nh5Ndb.
        total (float | Unset):  Example: 50.
    """

    current_page: float | Unset = UNSET
    next_page: float | Unset = UNSET
    next_page_url: str | Unset = UNSET
    prev_page: float | None | Unset = UNSET
    start_after: float | Unset = UNSET
    start_after_id: str | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        next_page = self.next_page

        next_page_url = self.next_page_url

        prev_page: float | None | Unset
        if isinstance(self.prev_page, Unset):
            prev_page = UNSET
        else:
            prev_page = self.prev_page

        start_after = self.start_after

        start_after_id = self.start_after_id

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page
        if next_page_url is not UNSET:
            field_dict["nextPageUrl"] = next_page_url
        if prev_page is not UNSET:
            field_dict["prevPage"] = prev_page
        if start_after is not UNSET:
            field_dict["startAfter"] = start_after
        if start_after_id is not UNSET:
            field_dict["startAfterId"] = start_after_id
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("currentPage", UNSET)

        next_page = d.pop("nextPage", UNSET)

        next_page_url = d.pop("nextPageUrl", UNSET)

        def _parse_prev_page(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        prev_page = _parse_prev_page(d.pop("prevPage", UNSET))

        start_after = d.pop("startAfter", UNSET)

        start_after_id = d.pop("startAfterId", UNSET)

        total = d.pop("total", UNSET)

        contacts_meta_schema = cls(
            current_page=current_page,
            next_page=next_page,
            next_page_url=next_page_url,
            prev_page=prev_page,
            start_after=start_after,
            start_after_id=start_after_id,
            total=total,
        )

        contacts_meta_schema.additional_properties = d
        return contacts_meta_schema

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
