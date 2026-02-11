from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribution_source import AttributionSource
    from ..models.custom_field_schema import CustomFieldSchema
    from ..models.dnd_settings_schema import DndSettingsSchema


T = TypeVar("T", bound="GetContectByIdSchema")


@_attrs_define
class GetContectByIdSchema:
    """
    Attributes:
        address1 (str | Unset):  Example: 3535 1st St N.
        assigned_to (str | Unset):  Example: ve9EPM428h8vShlRW1KT.
        attachments (str | Unset):
        attribution_source (AttributionSource | Unset):
        business_id (str | Unset):  Example: 641c094001436dbc2081e642.
        city (str | Unset):  Example: ruDolomitebika.
        company_name (str | Unset):  Example: DGS VolMAX.
        country (str | Unset):  Example: US.
        custom_fields (list[CustomFieldSchema] | Unset):
        date_added (str | Unset):  Example: 2021-07-02T05:18:26.704Z.
        date_of_birth (str | Unset):  Example: 1990-09-25T00:00:00.000Z.
        date_updated (str | Unset):  Example: 2021-07-02T05:18:26.704Z.
        dnd (bool | Unset):  Example: True.
        dnd_settings (DndSettingsSchema | Unset):
        email (str | Unset):  Example: rubika@deos.com.
        email_lower_case (str | Unset):  Example: rubika@deos.com.
        first_name (str | Unset):  Example: rubika.
        first_name_lower_case (str | Unset):  Example: rubika.
        full_name_lower_case (str | Unset):  Example: rubika deo.
        id (str | Unset):  Example: seD4PfOuKoVMLkEZqohJ.
        keyword (str | Unset):  Example: test.
        last_activity (str | Unset):  Example: 2021-07-16T11:39:30.564Z.
        last_attribution_source (AttributionSource | Unset):
        last_name (str | Unset):  Example: Deo.
        last_name_lower_case (str | Unset):  Example: deo.
        location_id (str | Unset):  Example: ve9EPM428h8vShlRW1KT.
        name (str | Unset):  Example: rubika deo.
        phone (str | Unset):  Example: +18832327657.
        postal_code (str | Unset):  Example: 35061.
        source (str | Unset):  Example: public api.
        ssn (str | Unset):
        state (str | Unset):  Example: AL.
        tags (list[str] | Unset):  Example: ['nisi sint commodo amet', 'consequat'].
        timezone (str | Unset):
        type_ (str | Unset):  Example: read.
        visitor_id (str | Unset): visitorId is the Unique ID assigned to each Live chat visitor. Example:
            ve9EPM428h8vShlRW1KT.
        website (str | Unset):  Example: https://www.tesla.com.
    """

    address1: str | Unset = UNSET
    assigned_to: str | Unset = UNSET
    attachments: str | Unset = UNSET
    attribution_source: AttributionSource | Unset = UNSET
    business_id: str | Unset = UNSET
    city: str | Unset = UNSET
    company_name: str | Unset = UNSET
    country: str | Unset = UNSET
    custom_fields: list[CustomFieldSchema] | Unset = UNSET
    date_added: str | Unset = UNSET
    date_of_birth: str | Unset = UNSET
    date_updated: str | Unset = UNSET
    dnd: bool | Unset = UNSET
    dnd_settings: DndSettingsSchema | Unset = UNSET
    email: str | Unset = UNSET
    email_lower_case: str | Unset = UNSET
    first_name: str | Unset = UNSET
    first_name_lower_case: str | Unset = UNSET
    full_name_lower_case: str | Unset = UNSET
    id: str | Unset = UNSET
    keyword: str | Unset = UNSET
    last_activity: str | Unset = UNSET
    last_attribution_source: AttributionSource | Unset = UNSET
    last_name: str | Unset = UNSET
    last_name_lower_case: str | Unset = UNSET
    location_id: str | Unset = UNSET
    name: str | Unset = UNSET
    phone: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    source: str | Unset = UNSET
    ssn: str | Unset = UNSET
    state: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    timezone: str | Unset = UNSET
    type_: str | Unset = UNSET
    visitor_id: str | Unset = UNSET
    website: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address1 = self.address1

        assigned_to = self.assigned_to

        attachments = self.attachments

        attribution_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attribution_source, Unset):
            attribution_source = self.attribution_source.to_dict()

        business_id = self.business_id

        city = self.city

        company_name = self.company_name

        country = self.country

        custom_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        date_added = self.date_added

        date_of_birth = self.date_of_birth

        date_updated = self.date_updated

        dnd = self.dnd

        dnd_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dnd_settings, Unset):
            dnd_settings = self.dnd_settings.to_dict()

        email = self.email

        email_lower_case = self.email_lower_case

        first_name = self.first_name

        first_name_lower_case = self.first_name_lower_case

        full_name_lower_case = self.full_name_lower_case

        id = self.id

        keyword = self.keyword

        last_activity = self.last_activity

        last_attribution_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_attribution_source, Unset):
            last_attribution_source = self.last_attribution_source.to_dict()

        last_name = self.last_name

        last_name_lower_case = self.last_name_lower_case

        location_id = self.location_id

        name = self.name

        phone = self.phone

        postal_code = self.postal_code

        source = self.source

        ssn = self.ssn

        state = self.state

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        timezone = self.timezone

        type_ = self.type_

        visitor_id = self.visitor_id

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if attribution_source is not UNSET:
            field_dict["attributionSource"] = attribution_source
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if city is not UNSET:
            field_dict["city"] = city
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if country is not UNSET:
            field_dict["country"] = country
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if date_added is not UNSET:
            field_dict["dateAdded"] = date_added
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if dnd is not UNSET:
            field_dict["dnd"] = dnd
        if dnd_settings is not UNSET:
            field_dict["dndSettings"] = dnd_settings
        if email is not UNSET:
            field_dict["email"] = email
        if email_lower_case is not UNSET:
            field_dict["emailLowerCase"] = email_lower_case
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if first_name_lower_case is not UNSET:
            field_dict["firstNameLowerCase"] = first_name_lower_case
        if full_name_lower_case is not UNSET:
            field_dict["fullNameLowerCase"] = full_name_lower_case
        if id is not UNSET:
            field_dict["id"] = id
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if last_activity is not UNSET:
            field_dict["lastActivity"] = last_activity
        if last_attribution_source is not UNSET:
            field_dict["lastAttributionSource"] = last_attribution_source
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if last_name_lower_case is not UNSET:
            field_dict["lastNameLowerCase"] = last_name_lower_case
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if source is not UNSET:
            field_dict["source"] = source
        if ssn is not UNSET:
            field_dict["ssn"] = ssn
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if type_ is not UNSET:
            field_dict["type"] = type_
        if visitor_id is not UNSET:
            field_dict["visitorId"] = visitor_id
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribution_source import AttributionSource
        from ..models.custom_field_schema import CustomFieldSchema
        from ..models.dnd_settings_schema import DndSettingsSchema

        d = dict(src_dict)
        address1 = d.pop("address1", UNSET)

        assigned_to = d.pop("assignedTo", UNSET)

        attachments = d.pop("attachments", UNSET)

        _attribution_source = d.pop("attributionSource", UNSET)
        attribution_source: AttributionSource | Unset
        if isinstance(_attribution_source, Unset):
            attribution_source = UNSET
        else:
            attribution_source = AttributionSource.from_dict(_attribution_source)

        business_id = d.pop("businessId", UNSET)

        city = d.pop("city", UNSET)

        company_name = d.pop("companyName", UNSET)

        country = d.pop("country", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: list[CustomFieldSchema] | Unset = UNSET
        if _custom_fields is not UNSET:
            custom_fields = []
            for custom_fields_item_data in _custom_fields:
                custom_fields_item = CustomFieldSchema.from_dict(custom_fields_item_data)

                custom_fields.append(custom_fields_item)

        date_added = d.pop("dateAdded", UNSET)

        date_of_birth = d.pop("dateOfBirth", UNSET)

        date_updated = d.pop("dateUpdated", UNSET)

        dnd = d.pop("dnd", UNSET)

        _dnd_settings = d.pop("dndSettings", UNSET)
        dnd_settings: DndSettingsSchema | Unset
        if isinstance(_dnd_settings, Unset):
            dnd_settings = UNSET
        else:
            dnd_settings = DndSettingsSchema.from_dict(_dnd_settings)

        email = d.pop("email", UNSET)

        email_lower_case = d.pop("emailLowerCase", UNSET)

        first_name = d.pop("firstName", UNSET)

        first_name_lower_case = d.pop("firstNameLowerCase", UNSET)

        full_name_lower_case = d.pop("fullNameLowerCase", UNSET)

        id = d.pop("id", UNSET)

        keyword = d.pop("keyword", UNSET)

        last_activity = d.pop("lastActivity", UNSET)

        _last_attribution_source = d.pop("lastAttributionSource", UNSET)
        last_attribution_source: AttributionSource | Unset
        if isinstance(_last_attribution_source, Unset):
            last_attribution_source = UNSET
        else:
            last_attribution_source = AttributionSource.from_dict(_last_attribution_source)

        last_name = d.pop("lastName", UNSET)

        last_name_lower_case = d.pop("lastNameLowerCase", UNSET)

        location_id = d.pop("locationId", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        source = d.pop("source", UNSET)

        ssn = d.pop("ssn", UNSET)

        state = d.pop("state", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        timezone = d.pop("timezone", UNSET)

        type_ = d.pop("type", UNSET)

        visitor_id = d.pop("visitorId", UNSET)

        website = d.pop("website", UNSET)

        get_contect_by_id_schema = cls(
            address1=address1,
            assigned_to=assigned_to,
            attachments=attachments,
            attribution_source=attribution_source,
            business_id=business_id,
            city=city,
            company_name=company_name,
            country=country,
            custom_fields=custom_fields,
            date_added=date_added,
            date_of_birth=date_of_birth,
            date_updated=date_updated,
            dnd=dnd,
            dnd_settings=dnd_settings,
            email=email,
            email_lower_case=email_lower_case,
            first_name=first_name,
            first_name_lower_case=first_name_lower_case,
            full_name_lower_case=full_name_lower_case,
            id=id,
            keyword=keyword,
            last_activity=last_activity,
            last_attribution_source=last_attribution_source,
            last_name=last_name,
            last_name_lower_case=last_name_lower_case,
            location_id=location_id,
            name=name,
            phone=phone,
            postal_code=postal_code,
            source=source,
            ssn=ssn,
            state=state,
            tags=tags,
            timezone=timezone,
            type_=type_,
            visitor_id=visitor_id,
            website=website,
        )

        get_contect_by_id_schema.additional_properties = d
        return get_contect_by_id_schema

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
