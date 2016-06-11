from flask import Flask, jsonify
from SystemMetrics import SystemMetrics

app = Flask(__name__)

metrics = SystemMetrics()


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello World'})


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

if __name__ == '__main__':
    app.run()
