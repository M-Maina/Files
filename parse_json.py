import json

def display_json():
    with open("monster.json") as f:
        content_json = json.load(f)
        print(content_json)    
        
        
        
if __name__ == '__main__ ':
    display_json()