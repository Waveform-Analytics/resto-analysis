from typing import Dict, Optional
import pandas as pd

from resto.clerk import get_clerk_users
from resto.supa import get_supabase_users as get_supabase_users
from resto.supa import get_supabase_visits, get_supabase_restaurants


class DataLoader:
    """Handles loading and caching of data from Clerk and Supabase sources."""
    
    def __init__(self):
        self._data_cache: Dict[str, pd.DataFrame] = {}
    
    def _get_from_cache(self, key: str) -> Optional[pd.DataFrame]:
        return self._data_cache.get(key)
    
    def _set_cache(self, key: str, data: pd.DataFrame) -> None:
        self._data_cache[key] = data
    
    def get_users(self, force_reload: bool = False) -> pd.DataFrame:
        """Get merged user data from Clerk and Supabase.
        
        Args:
            force_reload: If True, bypass cache and reload data from sources
        
        Returns:
            pd.DataFrame: Merged DataFrame containing user information with columns:
                - user_id (from Clerk)
                - email (from Clerk)
                - name (from Supabase if exists)
                - phone (from Supabase if exists)
                - created_at (from Supabase if exists)
        """
        if not force_reload:
            cached = self._get_from_cache('users')
            if cached is not None:
                return cached
        
        # Load and merge user data
        clerk_users = get_clerk_users()
        supabase_users = get_supabase_users()
        
        merged_users = pd.merge(
            clerk_users,
            supabase_users,
            left_on="user_id",
            right_on="id",
            how="left",
            suffixes=('_clerk', '_supabase')
        )
        
        # Keep only relevant columns, prioritizing Clerk data for email
        final_columns = {
            'user_id': merged_users['user_id'],
            'email': merged_users['email_clerk'],
            'name': merged_users['name'],
            'phone': merged_users['phone'],
            'created_at': merged_users['created_at']
        }
        
        result = pd.DataFrame(final_columns)
        self._set_cache('users', result)
        return result
    
    def get_visits(self, force_reload: bool = False) -> pd.DataFrame:
        """Get visits data from Supabase.
        
        Args:
            force_reload: If True, bypass cache and reload data from source
        
        Returns:
            pd.DataFrame: DataFrame containing visit information
        """
        if not force_reload:
            cached = self._get_from_cache('visits')
            if cached is not None:
                return cached
        
        result = get_supabase_visits()
        self._set_cache('visits', result)
        return result
    
    def get_restaurants(self, force_reload: bool = False) -> pd.DataFrame:
        """Get restaurants data from Supabase.
        
        Args:
            force_reload: If True, bypass cache and reload data from source
        
        Returns:
            pd.DataFrame: DataFrame containing restaurant information
        """
        if not force_reload:
            cached = self._get_from_cache('restaurants')
            if cached is not None:
                return cached
        
        result = get_supabase_restaurants()
        self._set_cache('restaurants', result)
        return result


# Create a singleton instance for convenience
loader = DataLoader()