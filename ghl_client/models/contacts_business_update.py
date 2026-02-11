from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ContactsBusinessUpdate")


@_attrs_define
class ContactsBusinessUpdate:
    """
    Attributes:
        business_id (None | str):  Example: 63b7ec34ea409a9a8bd2a4ff.
        ids (list[str]):  Example: ['IDqvFHGColiyK6jiatuz', 'pOC0uJ97VYOKH2m3fkMD'].
        location_id (str):  Example: PX8m5VwxEbcpFlzYEPVG.
    """

    business_id: None | str
    ids: list[str]
    location_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id: None | str
        business_id = self.business_id

        ids = self.ids

        location_id = self.location_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businessId": business_id,
                "ids": ids,
                "locationId": location_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_business_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        business_id = _parse_business_id(d.pop("businessId"))

        ids = cast(list[str], d.pop("ids"))

        location_id = d.pop("locationId")

        contacts_business_update = cls(
            business_id=business_id,
            ids=ids,
            location_id=location_id,
        )

        contacts_business_update.additional_properties = d
        return contacts_business_update

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
