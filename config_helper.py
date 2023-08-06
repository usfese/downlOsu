import json
import os


# 读取配置
def read_config_from_file():
    if os.path.exists("config.json"):
        with open("config.json", "r") as config_file:
            return json.load(config_file)
    else:
        return None


# 写入配置
def write_config(config: dict):
    config_file = open("config.json", "w")
    json.dump(config, config_file)
    config_file.close()

#首次运行时初始化配置文件
def try_init_config():
    with open("config.json", "w") as config_file:
        config = {
            "songsDirectory" : ".",
            "defaultNum" : 10
        }
        write_config(config)