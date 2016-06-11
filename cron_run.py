from files_data import SaveData
import os


base_dir = os.path.dirname(os.path.realpath(__file__))
sd = SaveData()

# order of execution for each second
sd.create_base_folder(base_dir)
sd.add_today(base_dir)
sd.save_data(base_dir)
