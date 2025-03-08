from resto.data_processing import loader

def main():
    # Load all required data
    users_df = loader.get_users()
    visits_df = loader.get_visits()
    restaurants_df = loader.get_restaurants()
    
    # Print basic info about the loaded data
    print(f"\nLoaded data summary:")
    print(f"Users: {len(users_df)} records")
    print(f"Visits: {len(visits_df)} records")
    print(f"Restaurants: {len(restaurants_df)} records")

if __name__ == "__main__":
    main()