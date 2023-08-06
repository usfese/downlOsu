#读取配置
def read_config_from_file():
    if os.path.exists("config.json"):
        try :
            config_file = open("config.json", "r")
            config = json.load(config_file)
        except :
            config = None
        finally:
            config_file.close()
            return config
    else :
        return None
#写入配置
def write_config(config : str):
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