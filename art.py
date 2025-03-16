import urllib.request
import json
import random

def get_met_art():
    # The Metropolitan Museum of Art Collection API
    # Fetches a random artwork with an image from the their collection
    search_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=painting"

    try:
        with urllib.request.urlopen(search_url) as response:
            data = json.loads(response.read().decode())

        if data["total"] > 0:
            object_id = random.choice(data["objectIDs"]) # Chooses a random object ID from the results
            object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"

            try:
                with urllib.request.urlopen(object_url) as response:
                    object_data = json.loads(response.read().decode())
                
                if "primaryImage" in object_data and object_data["primaryImage"]:
                    image_url = object_data["primaryImage"]
                    title = object_data.get('title')
                    artist = object_data.get('artistDisplayName')
                    date = object_data.get('objectDate')

                    print("-----------------------------")
                    print(f"Artwork: {title if title else 'Unknown'}")
                    print(f"Artist: {artist if artist else 'Unknown'}")
                    print(f"Date: {date if date else 'Unknown'}")
                    print(f"Image URL: {image_url}")
                    print("-----------------------------")

                else:
                    print("No image available for this object, please try again.")
            except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
                print(f"Error retrieving artwork details: {e}. Please try again.")
        else:
            print("No objects found, please try again.")
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"Error connecting to Met API: {e}. Please check your internet connection and try again.")
    except json.JSONDecodeError as e:
        print(f"Error processing API response: {e}. The Met API may be experiencing issues.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_met_art()
