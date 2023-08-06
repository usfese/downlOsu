import requests

import info
from config_helper import read_config_from_file


class Downloader:
    down_queue: list
    songs_dir: str
    config = {}

    def __init__(self, down_queue: list, song_dir: str):
        self.down_queue = down_queue
        self.songs_dir = song_dir
        self.config = read_config_from_file()

    def downloadSingle(self, beatmap_data):
        response = requests.get("https://dl.sayobot.cn/beatmaps/download/full/" + beatmap_data["sid"],
                                headers=info.USER_AGENT, timeout=5)
        file_name = self.config["songsDir"] + "/" + beatmap_data["sid"] + " " + beatmap_data["artist"] + " - " + \
                    beatmap_data["title"]
        with open(file_name, "wb") as file:
            file.write(response.content)
