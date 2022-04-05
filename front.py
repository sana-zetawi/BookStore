from flask import Flask, request,jsonify
import requests

app = Flask(__name__)

@app.route("/search/<topic>",methods=['GET'])
def search(topic):
    # result=requests.get("http://192.168.136.5:5000/search/"+str(topic))
    result=requests.get("http://192.168.1.18:4000/search/"+str(topic))
    return (result.content)


@app.route("/info/<int:item_number>",methods=['GET'])
def info(item_number):
    # result=requests.get("http://192.168.136.5:5000/info/"+str(item_number))
    result=requests.get("http://192.168.1.18:4000/info/"+str(item_number))
    return (result.content)


@app.route("/update_price/<int:item_number>",methods=['PUT'])
def update(item_number):
    # result=requests.put("http://192.168.136.5:5000/update_price/"+str(item_number),data={'price':request.json['price']})
    result=requests.put("http://192.168.1.18:4000/update_price/"+str(item_number),data={'price':request.json['price']})
    return (result.content)


@app.route("/increase/<int:item_number>",methods=['PUT'])
def increase(item_number):
    # result=requests.put("http://192.168.136.5:5000/increase/"+str(item_number),data={'amount':request.json['amount']})
    result=requests.put("http://192.168.1.18:4000/increase/"+str(item_number),data={'amount':request.json['amount']})
    return (result.content)

@app.route("/decrease/<int:item_number>",methods=['PUT'])
def decrease(item_number):
    # result=requests.put("http://192.168.136.5:5000/decreas/"+str(item_number),data={'amount':request.json['amount']})
    result=requests.put("http://192.168.1.18:4000/decreas/"+str(item_number),data={'amount':request.json['amount']})
    return (result.content)

@app.route("/purchase/<int:item_number>",methods=['PUT'])
def purchase(item_number):
    # result=requests.put("http://192.168.136.4:5000/purchase/"+str(item_number))
    result=requests.put("http://192.168.1.18:7000/purchase/"+str(item_number))
    return (result.content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
