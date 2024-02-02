import json
import os
from tqdm import tqdm

inverted_index={}
for file in tqdm(os.listdir('merchants')):
    with open('merchants/'+file, 'r') as f:
        content = json.load(f)

    for pincode in content[file.split('.')[0]]:
        if pincode not in inverted_index.keys():
            inverted_index[pincode] = set()
        inverted_index[pincode].add(file.split('.')[0])


for key in inverted_index.keys():
    with open('pincodes/'+key+'.json', 'w') as f:
        json.dump({key:list(inverted_index[key])}, f)
    