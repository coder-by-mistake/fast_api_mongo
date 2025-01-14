from pydantic import BaseModel

class meal_nutration(BaseModel):
    Kid_id : str

class user_data(BaseModel):
    name : str
    number : int
    doc_no : str
    typ : str