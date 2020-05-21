import requests
from cfg.cfg import g_api_class, g_vcode


class SClass:
    def print_response(self, response):
        print("\n\n-------- HTTP response * begin -------")
        print(response.status_code)

        for k, v in response.headers.items():
            print(f"{k}: {v}")

        print("")

        print(response.content.decode("utf8"))
        try:
            response.json()
        except Exception:
            print("消息体不是json格式！！")
        print("-------- HTTP response * end -------\n\n")

    # 列出班级

    def class_list(self, gradeid=None):
        payloads = {"vcode": g_vcode, "action": "list_classes_by_schoolgrade"}
        if gradeid is not None:
            payloads["gradeid"] = gradeid
        res = requests.get(g_api_class, params=payloads)
        self.print_response(res)
        return res

    # 新增班级

    def add_class(self, grade, name, studentlimit):
        # proxies = {
        #     'http': 'http://127.0.0.1:8888',
        #     'https': 'http://127.0.0.1:8888',
        # }
        payloads = {
            "vcode": g_vcode,
            "action": "add",
            "grade": grade,
            "name": name,
            "studentlimit": studentlimit,
        }
        res = requests.post(g_api_class, data=payloads)
        self.print_response(res)
        return res

    # 修改班级

    def modify_class(self, classid, name, studentlimit):
        url = f'{g_api_class}/{classid}'
        payloads = {
            "vcode": g_vcode,
            "action": "modify",
            "name": name,
            "studentlimit": studentlimit,
        }
        res = requests.put(url, data=payloads)
        self.print_response(res)
        return res

    # 删除班级

    def del_class(self, classid):
        payloads = {"vcode": g_vcode}
        url = f'{g_api_class}/{classid}'
        res = requests.delete(url, data=payloads)
        self.print_response(res)
        return res

    # 删除全部班级

    def del_class_all(self):
        res = self.class_list()
        classlist = res.json()["retlist"]
        for i in classlist:
            self.del_class(i["id"])


sclass = SClass()
