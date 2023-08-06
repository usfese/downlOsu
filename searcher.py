import json

import requests


class Searcher:
    # 进行post请求的字典，会被解析成json，需要在外部添加或修改参数
    request_dict = None
    # 结果列表
    _result = []

    # 初始化
    def __init__(self, num):
        pass

    # 搜索方法
    def search(self) -> list:
        count = num
        offset = 0
        while count > 0:
            batch_size = min(30, count)
            # 搜索数量限制
            self.request_dict["limit"] = batch_size
            # 搜索偏移
            self.request_dict["offset"] = offset
            response = requests.post("https://api.sayobot.cn/?post", request_dict, timeout=5)
            if response.status_code == 200:
                # 请求成功时将数据加入结果
                json_data = json.loads(response.content)
                self._result += json_data["data"]
                offset = ++json_data["endid"]
            else:
                # 请求失败时跳过
                offset += 30
            # 指针(?)向前移动
            count -= batch_size
        return _result
