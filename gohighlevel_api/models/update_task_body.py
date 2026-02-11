from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTaskBody")


@_attrs_define
class UpdateTaskBody:
    """
    Attributes:
        assigned_to (str | Unset):  Example: hxHGVRb1YJUscrCB8eXK.
        body (str | Unset):  Example: loram ipsum.
        completed (bool | Unset):  Example: True.
        due_date (str | Unset):  Example: 2020-10-25T11:00:00Z.
        title (str | Unset):  Example: First Task.
    """

    assigned_to: str | Unset = UNSET
    body: str | Unset = UNSET
    completed: bool | Unset = UNSET
    due_date: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_to = self.assigned_to

        body = self.body

        completed = self.completed

        due_date = self.due_date

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
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assigned_to = d.pop("assignedTo", UNSET)

        body = d.pop("body", UNSET)

        completed = d.pop("completed", UNSET)

        due_date = d.pop("dueDate", UNSET)

        title = d.pop("title", UNSET)

        update_task_body = cls(
            assigned_to=assigned_to,
            body=body,
            completed=completed,
            due_date=due_date,
            title=title,
        )

        update_task_body.additional_properties = d
        return update_task_body

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
