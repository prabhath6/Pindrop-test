import os
from datetime import datetime
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

if __name__ == "__main__":
    sd = SaveData()