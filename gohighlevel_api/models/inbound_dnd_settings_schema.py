from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_dnd_setting_schema import InboundDndSettingSchema


T = TypeVar("T", bound="InboundDndSettingsSchema")


@_attrs_define
class InboundDndSettingsSchema:
    """
    Attributes:
        all_ (InboundDndSettingSchema | Unset):
    """

    all_: InboundDndSettingSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_, Unset):
            all_ = self.all_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbound_dnd_setting_schema import InboundDndSettingSchema

        d = dict(src_dict)
        _all_ = d.pop("all", UNSET)
        all_: InboundDndSettingSchema | Unset
        if isinstance(_all_, Unset):
            all_ = UNSET
        else:
            all_ = InboundDndSettingSchema.from_dict(_all_)

        inbound_dnd_settings_schema = cls(
            all_=all_,
        )

        inbound_dnd_settings_schema.additional_properties = d
        return inbound_dnd_settings_schema

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
