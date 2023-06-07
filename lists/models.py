from django.test import TestCase
from lists.models import Item, List

class ListAndItemModelsTest(TestCase):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)