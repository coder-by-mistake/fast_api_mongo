from fastapi import APIRouter
from pydantic import BaseModel
from api.requests import meal_nutration
from api.services import (
    meal_nutration_funcation,
    new_user_servies,
    get_details,
    edit_details
)

from api.requests import(
   user_data
)
mng = APIRouter(prefix="/api")
proj = APIRouter(prefix="/API")

@mng.get("/mng_services/{kid_id}")
def meal_nutration(kid_id : str):
   return meal_nutration_funcation(kid_id)

@proj.post("/new-user")
def new_user(request : user_data ):
   return new_user_servies(request)

@proj.get("/all_data")
def details():
   return get_details()

@proj.put("/update-details/{no}")
def update_details(no: int,request : user_data):
   return edit_details(no, request)