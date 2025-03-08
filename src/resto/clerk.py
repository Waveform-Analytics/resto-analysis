# Synchronous Example
import os
from clerk_backend_api import Clerk

clerk_key = os.getenv("CLERK_SECRET_KEY")

with Clerk(
        bearer_auth=clerk_key,  # Your Clerk secret key here
) as clerk:
    response = clerk.users.list(request={    })

emails = []
user_ids = []
for r in response:
    emails.append(r.email_addresses[0].email_address)
    user_ids.append(r.id)



