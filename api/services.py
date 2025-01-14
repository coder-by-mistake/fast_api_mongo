import json

from api.models import (
    user,
    MealNutrition
)
def meal_nutration_funcation(kid_id):
    
    try:
        # all_meals = MealNutrition.objects(kid_id = kid_id)
        print("hai bhai",kid_id)
        all_meals = MealNutrition.objects(kid_id =kid_id).limit(1)
        print(all_meals)
        # meals_json = [meal.to_json() for meal in all_meals]
        meals_json = [json.loads(meal.to_json()) for meal in all_meals]
        return {
            "status" : "200",
            "data"  : meals_json
        }
    except Exception as e:
        return {
            "success": False,
            "status": 400,
            "message": f"Generate Vector Error: {e}"
        }
    
def new_user_servies(request):
    try:
        obj = user()
        obj.name = request.name
        obj.number = request.number
        obj.doc_no = request.doc_no
        obj.typ = request.typ
        
        print(type(obj))
        print(obj.name)
        print(obj.number)
        print(obj.typ)
        print(obj.doc_no)
        obj.save()
        return{
            "Status" : True,
            "Status" : 200,
            "Data" : request
        }
    except Exception as e:
        return{
            "Success" : "Faild",
            "status" : f"Generate Vector Error: {e}"
        }
    

def get_details():
    try:
        obj = user.objects()
        obj_json = [json.loads(i.to_json()) for i in obj ]
        return{
            "Status" : True,
            "Status" : 200,
            "Data" : obj_json
        }
    except Exception as e:
        return{
            "Success" : "Faild",
            "status" : f"Generate Vector Error: {e}"
        }
    
def edit_details(number,request):
    try:

        user.objects(number=number).delete()
        
        new_user = user(
            name=request.name,
            number=request.number,
            doc_no=request.doc_no,
            typ=request.typ
        )
        new_user.save()
        
        obj_json = [
            json.loads(user_obj.to_json())
            for user_obj in user.objects(number=request.number)
        ]

        return{
            "status" : "200",
            "message" : "sucess",
            "data" : obj_json
        }
    except Exception as e:
        return{
            "status" : "400",
            "messae" : f"Generated Error: {e}"
        }