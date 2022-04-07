from flask import Flask, request, jsonify
import requests
import json


app = Flask(__name__)

@app.route("/purchase/<item_number>",methods=['PUT'])
def purchase(item_number):
    result=requests.put("http://127.0.0.1:4000/decrease/"+str(item_number),data={'amount': 1})
    s=result.json()
    masage=str(s.get('Successful'))

    if(masage =='Decrease The Number Of Items In Stock'):
         result=requests.get("http://127.0.0.1:4000/info/"+str(item_number)) 
         return (result.content)
    
    return("no book in stock")
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=7000)