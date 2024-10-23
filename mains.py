from flask import Flask,render_template,request

from utils import BengaluruHousePrice

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Bengaluru House Price Prediction')
    return render_template('index.html')

@app.route('/predict_prices',methods=['POST','GET'])

def get_house_prices():
    
    if request.method == 'GET':
        
        print('We are in GET Method')
        
        data = request.form
        
        availability = data[availability]
        area_type = data[area_type]
        location = data[location]
        size = data[size]
        total_sqft = data[total_sqft]
        bath = eval(data[bath])
        balcony = eval(data[balcony])
        
        # availability = request.args.get('availability')
        # area_type = request.args.get('area_type')
        # location = request.args.get('location')
        # size = request.args.get('size')
        # total_sqft = request.args.get('total_sqft')
        # bath = eval(request.args.get('bath'))
        # balcony = eval(request.args.get('balcony'))
        
        house_price = BengaluruHousePrice(area_type,availability,location,size,total_sqft,bath,balcony)
        
        price = house_price.get_predicted_price()
        
        return f'Price of House is Rs {round(price,2)} Lakh /-'


        # return render_template('index.html',prediction=round(price,2))

print('__name__ :',__name__)

if __name__ == '__main__':
    app.run()
