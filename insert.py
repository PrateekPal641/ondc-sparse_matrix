import os
import json
def insert(merchant, pincode):
    for file in os.listdir('merchants'):
        if file.split('.')[0]==merchant:
            with open('merchants/'+file, 'r') as f:
                content = json.load(f)
                f.close()
            print('content before....', content)
            if pincode in content[merchant]:
                print('Already Present')
            else:
                content[merchant].append(pincode)
            print('content after....', content)
            with open('merchants/'+file, 'w') as f:
                json.dump(content, f)

insert('Merchant_3003', 245861)


