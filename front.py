from flask import Flask, request,jsonify
import requests

app = Flask(__name__)

@app.route("/search/<topic>",methods=['GET'])
def search(topic):
    # result=requests.get("http://192.168.136.5:4000/search/"+str(topic))
    result=requests.get("http://127.0.0.1:4000/search/"+str(topic))
    return (result.content)


@app.route("/info/<item_number>",methods=['GET'])
def info(item_number):
    # result=requests.get("http://192.168.136.5:4000/info/"+str(item_number))
    result=requests.get("http://127.0.0.1:4000/info/"+str(item_number))
    return (result.content)


@app.route("/update_price/<item_number>",methods=['PUT'])
def update(item_number):
    # result=requests.put("http://192.168.136.5:4000/update_price/"+str(item_number),data={'price':request.json['price']})
    result=requests.put("http://127.0.0.1:4000/update_price/"+str(item_number),data={'price':request.json['price']})
    return (result.content)


@app.route("/increase/<item_number>",methods=['PUT'])
def increase(item_number):
    # result=requests.put("http://192.168.136.5:4000/increase/"+str(item_number),data={'amount':request.json['amount']})
    result=requests.put("http://127.0.0.1:4000/increase/"+str(item_number),data={'amount':request.json['amount']})
    return (result.content)

@app.route("/decrease/<item_number>",methods=['PUT'])
def decrease(item_number):
    # result=requests.put("http://192.168.136.5:4000/increase/"+str(item_number),data={'amount':request.json['amount']})
    result=requests.put("http://127.0.0.1:4000/decrease/"+str(item_number),data={'amount':request.json['amount']})
    return (result.content)

@app.route("/purchase/<item_number>",methods=['PUT'])
def purchase(item_number):
    # result=requests.put("http://192.168.136.4:7000/purchase/"+str(item_number))
    result=requests.put("http://127.0.0.1:7000/purchase/"+str(item_number))
    return (result.content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
