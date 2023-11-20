from django.db.models.fields import Field

from .column_serializer import (
    ColumnSerializer,
)


class FieldNameColumnSerializer(ColumnSerializer):
    name = "Field"

    def markdown(field: Field) -> str:
        """Return a string describing a field"""

        return f"`{field.name}`"
