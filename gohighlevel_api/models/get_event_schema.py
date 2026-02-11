from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetEventSchema")


@_attrs_define
class GetEventSchema:
    """
    Attributes:
        address (str | Unset):  Example: Address.
        appointment_status (str | Unset):  Example: booked.
        assigned_resources (list[str] | Unset):  Example: ['YlWd2wuCAZQzh2cH1fVZ', 'YlWd2wuCAZQzh2cH1fVZ'].
        assigned_user_id (str | Unset):  Example: YlWd2wuCAZQzh2cH1fVZ.
        calendar_id (str | Unset):  Example: YlWd2wuCAZQzh2cH1fVZ.
        contact_id (str | Unset):  Example: YlWd2wuCAZQzh2cH1fVZ.
        date_added (str | Unset):  Example: 2021-07-16 11:00:00.
        date_updated (str | Unset):  Example: 2021-07-16 11:30:00.
        end_time (str | Unset):  Example: 2021-07-16 11:30:00.
        group_id (str | Unset):  Example: YlWd2wuCAZQzh2cH1fVZ.
        id (str | Unset):  Example: YS3jaqqeehkR2Is80miy.
        location_id (str | Unset):  Example: YlWd2wuCAZQzh2cH1fVZ.
        notes (str | Unset):  Example: test.
        start_time (str | Unset):  Example: 2021-07-16 11:00:00.
        status (str | Unset):  Example: booked.
        title (str | Unset):  Example: Test.
        users (list[str] | Unset):  Example: ['YlWd2wuCAZQzh2cH1fVZ', 'YlWd2wuCAZQzh2cH1fVZ'].
    """

    address: str | Unset = UNSET
    appointment_status: str | Unset = UNSET
    assigned_resources: list[str] | Unset = UNSET
    assigned_user_id: str | Unset = UNSET
    calendar_id: str | Unset = UNSET
    contact_id: str | Unset = UNSET
    date_added: str | Unset = UNSET
    date_updated: str | Unset = UNSET
    end_time: str | Unset = UNSET
    group_id: str | Unset = UNSET
    id: str | Unset = UNSET
    location_id: str | Unset = UNSET
    notes: str | Unset = UNSET
    start_time: str | Unset = UNSET
    status: str | Unset = UNSET
    title: str | Unset = UNSET
    users: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        appointment_status = self.appointment_status

        assigned_resources: list[str] | Unset = UNSET
        if not isinstance(self.assigned_resources, Unset):
            assigned_resources = self.assigned_resources

        assigned_user_id = self.assigned_user_id

        calendar_id = self.calendar_id

        contact_id = self.contact_id

        date_added = self.date_added

        date_updated = self.date_updated

        end_time = self.end_time

        group_id = self.group_id

        id = self.id

        location_id = self.location_id

        notes = self.notes

        start_time = self.start_time

        status = self.status

        title = self.title

        users: list[str] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if appointment_status is not UNSET:
            field_dict["appointmentStatus"] = appointment_status
        if assigned_resources is not UNSET:
            field_dict["assignedResources"] = assigned_resources
        if assigned_user_id is not UNSET:
            field_dict["assignedUserId"] = assigned_user_id
        if calendar_id is not UNSET:
            field_dict["calendarId"] = calendar_id
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if date_added is not UNSET:
            field_dict["dateAdded"] = date_added
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        appointment_status = d.pop("appointmentStatus", UNSET)

        assigned_resources = cast(list[str], d.pop("assignedResources", UNSET))

        assigned_user_id = d.pop("assignedUserId", UNSET)

        calendar_id = d.pop("calendarId", UNSET)

        contact_id = d.pop("contactId", UNSET)

        date_added = d.pop("dateAdded", UNSET)

        date_updated = d.pop("dateUpdated", UNSET)

        end_time = d.pop("endTime", UNSET)

        group_id = d.pop("groupId", UNSET)

        id = d.pop("id", UNSET)

        location_id = d.pop("locationId", UNSET)

        notes = d.pop("notes", UNSET)

        start_time = d.pop("startTime", UNSET)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        users = cast(list[str], d.pop("users", UNSET))

        get_event_schema = cls(
            address=address,
            appointment_status=appointment_status,
            assigned_resources=assigned_resources,
            assigned_user_id=assigned_user_id,
            calendar_id=calendar_id,
            contact_id=contact_id,
            date_added=date_added,
            date_updated=date_updated,
            end_time=end_time,
            group_id=group_id,
            id=id,
            location_id=location_id,
            notes=notes,
            start_time=start_time,
            status=status,
            title=title,
            users=users,
        )

        get_event_schema.additional_properties = d
        return get_event_schema

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
