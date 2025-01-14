from mongoengine import Document
from datetime import datetime
from mongoengine import (
    ObjectIdField,
    StringField,
    ListField,
    DateTimeField,
    IntField
)
class MealNutrition(Document):
    kid_id = ObjectIdField()
    meal_type = StringField()
    meal_options = ListField()
    meal_date = DateTimeField()
    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)

    meta = {"collection": "meal_nutritions"}


class user(Document):
    name = StringField()
    number = IntField()
    doc_no = StringField()
    typ = StringField()
    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)