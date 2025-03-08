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

## Usage

### Available Tables

The package provides access to three main tables:

1. **Users**: Combined user data from Clerk and Supabase
   - `user_id`: Unique identifier (from Clerk)
   - `email`: User's email (from Clerk)
   - `name`: User's name (from Supabase)
   - `phone`: Contact number (from Supabase)
   - `created_at`: Account creation timestamp (from Supabase)

2. **Visits**: Restaurant visit records from Supabase
   - `visit_id`: Unique visit identifier
   - `user_id`: ID of the user who made the visit
   - `restaurant_id`: ID of the visited restaurant
   - `created_at`: Timestamp of the visit

3. **Restaurants**: Restaurant information from Supabase
   - `id`: Unique restaurant identifier
   - `address`: Restaurant's physical address
   - `url`: Restaurant's website URL
   - `code`: Restaurant's unique code

### Basic Usage

```python
from resto import get_data

# Get data from a single table
users_df = get_data('users')
visits_df = get_data('visits')
restaurants_df = get_data('restaurants')

# Get multiple tables at once
all_data = get_data(['users', 'visits', 'restaurants'])
```

### Configuration

The package requires the following credentials:
- Clerk Secret Key (for user authentication)
- Supabase URL and Key (for data storage)

You can provide these credentials in two ways:

#### 1. Environment Variables (Recommended)

Set the following environment variables:

```bash
export CLERK_SECRET_KEY='your_clerk_secret_key'
export SUPABASE_URL='your_supabase_url'
export SUPABASE_KEY='your_supabase_key'
```

#### 2. Direct Configuration

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

### Data Sources

The package integrates data from multiple sources:

- **Clerk**: Primary source for user authentication
  - Source of truth for `user_id` and `email`
  - Complete email data for all users

- **Supabase**: Primary data storage
  - Extended user metadata (name, phone, etc.)
  - Visit and restaurant data
  - User data linked to Clerk via `id` = `user_id`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.