from flask import Flask, request, jsonify,render_template
import functions

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': functions.get_location_names()
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        data = request.form
        print(data)
        total_sqft = float(data['sqft'])
        bhk = int(data['bhk'])
        bath = int(data['bath'])
        location = data['loc']
        print('location,total_sqft,bhk,bath',location,total_sqft,bhk,bath)
        prediction = functions.get_estimated_price(location,total_sqft,bhk,bath)
        return "The Predicted house price is Rs. {} lakhs".format(prediction)
        # return render_template('home.html', prediction_text="The Predicted house price is Rs. {} lakhs".format(prediction))

    return render_template("home.html")

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    # functions.load_saved_artifacts()
    app.run(debug=False)