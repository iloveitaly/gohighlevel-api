from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_schema import CustomFieldSchema
    from ..models.dnd_settings_schema import DndSettingsSchema


T = TypeVar("T", bound="CreateContactSchema")


@_attrs_define
class CreateContactSchema:
    """
    Attributes:
        address1 (str | Unset):  Example: 3535 1st St N.
        assigned_to (str | Unset): User's Id Example: y0BeYjuRIlDwsDcOHOJo.
        birth_day (float | Unset):  Example: 25.
        birth_month (float | Unset):  Example: 8.
        bounce_email (bool | Unset):
        business_id (str | Unset):  Example: 641c094001436dbc2081e642.
        city (str | Unset):  Example: ruDolomitebika.
        company_name (str | Unset):  Example: DGS VolMAX.
        country (str | Unset):  Example: US.
        custom_fields (list[CustomFieldSchema] | Unset):
        date_added (str | Unset):  Example: 2021-08-31T09:59:41.937Z.
        date_of_birth (str | Unset):  Example: 1990-09-25T00:00:00.000Z.
        date_updated (str | Unset):  Example: 2021-08-31T09:59:41.937Z.
        deleted (bool | Unset):
        dnd (bool | Unset):  Example: True.
        dnd_settings (DndSettingsSchema | Unset):
        email (str | Unset):  Example: rubika@deos.com.
        email_lower_case (str | Unset):  Example: rubika@deos.com.
        first_name (str | Unset):  Example: rubika.
        first_name_lower_case (str | Unset):  Example: rubika.
        full_name_lower_case (str | Unset):  Example: rubika deo.
        id (str | Unset):  Example: seD4PfOuKoVMLkEZqohJ.
        last_name (str | Unset):  Example: Deo.
        last_name_lower_case (str | Unset):  Example: deo.
        last_session_activity_at (str | Unset):  Example: 2021-07-16T11:39:30.564Z.
        location_id (str | Unset):  Example: ve9EPM428h8vShlRW1KT.
        offers (list[str] | Unset):
        phone (str | Unset):  Example: +18832327657.
        postal_code (str | Unset):  Example: 35061.
        products (list[str] | Unset):
        source (str | Unset):  Example: public api.
        state (str | Unset):  Example: AL.
        tags (list[str] | Unset):  Example: ['nisi sint commodo amet', 'consequat'].
        type_ (str | Unset):  Example: read.
        unsubscribe_email (bool | Unset):
        website (str | Unset):  Example: https://www.tesla.com.
    """

    address1: str | Unset = UNSET
    assigned_to: str | Unset = UNSET
    birth_day: float | Unset = UNSET
    birth_month: float | Unset = UNSET
    bounce_email: bool | Unset = UNSET
    business_id: str | Unset = UNSET
    city: str | Unset = UNSET
    company_name: str | Unset = UNSET
    country: str | Unset = UNSET
    custom_fields: list[CustomFieldSchema] | Unset = UNSET
    date_added: str | Unset = UNSET
    date_of_birth: str | Unset = UNSET
    date_updated: str | Unset = UNSET
    deleted: bool | Unset = UNSET
    dnd: bool | Unset = UNSET
    dnd_settings: DndSettingsSchema | Unset = UNSET
    email: str | Unset = UNSET
    email_lower_case: str | Unset = UNSET
    first_name: str | Unset = UNSET
    first_name_lower_case: str | Unset = UNSET
    full_name_lower_case: str | Unset = UNSET
    id: str | Unset = UNSET
    last_name: str | Unset = UNSET
    last_name_lower_case: str | Unset = UNSET
    last_session_activity_at: str | Unset = UNSET
    location_id: str | Unset = UNSET
    offers: list[str] | Unset = UNSET
    phone: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    products: list[str] | Unset = UNSET
    source: str | Unset = UNSET
    state: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    type_: str | Unset = UNSET
    unsubscribe_email: bool | Unset = UNSET
    website: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address1 = self.address1

        assigned_to = self.assigned_to

        birth_day = self.birth_day

        birth_month = self.birth_month

        bounce_email = self.bounce_email

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

        deleted = self.deleted

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

        last_name = self.last_name

        last_name_lower_case = self.last_name_lower_case

        last_session_activity_at = self.last_session_activity_at

        location_id = self.location_id

        offers: list[str] | Unset = UNSET
        if not isinstance(self.offers, Unset):
            offers = self.offers

        phone = self.phone

        postal_code = self.postal_code

        products: list[str] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        source = self.source

        state = self.state

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        type_ = self.type_

        unsubscribe_email = self.unsubscribe_email

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if birth_day is not UNSET:
            field_dict["birthDay"] = birth_day
        if birth_month is not UNSET:
            field_dict["birthMonth"] = birth_month
        if bounce_email is not UNSET:
            field_dict["bounceEmail"] = bounce_email
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
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
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
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if last_name_lower_case is not UNSET:
            field_dict["lastNameLowerCase"] = last_name_lower_case
        if last_session_activity_at is not UNSET:
            field_dict["lastSessionActivityAt"] = last_session_activity_at
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if offers is not UNSET:
            field_dict["offers"] = offers
        if phone is not UNSET:
            field_dict["phone"] = phone
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if products is not UNSET:
            field_dict["products"] = products
        if source is not UNSET:
            field_dict["source"] = source
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unsubscribe_email is not UNSET:
            field_dict["unsubscribeEmail"] = unsubscribe_email
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_schema import CustomFieldSchema
        from ..models.dnd_settings_schema import DndSettingsSchema

        d = dict(src_dict)
        address1 = d.pop("address1", UNSET)

        assigned_to = d.pop("assignedTo", UNSET)

        birth_day = d.pop("birthDay", UNSET)

        birth_month = d.pop("birthMonth", UNSET)

        bounce_email = d.pop("bounceEmail", UNSET)

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

        deleted = d.pop("deleted", UNSET)

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

        last_name = d.pop("lastName", UNSET)

        last_name_lower_case = d.pop("lastNameLowerCase", UNSET)

        last_session_activity_at = d.pop("lastSessionActivityAt", UNSET)

        location_id = d.pop("locationId", UNSET)

        offers = cast(list[str], d.pop("offers", UNSET))

        phone = d.pop("phone", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        products = cast(list[str], d.pop("products", UNSET))

        source = d.pop("source", UNSET)

        state = d.pop("state", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        type_ = d.pop("type", UNSET)

        unsubscribe_email = d.pop("unsubscribeEmail", UNSET)

        website = d.pop("website", UNSET)

        create_contact_schema = cls(
            address1=address1,
            assigned_to=assigned_to,
            birth_day=birth_day,
            birth_month=birth_month,
            bounce_email=bounce_email,
            business_id=business_id,
            city=city,
            company_name=company_name,
            country=country,
            custom_fields=custom_fields,
            date_added=date_added,
            date_of_birth=date_of_birth,
            date_updated=date_updated,
            deleted=deleted,
            dnd=dnd,
            dnd_settings=dnd_settings,
            email=email,
            email_lower_case=email_lower_case,
            first_name=first_name,
            first_name_lower_case=first_name_lower_case,
            full_name_lower_case=full_name_lower_case,
            id=id,
            last_name=last_name,
            last_name_lower_case=last_name_lower_case,
            last_session_activity_at=last_session_activity_at,
            location_id=location_id,
            offers=offers,
            phone=phone,
            postal_code=postal_code,
            products=products,
            source=source,
            state=state,
            tags=tags,
            type_=type_,
            unsubscribe_email=unsubscribe_email,
            website=website,
        )

        create_contact_schema.additional_properties = d
        return create_contact_schema

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
