from enum import Enum


class ICustomFieldAcceptedFormats(str, Enum):
    ALL = "all"
    VALUE_0 = ".pdf"
    VALUE_1 = ".docx"
    VALUE_2 = ".doc"
    VALUE_3 = ".jpg"
    VALUE_4 = ".jpeg"
    VALUE_5 = ".png"
    VALUE_6 = ".gif"
    VALUE_7 = ".csv"
    VALUE_8 = ".xlsx"
    VALUE_9 = ".xls"

    def __str__(self) -> str:
        return str(self.value)
