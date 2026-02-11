from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_opportunity import ContactOpportunity
    from ..models.custom_field_schema import CustomFieldSchema
    from ..models.dnd_settings_schema import DndSettingsSchema


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        additional_emails (list[str] | Unset):  Example: ['john@example.com', 'jane@example.com'].
        additional_phones (list[str] | Unset):  Example: ['123456789', '987654321'].
        address (str | Unset):  Example: 123 Main Street.
        assigned_to (str | Unset):  Example: 182goXVW3lIExEQPOnd3.
        business_id (str | Unset):  Example: 282goXVW3lIExEQPOnd3.
        business_name (str | Unset):  Example: Acme Corporation.
        city (str | Unset):  Example: New York.
        company_name (str | Unset):  Example: XYZ Corp.
        country (str | Unset):  Example: United States.
        custom_fields (list[CustomFieldSchema] | Unset):
        date_added (str | Unset):  Example: 2024-06-06T18:54:57.221Z.
        date_of_birth (str | Unset):  Example: 1990-01-01.
        date_updated (str | Unset):  Example: 2024-06-06T18:54:57.221Z.
        dnd (bool | Unset):
        dnd_settings (DndSettingsSchema | Unset):
        email (str | Unset):  Example: john@example.com.
        first_name (str | Unset):  Example: john.
        first_name_lower_case (str | Unset):  Example: john.
        followers (list[str] | Unset):  Example: ['682goXVW3lIExEQPOnd3', '582goXVW3lIExEQPOnd3'].
        id (str | Unset):  Example: 102goXVW3lIExEQPOnd3.
        last_name (str | Unset):  Example: doe.
        last_name_lower_case (str | Unset):  Example: doe.
        location_id (str | Unset):  Example: 502goXVW3lIExEQPOnd3.
        opportunities (list[ContactOpportunity] | Unset):
        phone (str | Unset):  Example: +123456789.
        phone_label (str | Unset):  Example: Mobile.
        postal_code (str | Unset):  Example: 12345.
        search_after (list[str] | Unset):  Example: [1234, '102goXVW3lIExEQPOnd3'].
        source (str | Unset):  Example: Website.
        state (str | Unset):  Example: California.
        tags (list[str] | Unset):  Example: ['tag-1', 'tag-2'].
        type_ (str | Unset):  Example: lead.
        valid_email (bool | Unset):  Example: True.
    """

    additional_emails: list[str] | Unset = UNSET
    additional_phones: list[str] | Unset = UNSET
    address: str | Unset = UNSET
    assigned_to: str | Unset = UNSET
    business_id: str | Unset = UNSET
    business_name: str | Unset = UNSET
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
    first_name: str | Unset = UNSET
    first_name_lower_case: str | Unset = UNSET
    followers: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    last_name: str | Unset = UNSET
    last_name_lower_case: str | Unset = UNSET
    location_id: str | Unset = UNSET
    opportunities: list[ContactOpportunity] | Unset = UNSET
    phone: str | Unset = UNSET
    phone_label: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    search_after: list[str] | Unset = UNSET
    source: str | Unset = UNSET
    state: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    type_: str | Unset = UNSET
    valid_email: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_emails: list[str] | Unset = UNSET
        if not isinstance(self.additional_emails, Unset):
            additional_emails = self.additional_emails

        additional_phones: list[str] | Unset = UNSET
        if not isinstance(self.additional_phones, Unset):
            additional_phones = self.additional_phones

        address = self.address

        assigned_to = self.assigned_to

        business_id = self.business_id

        business_name = self.business_name

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

        first_name = self.first_name

        first_name_lower_case = self.first_name_lower_case

        followers: list[str] | Unset = UNSET
        if not isinstance(self.followers, Unset):
            followers = self.followers

        id = self.id

        last_name = self.last_name

        last_name_lower_case = self.last_name_lower_case

        location_id = self.location_id

        opportunities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.opportunities, Unset):
            opportunities = []
            for opportunities_item_data in self.opportunities:
                opportunities_item = opportunities_item_data.to_dict()
                opportunities.append(opportunities_item)

        phone = self.phone

        phone_label = self.phone_label

        postal_code = self.postal_code

        search_after: list[str] | Unset = UNSET
        if not isinstance(self.search_after, Unset):
            search_after = self.search_after

        source = self.source

        state = self.state

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        type_ = self.type_

        valid_email = self.valid_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_emails is not UNSET:
            field_dict["additionalEmails"] = additional_emails
        if additional_phones is not UNSET:
            field_dict["additionalPhones"] = additional_phones
        if address is not UNSET:
            field_dict["address"] = address
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
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
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if first_name_lower_case is not UNSET:
            field_dict["firstNameLowerCase"] = first_name_lower_case
        if followers is not UNSET:
            field_dict["followers"] = followers
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if last_name_lower_case is not UNSET:
            field_dict["lastNameLowerCase"] = last_name_lower_case
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if opportunities is not UNSET:
            field_dict["opportunities"] = opportunities
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_label is not UNSET:
            field_dict["phoneLabel"] = phone_label
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if search_after is not UNSET:
            field_dict["searchAfter"] = search_after
        if source is not UNSET:
            field_dict["source"] = source
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_
        if valid_email is not UNSET:
            field_dict["validEmail"] = valid_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_opportunity import ContactOpportunity
        from ..models.custom_field_schema import CustomFieldSchema
        from ..models.dnd_settings_schema import DndSettingsSchema

        d = dict(src_dict)
        additional_emails = cast(list[str], d.pop("additionalEmails", UNSET))

        additional_phones = cast(list[str], d.pop("additionalPhones", UNSET))

        address = d.pop("address", UNSET)

        assigned_to = d.pop("assignedTo", UNSET)

        business_id = d.pop("businessId", UNSET)

        business_name = d.pop("businessName", UNSET)

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

        first_name = d.pop("firstName", UNSET)

        first_name_lower_case = d.pop("firstNameLowerCase", UNSET)

        followers = cast(list[str], d.pop("followers", UNSET))

        id = d.pop("id", UNSET)

        last_name = d.pop("lastName", UNSET)

        last_name_lower_case = d.pop("lastNameLowerCase", UNSET)

        location_id = d.pop("locationId", UNSET)

        _opportunities = d.pop("opportunities", UNSET)
        opportunities: list[ContactOpportunity] | Unset = UNSET
        if _opportunities is not UNSET:
            opportunities = []
            for opportunities_item_data in _opportunities:
                opportunities_item = ContactOpportunity.from_dict(opportunities_item_data)

                opportunities.append(opportunities_item)

        phone = d.pop("phone", UNSET)

        phone_label = d.pop("phoneLabel", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        search_after = cast(list[str], d.pop("searchAfter", UNSET))

        source = d.pop("source", UNSET)

        state = d.pop("state", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        type_ = d.pop("type", UNSET)

        valid_email = d.pop("validEmail", UNSET)

        contact = cls(
            additional_emails=additional_emails,
            additional_phones=additional_phones,
            address=address,
            assigned_to=assigned_to,
            business_id=business_id,
            business_name=business_name,
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
            first_name=first_name,
            first_name_lower_case=first_name_lower_case,
            followers=followers,
            id=id,
            last_name=last_name,
            last_name_lower_case=last_name_lower_case,
            location_id=location_id,
            opportunities=opportunities,
            phone=phone,
            phone_label=phone_label,
            postal_code=postal_code,
            search_after=search_after,
            source=source,
            state=state,
            tags=tags,
            type_=type_,
            valid_email=valid_email,
        )

        contact.additional_properties = d
        return contact

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
