from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskSchema")


@_attrs_define
class TaskSchema:
    """
    Attributes:
        assigned_to (str | Unset):  Example: tesTUcmRxWrjqzJS8EjkxNKting.
        body (str | Unset):  Example: testing.
        completed (bool | Unset):  Example: True.
        contact_id (str | Unset):  Example: lJpzYrWdpkC2hX6t2yue.
        due_date (str | Unset):  Example: 2021-07-08T02:30:00.000Z.
        id (str | Unset):  Example: lJpzYrWdpkC2hX6t2yue.
        title (str | Unset):  Example: test.
    """

    assigned_to: str | Unset = UNSET
    body: str | Unset = UNSET
    completed: bool | Unset = UNSET
    contact_id: str | Unset = UNSET
    due_date: str | Unset = UNSET
    id: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_to = self.assigned_to

        body = self.body

        completed = self.completed

        contact_id = self.contact_id

        due_date = self.due_date

        id = self.id

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if body is not UNSET:
            field_dict["body"] = body
        if completed is not UNSET:
            field_dict["completed"] = completed
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assigned_to = d.pop("assignedTo", UNSET)

        body = d.pop("body", UNSET)

        completed = d.pop("completed", UNSET)

        contact_id = d.pop("contactId", UNSET)

        due_date = d.pop("dueDate", UNSET)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        task_schema = cls(
            assigned_to=assigned_to,
            body=body,
            completed=completed,
            contact_id=contact_id,
            due_date=due_date,
            id=id,
            title=title,
        )

        task_schema.additional_properties = d
        return task_schema

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
