from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
import os
app = Flask(__name__)
riwayat_data = []
@app.route('/')
def index(): return send_from_directory(os.getcwd(), 'index.html')
@app.route('/api/input', methods=['POST'])
def terima_input():
    konten = request.get_json()
    if not konten or 'pesan' not in konten: return jsonify({"status": "gagal"}), 400
    data_baru = {"pesan": konten['pesan'], "waktu": datetime.now().strftime("%H:%M:%S")}
    riwayat_data.append(data_baru)
    return jsonify({"status": "sukses", "diterima": data_baru})
@app.route('/api/data', methods=['GET'])
def kirim_data(): return jsonify(riwayat_data)
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
