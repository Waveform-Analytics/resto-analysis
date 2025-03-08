from clerk_backend_api import Clerk
import pandas as pd

from .config import get_config


def get_clerk_users() -> pd.DataFrame:
    """
    Fetch users data from Clerk and return as a pandas DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame containing user information with columns:
            - user_id
            - email
            
    Raises:
        RuntimeError: If configuration is not initialized
    """
    config = get_config()
    
    with Clerk(bearer_auth=config.clerk_secret_key) as clerk:
        response = clerk.users.list(request={})
    
    users_data = [
        {
            "user_id": r.id,
            "email": r.email_addresses[0].email_address if r.email_addresses else None
        }
        for r in response
    ]
    
    return pd.DataFrame(users_data)

