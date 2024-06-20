import requests

def fetch_asteroids(start_date, end_date, api_key):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
    
    try:
        response = requests.get(url)
        
        data = response.json()
        
        asteroids = []
        for date in data['near_earth_objects']:
            asteroids.extend(data['near_earth_objects'][date])
        
        return asteroids
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    start_date = "2024-06-20"
    end_date = "2024-06-21"
    api_key = "CRjgEmTP1PaDd7S6Qf7NghisiUHnCS4L2OoxFb7Y"  
    
    asteroids = fetch_asteroids(start_date, end_date, api_key)
    
    if asteroids:
        print(f"Number of asteroids found: {len(asteroids)}")
        print("Asteroid details:")
        for asteroid in asteroids:
            print(f"- Name: {asteroid['name']}, Potentially Hazardous: {asteroid['is_potentially_hazardous_asteroid']}")
    else:
        print("Failed to fetch asteroid data.")
