import json
import os
import requests

def main():
        listlist = ['1pm',15,10,20,51]
        json_d = {'BME280': listlist}

        url = 'http://127.0.0.1:5000/database'
    

        requests.post(url, json = json_d)
        
        
        #r = requests.get('http://myserver/emoncms2/api/post', data=payload)
        
        print(type(json_send))
        print(json_send)
        #print(x)

        #path = os.getcwd()
        
        #with open('Databaseupdate.json', 'w') as file:

       #     json_f = json.dumps(json_d)

       #     file.write(json_f)
            
main()