from enum import Enum


class DndSettingSchemaStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PERMANENT = "permanent"

    def __str__(self) -> str:
        return str(self.value)
