import requests
from pprint import pprint

def test_parents_api():
    url = "http://127.0.0.1:8000/parents/?format=json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        parents = response.json()
        
        print("\nAPI Response Status:", response.status_code)
        print("Number of parents found:", len(parents))
        print("\nParent Data:")
        
        for parent in parents:
            print(f"\nParent ID: {parent['id']}")
            print(f"Name: {parent['first_name']} {parent['last_name']}")
            print(f"Email: {parent['email']}")
            print(f"Phone: {parent['phone_number']}")
            print(f"Number of children: {len(parent['children'])}")
            
            for child in parent['children']:
                print(f"  - Child: {child['first_name']} {child['last_name']} (Born: {child['birth_date']})")
    
    except requests.exceptions.RequestException as e:
        print(f"\nError making request to {url}")
        print(f"Error: {e}")
    except ValueError as e:
        print("\nError parsing JSON response")
        print(f"Error: {e}")

if __name__ == "__main__":
    test_parents_api()