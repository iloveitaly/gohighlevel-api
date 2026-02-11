from enum import Enum


class UpdateCustomFieldVersion(str, Enum):
    VALUE_0 = "2021-07-28"

    def __str__(self) -> str:
        return str(self.value)
