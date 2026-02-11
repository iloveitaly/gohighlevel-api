from enum import Enum


class UpdateContactVersion(str, Enum):
    VALUE_0 = "2021-07-28"

    def __str__(self) -> str:
        return str(self.value)
