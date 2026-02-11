from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dnd_setting_schema import DndSettingSchema


T = TypeVar("T", bound="DndSettingsSchema")


@_attrs_define
class DndSettingsSchema:
    """
    Attributes:
        call (DndSettingSchema | Unset):
        email (DndSettingSchema | Unset):
        fb (DndSettingSchema | Unset):
        gmb (DndSettingSchema | Unset):
        sms (DndSettingSchema | Unset):
        whats_app (DndSettingSchema | Unset):
    """

    call: DndSettingSchema | Unset = UNSET
    email: DndSettingSchema | Unset = UNSET
    fb: DndSettingSchema | Unset = UNSET
    gmb: DndSettingSchema | Unset = UNSET
    sms: DndSettingSchema | Unset = UNSET
    whats_app: DndSettingSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call: dict[str, Any] | Unset = UNSET
        if not isinstance(self.call, Unset):
            call = self.call.to_dict()

        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        fb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fb, Unset):
            fb = self.fb.to_dict()

        gmb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmb, Unset):
            gmb = self.gmb.to_dict()

        sms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sms, Unset):
            sms = self.sms.to_dict()

        whats_app: dict[str, Any] | Unset = UNSET
        if not isinstance(self.whats_app, Unset):
            whats_app = self.whats_app.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call is not UNSET:
            field_dict["Call"] = call
        if email is not UNSET:
            field_dict["Email"] = email
        if fb is not UNSET:
            field_dict["FB"] = fb
        if gmb is not UNSET:
            field_dict["GMB"] = gmb
        if sms is not UNSET:
            field_dict["SMS"] = sms
        if whats_app is not UNSET:
            field_dict["WhatsApp"] = whats_app

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dnd_setting_schema import DndSettingSchema

        d = dict(src_dict)
        _call = d.pop("Call", UNSET)
        call: DndSettingSchema | Unset
        if isinstance(_call, Unset):
            call = UNSET
        else:
            call = DndSettingSchema.from_dict(_call)

        _email = d.pop("Email", UNSET)
        email: DndSettingSchema | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = DndSettingSchema.from_dict(_email)

        _fb = d.pop("FB", UNSET)
        fb: DndSettingSchema | Unset
        if isinstance(_fb, Unset):
            fb = UNSET
        else:
            fb = DndSettingSchema.from_dict(_fb)

        _gmb = d.pop("GMB", UNSET)
        gmb: DndSettingSchema | Unset
        if isinstance(_gmb, Unset):
            gmb = UNSET
        else:
            gmb = DndSettingSchema.from_dict(_gmb)

        _sms = d.pop("SMS", UNSET)
        sms: DndSettingSchema | Unset
        if isinstance(_sms, Unset):
            sms = UNSET
        else:
            sms = DndSettingSchema.from_dict(_sms)

        _whats_app = d.pop("WhatsApp", UNSET)
        whats_app: DndSettingSchema | Unset
        if isinstance(_whats_app, Unset):
            whats_app = UNSET
        else:
            whats_app = DndSettingSchema.from_dict(_whats_app)

        dnd_settings_schema = cls(
            call=call,
            email=email,
            fb=fb,
            gmb=gmb,
            sms=sms,
            whats_app=whats_app,
        )

        dnd_settings_schema.additional_properties = d
        return dnd_settings_schema

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
