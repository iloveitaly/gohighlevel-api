from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_custom_fields_dto_accepted_formats import UpdateCustomFieldsDTOAcceptedFormats
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.option_dto import OptionDTO


T = TypeVar("T", bound="UpdateCustomFieldsDTO")


@_attrs_define
class UpdateCustomFieldsDTO:
    """
    Attributes:
        location_id (str): Location Id Example: ve9EPM428h8vShlRW1KT.
        show_in_forms (bool): Whether the field should be shown in forms
        accepted_formats (UpdateCustomFieldsDTOAcceptedFormats | Unset): Allowed file formats for uploads. Options
            include: .pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all
        description (str | Unset): Description of the field
        max_file_limit (float | Unset): Maximum file limit for uploads. Applicable only for fields with a data type of
            FILE_UPLOAD. Example: 2.
        name (str | Unset): Field name Example: Name.
        options (list[OptionDTO] | Unset): Options for the field. Important: Providing options will completely replace
            the existing options array. You must include all existing options alongside any new options you wish to add.
            Removal of options is not supported through this update. Applicable only for SINGLE_OPTIONS, MULTIPLE_OPTIONS,
            RADIO, CHECKBOX, TEXTBOX_LIST types.
        placeholder (str | Unset): Placeholder text for the field
    """

    location_id: str
    show_in_forms: bool
    accepted_formats: UpdateCustomFieldsDTOAcceptedFormats | Unset = UNSET
    description: str | Unset = UNSET
    max_file_limit: float | Unset = UNSET
    name: str | Unset = UNSET
    options: list[OptionDTO] | Unset = UNSET
    placeholder: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_id = self.location_id

        show_in_forms = self.show_in_forms

        accepted_formats: str | Unset = UNSET
        if not isinstance(self.accepted_formats, Unset):
            accepted_formats = self.accepted_formats.value

        description = self.description

        max_file_limit = self.max_file_limit

        name = self.name

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        placeholder = self.placeholder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locationId": location_id,
                "showInForms": show_in_forms,
            }
        )
        if accepted_formats is not UNSET:
            field_dict["acceptedFormats"] = accepted_formats
        if description is not UNSET:
            field_dict["description"] = description
        if max_file_limit is not UNSET:
            field_dict["maxFileLimit"] = max_file_limit
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.option_dto import OptionDTO

        d = dict(src_dict)
        location_id = d.pop("locationId")

        show_in_forms = d.pop("showInForms")

        _accepted_formats = d.pop("acceptedFormats", UNSET)
        accepted_formats: UpdateCustomFieldsDTOAcceptedFormats | Unset
        if isinstance(_accepted_formats, Unset):
            accepted_formats = UNSET
        else:
            accepted_formats = UpdateCustomFieldsDTOAcceptedFormats(_accepted_formats)

        description = d.pop("description", UNSET)

        max_file_limit = d.pop("maxFileLimit", UNSET)

        name = d.pop("name", UNSET)

        _options = d.pop("options", UNSET)
        options: list[OptionDTO] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = OptionDTO.from_dict(options_item_data)

                options.append(options_item)

        placeholder = d.pop("placeholder", UNSET)

        update_custom_fields_dto = cls(
            location_id=location_id,
            show_in_forms=show_in_forms,
            accepted_formats=accepted_formats,
            description=description,
            max_file_limit=max_file_limit,
            name=name,
            options=options,
            placeholder=placeholder,
        )

        update_custom_fields_dto.additional_properties = d
        return update_custom_fields_dto

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
