from django.test import TestCase
from django.db import models
from django_model_docs.serializers.column_serializers.data_type import (
    DataTypeColumnSerializer,
)


class TestDataTypeColumnSerializer(TestCase):
    def test_handles_CharField(self):
        """Serializes non-nullable field to "False" """

        field = models.CharField()
        serializer = DataTypeColumnSerializer

        self.assertEqual(serializer.markdown(field), "CharField")
