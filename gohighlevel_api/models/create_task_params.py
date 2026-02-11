from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTaskParams")


@_attrs_define
class CreateTaskParams:
    """
    Attributes:
        completed (bool):  Example: True.
        due_date (str):  Example: 2020-10-25T11:00:00Z.
        title (str):  Example: First Task.
        assigned_to (str | Unset):  Example: hxHGVRb1YJUscrCB8eXK.
        body (str | Unset):  Example: loram ipsum.
    """

    completed: bool
    due_date: str
    title: str
    assigned_to: str | Unset = UNSET
    body: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed = self.completed

        due_date = self.due_date

        title = self.title

        assigned_to = self.assigned_to

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completed": completed,
                "dueDate": due_date,
                "title": title,
            }
        )
        if assigned_to is not UNSET:
            field_dict["assignedTo"] = assigned_to
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completed = d.pop("completed")

        due_date = d.pop("dueDate")

        title = d.pop("title")

        assigned_to = d.pop("assignedTo", UNSET)

        body = d.pop("body", UNSET)

        create_task_params = cls(
            completed=completed,
            due_date=due_date,
            title=title,
            assigned_to=assigned_to,
            body=body,
        )

        create_task_params.additional_properties = d
        return create_task_params

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
