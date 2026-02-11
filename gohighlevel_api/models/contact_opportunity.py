from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactOpportunity")


@_attrs_define
class ContactOpportunity:
    """
    Attributes:
        id (str):  Example: 1a2b3c4d5e6f7g8h9i0j.
        status (str):  Example: open.
        monetary_value (float | Unset):  Example: 10000.
        pipeline_id (str | Unset):  Example: pipeline123.
        pipeline_stage_id (str | Unset):  Example: stage456.
    """

    id: str
    status: str
    monetary_value: float | Unset = UNSET
    pipeline_id: str | Unset = UNSET
    pipeline_stage_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        monetary_value = self.monetary_value

        pipeline_id = self.pipeline_id

        pipeline_stage_id = self.pipeline_stage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if monetary_value is not UNSET:
            field_dict["monetaryValue"] = monetary_value
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if pipeline_stage_id is not UNSET:
            field_dict["pipelineStageId"] = pipeline_stage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        monetary_value = d.pop("monetaryValue", UNSET)

        pipeline_id = d.pop("pipelineId", UNSET)

        pipeline_stage_id = d.pop("pipelineStageId", UNSET)

        contact_opportunity = cls(
            id=id,
            status=status,
            monetary_value=monetary_value,
            pipeline_id=pipeline_id,
            pipeline_stage_id=pipeline_stage_id,
        )

        contact_opportunity.additional_properties = d
        return contact_opportunity

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
