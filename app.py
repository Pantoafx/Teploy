import pickle
from flask import Flask, request
app = Flask(__name__)

# @app.route('/')
# def index():
#     data = request.json
#     text = data.get('text', '')
#     sentiment = analyze_sentiment(text)
#     return jsonify({'sentiment': sentiment})

@app.route('/sapa')
def sama_nama():
    args = request.args
    nama = args.get('nama', default='afif')
    job = args.get('jobtitle', default="Data Scienctis")
    return {"status": "success",
            "message":f"Halo{nama},pekerjaaan anda adalah {job}"},200

app.run(debug=True)
