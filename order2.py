from flask import Flask, request, jsonify
from itertools import cycle
import requests
import json

app = Flask(__name__)
swap=cycle(["http://192.168.1.20:4000","http://192.168.1.20:9000"])

@app.route("/purchase/<item_number>",methods=['PUT'])
def purchase(item_number):
    result=requests.get(next(swap)+"/info/"+str(item_number)) 
    res=json.loads(result.content)
    masage=res[0]['number_of_items']

    if(masage>0):
         result2=requests.put(next(swap)+"/decrease/"+str(item_number),data={'amount': 1})
         result3=requests.put(next(swap)+"/decrease/"+str(item_number),data={'amount':1})
         return(result2.content)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=10000)