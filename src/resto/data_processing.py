from typing import Dict
import pandas as pd

from src.resto.clerk import get_clerk_users
from src.resto.supa import get_users as get_supabase_users
from src.resto.supa import get_visits, get_restaurants


def load_all_data() -> Dict[str, pd.DataFrame]:
    """Load all data from Clerk and Supabase sources.
    
    Returns:
        Dict[str, pd.DataFrame]: Dictionary containing the following DataFrames:
            - clerk_users: User data from Clerk
            - supabase_users: User data from Supabase
            - visits: Visit data from Supabase
            - restaurants: Restaurant data from Supabase
    """
    # Load data from both sources
    clerk_users_df = get_clerk_users()
    supabase_users_df = get_supabase_users()
    visits_df = get_visits()
    restaurants_df = get_restaurants()
    
    return {
        "clerk_users": clerk_users_df,
        "supabase_users": supabase_users_df,
        "visits": visits_df,
        "restaurants": restaurants_df
    }


def get_merged_user_data() -> pd.DataFrame:
    """Load and merge user data from both Clerk and Supabase.
    Prioritizes Clerk user data and only includes additional fields from Supabase
    if they exist.
    
    Returns:
        pd.DataFrame: Merged DataFrame containing user information with columns:
            - user_id (from Clerk)
            - email (from Clerk)
            - name (from Supabase if exists)
            - phone (from Supabase if exists)
            - created_at (from Supabase if exists)
    """
    data = load_all_data()
    
    # Merge Clerk and Supabase user data on their respective ID fields
    merged_users = pd.merge(
        data["clerk_users"],
        data["supabase_users"],
        left_on="user_id",
        right_on="id",
        how="left",  # Keep all Clerk users, only matching Supabase data
        suffixes=('_clerk', '_supabase')
    )
    
    # Keep only relevant columns, prioritizing Clerk data for email
    final_columns = {
        'user_id': merged_users['user_id'],  # From Clerk
        'email': merged_users['email_clerk'],  # From Clerk
        'name': merged_users['name'],  # From Supabase
        'phone': merged_users['phone'],  # From Supabase
        'created_at': merged_users['created_at']  # From Supabase
    }
    
    return pd.DataFrame(final_columns)