from flask import Flask, jsonify
from SystemMetrics import SystemMetrics
import os
from files_data import SaveData

app = Flask(__name__)

@app.route('/', methods=['GET'])
def system_metrics():
    return jsonify({'system_metrics': metrics.system_metrics()})


@app.route('/cpu/times', methods=['GET'])
def get_cpu_times_metrics():

    return jsonify({'cpu_time': metrics.cpu_times()})


@app.route('/cpu/usage', methods=['GET'])
def get_cpu_usage_metrics():

    return jsonify({'cpu_usage': metrics.cpu_usage()})


@app.route('/cpu', methods=['GET'])
def get_cpu_metrics():

    return jsonify({'cpu': metrics.cpu_aggregate()})


@app.route('/memory/virtual_memory', methods=['GET'])
def get_memory_virtual_memory():

    return jsonify({'virtual_memory': metrics.memory_virtual()})


@app.route('/memory/swap_memory', methods=['GET'])
def get_memory_swap_memory():

    return jsonify({'swap_memory': metrics.swap_memory()})


@app.route('/memory/memory_partitions', methods=['GET'])
def get_memory_partitions():

    return jsonify({'memory_partitions': metrics.memory_partitions()})


@app.route('/memory', methods=['GET'])
def get_memory_metrics():

    return jsonify({'memory_metrics': metrics.memory_aggregate()})


@app.route('/disk', methods=['GET'])
def get_disk_metrics():

    return jsonify({'disk_metrics': metrics.memory_partitions()})


@app.before_first_request
def create():
    global metrics, sd

    metrics = SystemMetrics()
    sd = SaveData()
    base_dir = os.path.dirname(os.path.realpath(__file__))
    sd.create_base_folder(base_dir)

if __name__ == '__main__':
    app.run()
