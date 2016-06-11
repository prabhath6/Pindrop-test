import os
from datetime import datetime
from time import gmtime, strftime
import json
from SystemMetrics import SystemMetrics


class SaveData:

    def __init__(self):
        self.metrics = SystemMetrics()

    @staticmethod
    def create_base_folder(base_path):
        os.chdir(base_path)
        if not os.path.exists("metrics_data"):
            os.mkdir("metrics_data")

    @staticmethod
    def add_today(base_path):
        os.chdir(base_path+"/metrics_data")
        date_ = datetime.now().date()
        today_ = date_.strftime('%Y-%m-%d')
        if not os.path.exists(today_):
            os.mkdir(today_)

    def save_data(self, base_path):

        date_ = datetime.now().date()
        today_ = date_.strftime('%Y-%m-%d')
        os.chdir(base_path+"/metrics_data/"+today_)
        time_ = strftime("%H:%M:%S", gmtime())

        whole_data = self.metrics.system_metrics()

        if not os.path.exists(time_):
            with open(time_,'w+') as f:
                f.write(json.dumps(whole_data))
        return whole_data

    @staticmethod
    def get_data(base_path, date_):

        path = base_path + "/" + "metrics_data" + "/" +date_
        os.chdir(path)

        filename = sorted(os.listdir())[-1]

        try:
            f = open(filename)
            data = f.read()
            return json.loads(data)
        except Exception as e:
            return ""

if __name__ == "__main__":
    sd = SaveData()