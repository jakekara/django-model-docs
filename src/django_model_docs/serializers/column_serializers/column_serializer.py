from abc import ABC, abstractmethod
from django.db.models.fields import Field


class ColumnSerializer(ABC):

    """
    Serializer to convert a field into a column cell content
    """

    @property
    @abstractmethod
    def name(self):
        return "Data Type"

    @abstractmethod
    def markdown(self, field: Field) -> str:
        return NotImplemented