from flask import Flask, jsonify
from SystemMetrics import SystemMetrics
import os
from files_data import SaveData

app = Flask(__name__)


@app.route('/', methods=['GET'])
def system_metrics_():
    data = sd.save_data(base_dir)
    return jsonify({'system_metrics': data})


@app.route('/<string:date_>', methods=['GET'])
def system_metrics_date(date_):
    data = sd.get_data(base_dir, date_)
    return jsonify({'system_metrics': data})


@app.route('/<string:date_>/<string:time_>', methods=['GET'])
def system_metrics_date_time(date_, time_):
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'system_metrics': data})


@app.route('/cpu/times', methods=['GET'])
def get_cpu_times_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'cpu_time': data['cpu']['cpu_times']})


# ends points based on date
@app.route('/cpu/times/<string:date_>', methods=['GET'])
def get_cpu_times_date_metrics(date_):
    date_ = str(date_)
    data = sd.get_data(base_dir, date_)
    return jsonify({'cpu_time': data['cpu']['cpu_times']})


# ends points based on date
@app.route('/cpu/times/<string:date_>/<string:time_>', methods=['GET'])
def get_cpu_times_date_time_metrics(date_, time_):
    date_ = str(date_)
    time_ = str(time_)
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'cpu_time': data['cpu']['cpu_times']})


@app.route('/cpu/usage', methods=['GET'])
def get_cpu_usage_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'cpu_usage': data['cpu']['cpu_usage']})


# ends points based on date
@app.route('/cpu/usage/<string:date_>', methods=['GET'])
def get_cpu_usage_date_metrics(date_):
    date_ = str(date_)
    data = sd.get_data(base_dir, date_)
    return jsonify({'cpu_usage': data['cpu']['cpu_usage']})


# ends points based on date
@app.route('/cpu/usage/<string:date_>/<string:time_>', methods=['GET'])
def get_cpu_usage_date_time_metrics(date_, time_):
    date_ = str(date_)
    time_ = str(time_)
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'cpu_usage': data['cpu']['cpu_usage']})


@app.route('/cpu', methods=['GET'])
def get_cpu_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'cpu': data['cpu']})


# ends points based on date
@app.route('/cpu/<string:date_>', methods=['GET'])
def get_cpu_date_metrics(date_):
    data = sd.get_data(base_dir, date_)
    return jsonify({'cpu': data['cpu']})


@app.route('/cpu/<string:date_>/<string:time_>', methods=['GET'])
def get_cpu_date_time_metrics(date_, time_):
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'cpu': data['cpu']})


@app.route('/memory/virtual_memory', methods=['GET'])
def get_memory_virtual_memory():
    data = sd.save_data(base_dir)
    return jsonify({'virtual_memory': data['memory']['virtual_memory']})


# ends points based on date
@app.route('/memory/virtual_memory/<string:date_>', methods=['GET'])
def get_memory_virtual_date_metrics(date_):
    data = sd.get_data(base_dir, date_)
    return jsonify({'virtual_memory': data['memory']['virtual_memory']})


@app.route('/memory/virtual_memory/<string:date_>/<string:time_>', methods=['GET'])
def get_memory_virtual_date_time_metrics(date_, time_):
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'virtual_memory': data['memory']['virtual_memory']})


@app.route('/memory/swap_memory', methods=['GET'])
def get_memory_swap_memory():
    data = sd.save_data(base_dir)
    return jsonify({'swap_memory': data['memory']['swap_memory']})


# ends points based on date
@app.route('/memory/swap_memory/<string:date_>', methods=['GET'])
def get_memory_swap_date_metrics(date_):
    data = sd.get_data(base_dir, date_)
    return jsonify({'swap_memory': data['memory']['swap_memory']})


@app.route('/memory/swap_memory/<string:date_>/<string:time_>', methods=['GET'])
def get_swap_virtual_date_time_metrics(date_, time_):
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'swap_memory': data['memory']['swap_memory']})


@app.route('/memory', methods=['GET'])
def get_memory_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'memory_metrics': data['memory']})


# ends points based on date
@app.route('/memory/<string:date_>', methods=['GET'])
def get_memory_date_metrics(date_):
    data = sd.get_data(base_dir, date_)
    return jsonify({'memory_metrics': data['memory']})


@app.route('/memory/<string:date_>/<string:time_>', methods=['GET'])
def get_memory_date_time_metrics(date_, time_):
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'memory_metrics': data['memory']})


@app.route('/disk', methods=['GET'])
def get_disk_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'disk_metrics': data["disk"]})


# ends points based on date
@app.route('/disk/<string:date_>', methods=['GET'])
def get_disk_date_metrics(date_):
    date_ = str(date_)
    data = sd.get_data(base_dir, date_)
    return jsonify({'disk_metrics': data["disk"]})


@app.route('/disk/<string:date_>/<string:time_>', methods=['GET'])
def get_disk_date_time_metrics(date_, time_):
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'disk_metrics': data["disk"]})


@app.route('/network', methods=['GET'])
def get_network_metrics():
    data = sd.save_data(base_dir)
    return jsonify({'network_metrics': data["network"]})


# ends points based on date
@app.route('/network/<string:date_>', methods=['GET'])
def get_network_date_metrics(date_):
    data = sd.get_data(base_dir, date_)
    return jsonify({'network_metrics': data["network"]})


@app.route('/network/<string:date_>/<string:time_>', methods=['GET'])
def get_network_date_time_metrics(date_, time_):
    data = sd.get_data_time(base_dir, date_, time_)
    return jsonify({'network_metrics': data["network"]})


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
