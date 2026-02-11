from enum import Enum


class CreateCustomFieldsDTODataType(str, Enum):
    CHECKBOX = "CHECKBOX"
    DATE = "DATE"
    EMAIL = "EMAIL"
    FILE_UPLOAD = "FILE_UPLOAD"
    LARGE_TEXT = "LARGE_TEXT"
    MONETORY = "MONETORY"
    MULTIPLE_OPTIONS = "MULTIPLE_OPTIONS"
    NUMERICAL = "NUMERICAL"
    PHONE = "PHONE"
    RADIO = "RADIO"
    SINGLE_OPTIONS = "SINGLE_OPTIONS"
    TEXT = "TEXT"
    TEXTBOX_LIST = "TEXTBOX_LIST"

    def __str__(self) -> str:
        return str(self.value)
