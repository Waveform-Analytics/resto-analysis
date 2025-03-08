# Resto Analysis

A Python package for accessing and analyzing restaurant data, with built-in support for Clerk authentication and Supabase data storage.

## Installation

Install directly from GitHub using pip:

```bash
pip install git+https://github.com/Waveform-Analytics/resto-analysis.git
```

Or if you're using uv:

```bash
uv pip install git+https://github.com/Waveform-Analytics/resto-analysis.git
```

## Configuration

The package requires the following credentials:

- Clerk Secret Key (for user authentication)
- Supabase URL and Key (for additional user data)

You can provide these credentials in two ways:

### 1. Environment Variables

Set the following environment variables:

```bash
export CLERK_SECRET_KEY='your_clerk_secret_key'
export SUPABASE_URL='your_supabase_url'
export SUPABASE_KEY='your_supabase_key'
```

### 2. Direct Configuration

Pass credentials directly when calling functions:

```python
from resto import get_data

df = get_data(
    'users',
    clerk_secret_key='your_clerk_secret_key',
    supabase_url='your_supabase_url',
    supabase_key='your_supabase_key'
)
```

## Usage

### Basic Usage

```python
from resto import get_data

# Get user data (uses environment variables)
users_df = get_data('users')
```

### Data Sources

The `users` table combines data from two sources:

1. **Clerk Users Table**:
   - Primary source of truth for user authentication
   - Contains `user_id` and `email` fields
   - Complete email data for all users

2. **Supabase Users Table**:
   - Contains supplementary user metadata
   - `id` field matches Clerk's `user_id`
   - Additional fields: `name`, `phone`, `created_at`

When fetching user data:
- Data is merged using Clerk as the primary source (left join)
- Email data is always sourced from Clerk
- Additional fields from Supabase are included when available

### Advanced Configuration

```python
from resto import init_config, get_data

# Initialize configuration once
init_config(
    clerk_secret_key='your_clerk_secret_key',
    supabase_url='your_supabase_url',
    supabase_key='your_supabase_key'
)

# Make multiple calls using the same configuration
users_df = get_data('users')
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.