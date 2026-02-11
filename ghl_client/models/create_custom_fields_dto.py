from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_custom_fields_dto_accepted_formats import CreateCustomFieldsDTOAcceptedFormats
from ..models.create_custom_fields_dto_data_type import CreateCustomFieldsDTODataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.option_dto import OptionDTO


T = TypeVar("T", bound="CreateCustomFieldsDTO")


@_attrs_define
class CreateCustomFieldsDTO:
    """
    Attributes:
        data_type (CreateCustomFieldsDTODataType): Type of field that you are trying to create
        field_key (str): Field key. For Custom Object it's formatted as "custom_object.{objectKey}.{fieldKey}".
            "custom_object" is a fixed prefix, "{objectKey}" is your custom object's identifier, and "{fieldKey}" is the
            unique field name within that object. Example: "custom_object.pet.name" for a "name" field in a "pet" custom
            object. Example: custom_object.pet.name.
        location_id (str): Location Id Example: ve9EPM428h8vShlRW1KT.
        object_key (str): The key for your custom object. This key uniquely identifies the custom object. Example:
            "custom_object.pet" for a custom object related to pets. Example: custom_object.pet.
        parent_id (str): ID of the parent folder
        show_in_forms (bool): Whether the field should be shown in forms
        accepted_formats (CreateCustomFieldsDTOAcceptedFormats | Unset): Allowed file formats for uploads. Options
            include: .pdf, .docx, .doc, .jpg, .jpeg, .png, .gif, .csv, .xlsx, .xls, all
        allow_custom_option (bool | Unset): Determines if users can add a custom option value different from the
            predefined options in records for RADIO type fields. A custom value added in one record does not automatically
            become an option and will not appear as an option for other records. Example: True.
        description (str | Unset): Description of the field
        max_file_limit (float | Unset): Maximum file limit for uploads. Applicable only for fields with a data type of
            FILE_UPLOAD. Example: 2.
        name (str | Unset): Field name Example: Name.
        options (list[OptionDTO] | Unset): Options for the field (Optional, valid only for SINGLE_OPTIONS,
            MULTIPLE_OPTIONS, RADIO, CHECKBOX, TEXTBOX_LIST type)
        placeholder (str | Unset): Placeholder text for the field
    """

    data_type: CreateCustomFieldsDTODataType
    field_key: str
    location_id: str
    object_key: str
    parent_id: str
    show_in_forms: bool
    accepted_formats: CreateCustomFieldsDTOAcceptedFormats | Unset = UNSET
    allow_custom_option: bool | Unset = UNSET
    description: str | Unset = UNSET
    max_file_limit: float | Unset = UNSET
    name: str | Unset = UNSET
    options: list[OptionDTO] | Unset = UNSET
    placeholder: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_type = self.data_type.value

        field_key = self.field_key

        location_id = self.location_id

        object_key = self.object_key

        parent_id = self.parent_id

        show_in_forms = self.show_in_forms

        accepted_formats: str | Unset = UNSET
        if not isinstance(self.accepted_formats, Unset):
            accepted_formats = self.accepted_formats.value

        allow_custom_option = self.allow_custom_option

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
                "dataType": data_type,
                "fieldKey": field_key,
                "locationId": location_id,
                "objectKey": object_key,
                "parentId": parent_id,
                "showInForms": show_in_forms,
            }
        )
        if accepted_formats is not UNSET:
            field_dict["acceptedFormats"] = accepted_formats
        if allow_custom_option is not UNSET:
            field_dict["allowCustomOption"] = allow_custom_option
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
        data_type = CreateCustomFieldsDTODataType(d.pop("dataType"))

        field_key = d.pop("fieldKey")

        location_id = d.pop("locationId")

        object_key = d.pop("objectKey")

        parent_id = d.pop("parentId")

        show_in_forms = d.pop("showInForms")

        _accepted_formats = d.pop("acceptedFormats", UNSET)
        accepted_formats: CreateCustomFieldsDTOAcceptedFormats | Unset
        if isinstance(_accepted_formats, Unset):
            accepted_formats = UNSET
        else:
            accepted_formats = CreateCustomFieldsDTOAcceptedFormats(_accepted_formats)

        allow_custom_option = d.pop("allowCustomOption", UNSET)

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

        create_custom_fields_dto = cls(
            data_type=data_type,
            field_key=field_key,
            location_id=location_id,
            object_key=object_key,
            parent_id=parent_id,
            show_in_forms=show_in_forms,
            accepted_formats=accepted_formats,
            allow_custom_option=allow_custom_option,
            description=description,
            max_file_limit=max_file_limit,
            name=name,
            options=options,
            placeholder=placeholder,
        )

        create_custom_fields_dto.additional_properties = d
        return create_custom_fields_dto

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
