from enum import Enum


class CreateAssociationType(str, Enum):
    ADD = "add"
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
