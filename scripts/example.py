"""Example script demonstrating how to use the resto package."""

from resto import get_data, init_config

# Initialize config with your API keys
# You can also set these via environment variables
init_config(
    clerk_secret_key=None,  # Optional if set via env var
    supabase_url=None,          # Optional if set via env var
    supabase_key=None           # Optional if set via env var
)

# Get user data
users_df = get_data('users')
print("\nUser Data:")
print(users_df.head())

# You can also get multiple tables at once
all_data = get_data(['users'])
print("\nAll Data (dictionary of DataFrames):")
for table_name, df in all_data.items():
    print(f"\n{table_name} table:")
    print(df.head())
