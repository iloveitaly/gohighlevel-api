from enum import Enum


class GetCustomFieldsByObjectKeyVersion(str, Enum):
    VALUE_0 = "2021-07-28"

    def __str__(self) -> str:
        return str(self.value)
