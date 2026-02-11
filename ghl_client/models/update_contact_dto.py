from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox_field import CheckboxField
    from ..models.dnd_settings_schema import DndSettingsSchema
    from ..models.file_field import FileField
    from ..models.inbound_dnd_settings_schema import InboundDndSettingsSchema
    from ..models.large_text_field import LargeTextField
    from ..models.monetory_field import MonetoryField
    from ..models.multi_select_field import MultiSelectField
    from ..models.numeric_field import NumericField
    from ..models.radio_field import RadioField
    from ..models.single_select_field import SingleSelectField
    from ..models.text_field import TextField


T = TypeVar("T", bound="UpdateContactDto")


@_attrs_define
class UpdateContactDto:
    """
    Attributes:
        address1 (None | str | Unset):  Example: 3535 1st St N.
        assigned_to (None | str | Unset): User's Id Example: y0BeYjuRIlDwsDcOHOJo.
        city (None | str | Unset):  Example: Dolomite.
        country (str | Unset):  Example: US.
        custom_fields (list[CheckboxField | FileField | LargeTextField | MonetoryField | MultiSelectField | NumericField
            | RadioField | SingleSelectField | TextField] | Unset):
        dnd (bool | Unset):  Example: True.
        dnd_settings (DndSettingsSchema | Unset):
        email (None | str | Unset):  Example: rosan@deos.com.
        first_name (None | str | Unset):  Example: rosan.
        inbound_dnd_settings (InboundDndSettingsSchema | Unset):
        last_name (None | str | Unset):  Example: Deo.
        name (None | str | Unset):  Example: rosan Deo.
        phone (None | str | Unset):  Example: +1 888-888-8888.
        postal_code (str | Unset):  Example: 35061.
        source (None | str | Unset):  Example: public api.
        state (None | str | Unset):  Example: AL.
        tags (list[str] | Unset): This field will overwrite all current tags associated with the contact. To update a
            tags, it is recommended to use the Add Tag or Remove Tag API instead. Example: ['nisi sint commodo amet',
            'consequat'].
        timezone (None | str | Unset):  Example: America/Chihuahua.
        website (None | str | Unset):  Example: https://www.tesla.com.
    """

    address1: None | str | Unset = UNSET
    assigned_to: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: str | Unset = UNSET
    custom_fields: (
        list[
            CheckboxField
            | FileField
            | LargeTextField
            | MonetoryField
            | MultiSelectField
            | NumericField
            | RadioField
            | SingleSelectField
            | TextField
        ]
        | Unset
    ) = UNSET
    dnd: bool | Unset = UNSET
    dnd_settings: DndSettingsSchema | Unset = UNSET
    email: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    inbound_dnd_settings: InboundDndSettingsSchema | Unset = UNSET
    last_name: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    postal_code: str | Unset = UNSET
    source: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    timezone: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox_field import CheckboxField
        from ..models.large_text_field import LargeTextField
        from ..models.monetory_field import MonetoryField
        from ..models.multi_select_field import MultiSelectField
        from ..models.numeric_field import NumericField
        from ..models.radio_field import RadioField
        from ..models.single_select_field import SingleSelectField
        from ..models.text_field import TextField

        address1: None | str | Unset
        if isinstance(self.address1, Unset):
            address1 = UNSET
        else:
            address1 = self.address1

        assigned_to: None | str | Unset
        if isinstance(self.assigned_to, Unset):
            assigned_to = UNSET
        else:
            assigned_to = self.assigned_to

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country = self.country

        custom_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item: dict[str, Any]
                if isinstance(custom_fields_item_data, TextField):
                    custom_fields_item = custom_fields_item_data.to_dict()
                elif isinstance(custom_fields_item_data, LargeTextField):
                    custom_fields_item = custom_fields_item_data.to_dict()
                elif isinstance(custom_fields_item_data, SingleSelectField):
                    custom_fields_item = custom_fields_item_data.to_dict()
                elif isinstance(custom_fields_item_data, RadioField):
                    custom_fields_item = custom_fields_item_data.to_dict()
                elif isinstance(custom_fields_item_data, NumericField):
                    custom_fields_item = custom_fields_item_data.to_dict()
                elif isinstance(custom_fields_item_data, MonetoryField):
                    custom_fields_item = custom_fields_item_data.to_dict()
                elif isinstance(custom_fields_item_data, CheckboxField):
                    custom_fields_item = custom_fields_item_data.to_dict()
                elif isinstance(custom_fields_item_data, MultiSelectField):
                    custom_fields_item = custom_fields_item_data.to_dict()
                else:
                    custom_fields_item = custom_fields_item_data.to_dict()

                custom_fields.append(custom_fields_item)

        dnd = self.dnd

        dnd_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dnd_settings, Unset):
            dnd_settings = self.dnd_settings.to_dict()

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        inbound_dnd_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inbound_dnd_settings, Unset):
            inbound_dnd_settings = self.inbound_dnd_settings.to_dict()

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        postal_code = self.postal_code

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if dnd is not UNSET:
            field_dict["dnd"] = dnd
        if dnd_settings is not UNSET:
            field_dict["dndSettings"] = dnd_settings
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if inbound_dnd_settings is not UNSET:
            field_dict["inboundDndSettings"] = inbound_dnd_settings
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if source is not UNSET:
            field_dict["source"] = source
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox_field import CheckboxField
        from ..models.dnd_settings_schema import DndSettingsSchema
        from ..models.file_field import FileField
        from ..models.inbound_dnd_settings_schema import InboundDndSettingsSchema
        from ..models.large_text_field import LargeTextField
        from ..models.monetory_field import MonetoryField
        from ..models.multi_select_field import MultiSelectField
        from ..models.numeric_field import NumericField
        from ..models.radio_field import RadioField
        from ..models.single_select_field import SingleSelectField
        from ..models.text_field import TextField

        d = dict(src_dict)

        def _parse_address1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address1 = _parse_address1(d.pop("address1", UNSET))

        def _parse_assigned_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assigned_to = _parse_assigned_to(d.pop("assignedTo", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        country = d.pop("country", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: (
            list[
                CheckboxField
                | FileField
                | LargeTextField
                | MonetoryField
                | MultiSelectField
                | NumericField
                | RadioField
                | SingleSelectField
                | TextField
            ]
            | Unset
        ) = UNSET
        if _custom_fields is not UNSET:
            custom_fields = []
            for custom_fields_item_data in _custom_fields:

                def _parse_custom_fields_item(
                    data: object,
                ) -> (
                    CheckboxField
                    | FileField
                    | LargeTextField
                    | MonetoryField
                    | MultiSelectField
                    | NumericField
                    | RadioField
                    | SingleSelectField
                    | TextField
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_item_type_0 = TextField.from_dict(data)

                        return custom_fields_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_item_type_1 = LargeTextField.from_dict(data)

                        return custom_fields_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_item_type_2 = SingleSelectField.from_dict(data)

                        return custom_fields_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_item_type_3 = RadioField.from_dict(data)

                        return custom_fields_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_item_type_4 = NumericField.from_dict(data)

                        return custom_fields_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_item_type_5 = MonetoryField.from_dict(data)

                        return custom_fields_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_item_type_6 = CheckboxField.from_dict(data)

                        return custom_fields_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_item_type_7 = MultiSelectField.from_dict(data)

                        return custom_fields_item_type_7
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    custom_fields_item_type_8 = FileField.from_dict(data)

                    return custom_fields_item_type_8

                custom_fields_item = _parse_custom_fields_item(custom_fields_item_data)

                custom_fields.append(custom_fields_item)

        dnd = d.pop("dnd", UNSET)

        _dnd_settings = d.pop("dndSettings", UNSET)
        dnd_settings: DndSettingsSchema | Unset
        if isinstance(_dnd_settings, Unset):
            dnd_settings = UNSET
        else:
            dnd_settings = DndSettingsSchema.from_dict(_dnd_settings)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        _inbound_dnd_settings = d.pop("inboundDndSettings", UNSET)
        inbound_dnd_settings: InboundDndSettingsSchema | Unset
        if isinstance(_inbound_dnd_settings, Unset):
            inbound_dnd_settings = UNSET
        else:
            inbound_dnd_settings = InboundDndSettingsSchema.from_dict(_inbound_dnd_settings)

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        postal_code = d.pop("postalCode", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        update_contact_dto = cls(
            address1=address1,
            assigned_to=assigned_to,
            city=city,
            country=country,
            custom_fields=custom_fields,
            dnd=dnd,
            dnd_settings=dnd_settings,
            email=email,
            first_name=first_name,
            inbound_dnd_settings=inbound_dnd_settings,
            last_name=last_name,
            name=name,
            phone=phone,
            postal_code=postal_code,
            source=source,
            state=state,
            tags=tags,
            timezone=timezone,
            website=website,
        )

        update_contact_dto.additional_properties = d
        return update_contact_dto

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
