from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateTagsResponseDTO")


@_attrs_define
class UpdateTagsResponseDTO:
    """
    Attributes:
        error_count (float): Number of errors encountered during the operation
        responses (list[str]): Responses for each contact processed Example: [{'contactId': 'qFSqySFkVvNzOSqgGqFi',
            'message': 'Tags updated', 'oldTags': ['tag-1', 'tag-2'], 'tagsAdded': [], 'tagsRemoved': [], 'type':
            'success'}, {'contactId': 'abcdef', 'message': 'contact id is not a valid firebase id', 'type': 'error'},
            {'contactId': 'qFSqySFkVvNzOSqgGqFi', 'message': 'contact is deleted', 'type': 'error'}, {'contactId':
            '3ualbhnV7j3n3a9r2moD', 'message': 'contact does not belong to location', 'type': 'error'}].
        succeded (bool): Indicates if the operation was successful Example: True.
    """

    error_count: float
    responses: list[str]
    succeded: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_count = self.error_count

        responses = self.responses

        succeded = self.succeded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorCount": error_count,
                "responses": responses,
                "succeded": succeded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_count = d.pop("errorCount")

        responses = cast(list[str], d.pop("responses"))

        succeded = d.pop("succeded")

        update_tags_response_dto = cls(
            error_count=error_count,
            responses=responses,
            succeded=succeded,
        )

        update_tags_response_dto.additional_properties = d
        return update_tags_response_dto

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
