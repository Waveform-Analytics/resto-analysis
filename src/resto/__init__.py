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
               Supported tables: 'users', 'visits', 'restaurants'
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
    # Always initialize configuration, using provided credentials or None
    init_config(
        clerk_secret_key=clerk_secret_key,
        supabase_url=supabase_url,
        supabase_key=supabase_key
    )
    
    # Convert single table to list for consistent processing
    if isinstance(tables, str):
        tables = [tables]
    
    results = {}
    
    valid_tables = {'users', 'visits', 'restaurants'}
    unknown_tables = set(tables) - valid_tables
    if unknown_tables:
        raise ValueError(f"Unknown table(s): {', '.join(unknown_tables)}. Valid tables are: {', '.join(valid_tables)}")
    
    for table in tables:
        if table == 'users':
            results[table] = loader.get_users(force_reload=True)
        elif table == 'visits':
            results[table] = loader.get_visits(force_reload=True)
        elif table == 'restaurants':
            results[table] = loader.get_restaurants(force_reload=True)
    
    # Return single DataFrame if only one table requested
    if len(tables) == 1:
        return results[tables[0]]
    
    return results