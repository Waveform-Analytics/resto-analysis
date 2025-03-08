"""Resto: A package for accessing and analyzing restaurant data."""

from typing import Optional, List, Union
import pandas as pd

from .config import Config, init_config, set_config
from .clerk import get_clerk_users
from .supa import get_supabase_users
from .data_processing import loader

__all__ = [
    'init_config',
    'set_config',
    'get_data',
]


def get_data(
    tables: Union[str, List[str]] = 'users',
    clerk_secret_key: Optional[str] = None,
    supabase_url: Optional[str] = None,
    supabase_key: Optional[str] = None
) -> Union[pd.DataFrame, dict[str, pd.DataFrame]]:
    """Get data from specified tables.
    
    Args:
        tables: String or list of strings specifying which tables to fetch.
               Currently supported: 'users'
        clerk_secret_key: Optional Clerk secret key. If not provided, will use environment variable.
        supabase_url: Optional Supabase URL. If not provided, will use environment variable.
        supabase_key: Optional Supabase key. If not provided, will use environment variable.
    
    Returns:
        If a single table is requested, returns a DataFrame.
        If multiple tables are requested, returns a dict mapping table names to DataFrames.
    
    Raises:
        ValueError: If an invalid table name is provided
        RuntimeError: If configuration is not properly initialized
    """
    # Initialize configuration if credentials provided
    if any([clerk_secret_key, supabase_url, supabase_key]):
        init_config(
            clerk_secret_key=clerk_secret_key,
            supabase_url=supabase_url,
            supabase_key=supabase_key
        )
    
    # Convert single table to list for consistent processing
    if isinstance(tables, str):
        tables = [tables]
    
    results = {}
    
    for table in tables:
        if table == 'users':
            # Get merged user data using DataLoader
            results[table] = loader.get_users(force_reload=True)
        else:
            raise ValueError(f"Unknown table: {table}")
    
    # Return single DataFrame if only one table requested
    if len(tables) == 1:
        return results[tables[0]]
    
    return results