# Using the official Supabase Python client
import os
from supabase import create_client
import pandas as pd

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Query users table
users_response = supabase.table("users").select("*").execute().data

users = [
    {
        "id": user["id"],
        "created_at": user["created_at"],
        "name": user["name"],
        "phone": user["phone"],
        "email": user["email"],
    }
    for user in users_response
]

users_df = pd.DataFrame(users)

# Query visits table
visits_response = supabase.table("visits").select(
    "visit_id, user_id, restaurant_id, created_at").execute().data

visits = [
    {
        "visit_id": visit["visit_id"],
        "user_id": visit["user_id"],
        "restaurant_id": visit["restaurant_id"],
        "created_at": visit["created_at"],
    }
    for visit in visits_response
]

visits_df = pd.DataFrame(visits)

# Query restaurants table
restaurants_response = supabase.table("restaurants").select(
    "id, address, url, code").execute().data

restaurants = [
    {
        "id": restaurant["id"],
        "address": restaurant["address"],
        "url": restaurant["url"],
        "code": restaurant["code"],
    }
    for restaurant in restaurants_response
]

restaurants_df = pd.DataFrame(restaurants)
