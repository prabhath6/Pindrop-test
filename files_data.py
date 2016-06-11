import os
from SystemMetrics import SystemMetrics


class SaveData:

    def __init__(self):
        self.metrics = SystemMetrics()

    @staticmethod
    def create_base_folder(base_path):
        os.chdir(base_path)
        if not os.path.exists("metrics_data"):
            os.mkdir("metrics_data")

if __name__ == "__main__":
    sd = SaveData()