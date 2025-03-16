import urllib.request
import json
import random

def get_met_image():
    # The Metropolitan Museum of Art Collection API
    # Fetches a random artwork with an image from the their collection
    search_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=painting"
    
    with urllib.request.urlopen(search_url) as response:
        data = json.loads(response.read().decode())
    
    if data["total"] > 0:
        # Chooses a random object ID from the search results
        object_id = random.choice(data["objectIDs"])
        
        # Fetches the details of the chosen object
        object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
        with urllib.request.urlopen(object_url) as response:
            object_data = json.loads(response.read().decode())
        
        # Check if the object has an image
        if "primaryImage" in object_data and object_data["primaryImage"]:
            image_url = object_data["primaryImage"]
            title = object_data.get('title', '')
            artist = object_data.get('artistDisplayName', '')
            date = object_data.get('objectDate', '')

            print("-----------------------------")
            print(f"Artwork: {title if title else 'Unknown'}")
            print(f"Artist: {artist if artist else 'Unknown'}")
            print(f"Date: {date if date else 'Unknown'}")
            print(f"Image URL: {image_url}")
            print("-----------------------------")
            return
        else:
            return print("No image available for this object, please try again.")
    else:
        return print ("No objects found, please try again.")

if __name__ == "__main__":
    get_met_image()
