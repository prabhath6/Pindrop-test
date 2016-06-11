from flask import Flask, jsonify
from SystemMetrics import SystemMetrics
import os
from files_data import SaveData

app = Flask(__name__)


@app.route('/', methods=['GET'])
def system_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'system_metrics': data})


@app.route('/cpu/times', methods=['GET'])
def get_cpu_times_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'cpu_time': data['cpu']['cpu_time']})


@app.route('/cpu/usage', methods=['GET'])
def get_cpu_usage_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'cpu_usage': data['cpu']['cpu_usage']})


@app.route('/cpu', methods=['GET'])
def get_cpu_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'cpu': data['cpu']})


@app.route('/memory/virtual_memory', methods=['GET'])
def get_memory_virtual_memory():
    data = sd.save_data(base_dir)
    return jsonify({'virtual_memory': data['memory']['virtual_memory']})


@app.route('/memory/swap_memory', methods=['GET'])
def get_memory_swap_memory():
    data = sd.save_data(base_dir)
    return jsonify({'swap_memory': data['memory']['swap_memory']})


@app.route('/memory', methods=['GET'])
def get_memory_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'memory_metrics': data['memory']})


@app.route('/disk', methods=['GET'])
def get_disk_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'disk_metrics': data["disk"]})


@app.before_first_request
def create():
    global metrics, sd, base_dir

    metrics = SystemMetrics()
    sd = SaveData()

    # base dir
    base_dir = os.path.dirname(os.path.realpath(__file__))

    # creating folders
    sd.create_base_folder(base_dir)
    sd.add_today(base_dir)

if __name__ == '__main__':
    app.run()
