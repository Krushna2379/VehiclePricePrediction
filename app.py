from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd

app = Flask(__name__)


df = pd.read_csv('vehicles.csv')

@app.route('/vehicle')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    min_price = int(request.form['min_price'])
    max_price = int(request.form['max_price'])
    vehicle_type = request.form['vehicle_type']


    filtered_df = df[
        (df['type'].str.lower() == vehicle_type.lower()) &
        (df['price'] >= min_price) & (df['price'] <= max_price)
    ]

    results = filtered_df.to_dict(orient='records')
    return jsonify(results)

@app.route('/download')
def download_csv():
    return send_file('vehicles.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
