from enum import Enum


class LocatorType(Enum):
    ID = "id"
    TEXT = "text"
    XPATH = "xpath"
    CLASS_NAME = "class_name"
    ACCESSIBILITY_ID = "accessibility_id"
    DESCRIPTION = "description"
    RESOURCE_ID = "resource_id"
