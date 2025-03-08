import os
from supabase import create_client, Client
import pandas as pd

def get_supabase_client() -> Client:
    """Initialize and return Supabase client."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")
    
    return create_client(url, key)

def get_users() -> pd.DataFrame:
    """Fetch users data from Supabase.
    
    Returns:
        pd.DataFrame: DataFrame containing user information with columns:
            - id
            - created_at
            - name
            - phone
            - email
    """
    supabase = get_supabase_client()
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
    
    return pd.DataFrame(users)

def get_visits() -> pd.DataFrame:
    """Fetch visits data from Supabase.
    
    Returns:
        pd.DataFrame: DataFrame containing visit information with columns:
            - visit_id
            - user_id
            - restaurant_id
            - created_at
    """
    supabase = get_supabase_client()
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
    
    return pd.DataFrame(visits)

def get_restaurants() -> pd.DataFrame:
    """Fetch restaurants data from Supabase.
    
    Returns:
        pd.DataFrame: DataFrame containing restaurant information with columns:
            - id
            - address
            - url
            - code
    """
    supabase = get_supabase_client()
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
    
    return pd.DataFrame(restaurants)
