"""Example script demonstrating how to use the resto package."""

from resto import get_data

# Get user data - if you have API keys, you can pass them directly:
# users_df = get_data('users',
#                    clerk_secret_key='your_clerk_key',
#                    supabase_url='your_supabase_url',
#                    supabase_key='your_supabase_key')
#
# Or if you've set environment variables, just call without arguments:
users_df = get_data('users')
print("\nUser Data:")
print(users_df.head())

# You can also get multiple tables at once
all_data = get_data(['users'])
print("\nAll Data (dictionary of DataFrames):")
for table_name, df in all_data.items():
    print(f"\n{table_name} table:")
    print(df.head())
