import os


def search(key):
    for file in os.listdir('pincodes'):
        if int(file.split('.')[0])==key:
            print('Present')
            return
    print('Not Present')

search(524501)




