from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name_give']
    ordercount = request.form['ordercount_give']
    orderadress = request.form['orderaddress_give']
    orderphone = request.form['orderphone_give']

    print(name, ordercount, orderadress, orderphone)

    order = {
        'name': name,
        'count': ordercount,
        'address': orderadress,
        'phone': orderphone,
    }
    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '저장성공!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():

    read_orders = list(db.orders.find({},{'_id': False}))

# 여길 채워나가세요!
    return jsonify({'result': 'success', 'orders_data': read_orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)