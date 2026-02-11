from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribution_source import AttributionSource
    from ..models.custom_field_schema import CustomFieldSchema


T = TypeVar("T", bound="ContactsSearchSchema")


@_attrs_define
class ContactsSearchSchema:
    """
    Attributes:
        attributions (list[AttributionSource] | Unset):
        business_id (str | Unset):  Example: 641c094001436dbc2081e642.
        country (str | Unset):  Example: DE.
        custom_fields (list[CustomFieldSchema] | Unset):
        date_added (str | Unset):  Example: 2020-10-29T09:31:30.255Z.
        email (str | Unset):  Example: JohnDeo@gmail.com.
        followers (list[str] | Unset):  Example: 641c094001436dbc2081e642.
        id (str | Unset):  Example: ocQHyuzHvysMo5N5VsXc.
        location_id (str | Unset):  Example: C2QujeCh8ZnC7al2InWR.
        source (str | Unset):  Example: xyz form.
        tags (list[str] | Unset):  Example: ['nisi sint commodo amet', 'consequat'].
        timezone (str | Unset):  Example: Asia/Calcutta.
    """

    attributions: list[AttributionSource] | Unset = UNSET
    business_id: str | Unset = UNSET
    country: str | Unset = UNSET
    custom_fields: list[CustomFieldSchema] | Unset = UNSET
    date_added: str | Unset = UNSET
    email: str | Unset = UNSET
    followers: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    location_id: str | Unset = UNSET
    source: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributions, Unset):
            attributions = []
            for attributions_item_data in self.attributions:
                attributions_item = attributions_item_data.to_dict()
                attributions.append(attributions_item)

        business_id = self.business_id

        country = self.country

        custom_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        date_added = self.date_added

        email = self.email

        followers: list[str] | Unset = UNSET
        if not isinstance(self.followers, Unset):
            followers = self.followers

        id = self.id

        location_id = self.location_id

        source = self.source

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributions is not UNSET:
            field_dict["attributions"] = attributions
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if country is not UNSET:
            field_dict["country"] = country
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if date_added is not UNSET:
            field_dict["dateAdded"] = date_added
        if email is not UNSET:
            field_dict["email"] = email
        if followers is not UNSET:
            field_dict["followers"] = followers
        if id is not UNSET:
            field_dict["id"] = id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if source is not UNSET:
            field_dict["source"] = source
        if tags is not UNSET:
            field_dict["tags"] = tags
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribution_source import AttributionSource
        from ..models.custom_field_schema import CustomFieldSchema

        d = dict(src_dict)
        _attributions = d.pop("attributions", UNSET)
        attributions: list[AttributionSource] | Unset = UNSET
        if _attributions is not UNSET:
            attributions = []
            for attributions_item_data in _attributions:
                attributions_item = AttributionSource.from_dict(attributions_item_data)

                attributions.append(attributions_item)

        business_id = d.pop("businessId", UNSET)

        country = d.pop("country", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: list[CustomFieldSchema] | Unset = UNSET
        if _custom_fields is not UNSET:
            custom_fields = []
            for custom_fields_item_data in _custom_fields:
                custom_fields_item = CustomFieldSchema.from_dict(custom_fields_item_data)

                custom_fields.append(custom_fields_item)

        date_added = d.pop("dateAdded", UNSET)

        email = d.pop("email", UNSET)

        followers = cast(list[str], d.pop("followers", UNSET))

        id = d.pop("id", UNSET)

        location_id = d.pop("locationId", UNSET)

        source = d.pop("source", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        timezone = d.pop("timezone", UNSET)

        contacts_search_schema = cls(
            attributions=attributions,
            business_id=business_id,
            country=country,
            custom_fields=custom_fields,
            date_added=date_added,
            email=email,
            followers=followers,
            id=id,
            location_id=location_id,
            source=source,
            tags=tags,
            timezone=timezone,
        )

        contacts_search_schema.additional_properties = d
        return contacts_search_schema

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
