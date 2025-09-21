"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import os 
import csv
import json

INPUTFILE = 'input.csv'
OUTPUTFILE = 'output.json'

def get_file_Data(inputfile):
    if not os.path.exists(inputfile):
        print("File Not Exists")
        return []
    with open(inputfile,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        print(data)
        return data

def save_as_json(data,output):
    with open(output,'w',encoding='utf-8') as file:
        json.dump(data,file,indent=2)
    print(f" Converted {len(data)} records to {output}")
         
def preview_data(data,count=3):
    for row in data[:count]:
        print(json.dumps(row,indent=2)) 
    print("------")
    

def main():
    data = get_file_Data(INPUTFILE)
    if not data:
        return
    
    save_as_json(data,OUTPUTFILE)
    preview_data(data)
    
    
if __name__ == "__main__":
    main()
    
    