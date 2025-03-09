from clerk_backend_api import Clerk
import pandas as pd

from .config import get_config


def get_clerk_users() -> pd.DataFrame:
    """
    Fetch all users data from Clerk and return as a pandas DataFrame.
    Handles pagination to retrieve all users.
    
    Returns:
        pd.DataFrame: DataFrame containing user information with columns:
            - user_id
            - email
            
    Raises:
        RuntimeError: If configuration is not initialized
    """
    config = get_config()
    
    users_data = []
    limit = 100  # Max allowed by Clerk API
    offset = 0
    
    with Clerk(bearer_auth=config.clerk_secret_key) as clerk:
        while True:
            response = clerk.users.list(request={"limit": limit, "offset": offset})
            if not response:
                break
                
            users_data.extend([
                {
                    "user_id": r.id,
                    "email": r.email_addresses[0].email_address if r.email_addresses else None
                }
                for r in response
            ])
            
            if len(response) < limit:
                break
                
            offset += limit
    
    return pd.DataFrame(users_data)

