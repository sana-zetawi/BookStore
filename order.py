from flask import Flask, request, jsonify
import requests
import json


app = Flask(__name__)

@app.route("/purchase/<item_number>",methods=['PUT'])
def purchase(item_number):
    result=requests.get("http://192.168.1.18:4000/decreas/"+str(item_number),data={'amount':1})
    return (result.content)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=7000)