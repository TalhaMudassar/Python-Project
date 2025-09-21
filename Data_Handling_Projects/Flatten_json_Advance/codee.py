import json
import os
 
INPUTFILE = "nested_data.json"
OUTPUTFILE = "flatted_data.json"

def flatten_json(data, parent_key='', sep='.'):
    items = {}
    
    if isinstance(data, dict): 
        for k, v in data.items():
            full_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.update(flatten_json(v, full_key, sep=sep))
            
    elif isinstance(data, list):  
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key, sep=sep))

    
    else:  
        items[parent_key] = data
        
    return items


def main():
    if not os.path.exists(INPUTFILE):
        print("No input file exists")
        return
    
    try:
        with open(INPUTFILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            
        sep = input("Enter your separator (like . or -): ").strip() or '.'
        
        flattened = flatten_json(data, sep=sep)
        
        with open(OUTPUTFILE, "w", encoding="utf-8") as file:
            json.dump(flattened, file, indent=2)
            
        print(f"Flattened JSON saved to {OUTPUTFILE}")
    
    except Exception as e:
        print("Failed to flatten the data:", e)
        
        
if __name__ == "__main__":
    main()
