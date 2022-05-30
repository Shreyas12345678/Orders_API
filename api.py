from flask import Flask,jsonify,request
from flask_restful import Resource,Api

app = Flask(__name__)

api=Api(app)

#API structure Given
Orders={
  "order_items": [],
  "distance":0,
  "offer": {}
}


##welcome to our site
@app.route('/')
def home():
  return "Hey Welcome!!!"

#geeting order Items from user
@app.route('/order/orderitems',methods=['POST'])
def order_input():
    req_data=request.get_json()
    new_order_item={
      
      "name": req_data["name"],
      "quantity": req_data["quantity"],
      "price": req_data["price"]
      
      }
    Orders["order_items"].append(new_order_item)
    return jsonify(new_order_item)

      
#getting distance from the user     
@app.route('/order/distance/',methods=['POST'])
def order_distance():
    req_data=request.get_json()
    dis=req_data["distance"]
    
    Orders["distance"]=dis
    return jsonify(dis)


#for getting offer if applicable          
@app.route('/order/offer',methods=['POST'])
def order_offer():
    req_data=request.get_json()
    new_offer={
      "offer_type":req_data["offer_type"],
      "offer_val":req_data["offer_val"]

    }
    Orders["offer"]=new_offer
    return jsonify(new_offer)
    
    
#Total order price
@app.route('/order/total')
def get_fun():
    distance=Orders["distance"]
    total_price=0
    for x in Orders["order_items"]:
      total_price+=x["quantity"]*x["price"]

    if(distance>0 and distance<=10000):
      total_price+=5000
    elif(distance>10000 and distance<=20000):
      total_price+=10000
    elif(distance>20000 and distance<=50000):
      total_price+=50000
    elif(distance>50000):
      total_price+=100000

    Discount=Orders["offer"]["offer_val"]
    Discount=min(Discount,total_price)
    total_price=total_price-Discount
    return {'total':total_price}

#Order details
@app.route('/show_order_details')
def show_order():
  return jsonify(Orders)    


if __name__ == '__main__':
    app.run(debug=True)

