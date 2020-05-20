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
            payloads["gradeid"] = {"gradeid": gradeid}
        res = requests.get(g_api_class, params=payloads)
        self.print_response(res)
        return res

    # 新增班级

    def add_class(self, vcode, action, grade, name, studentlimit):
        payloads = {
            "vcode": g_vcode,
            "action": "add",
            "grade": grade,
            "name": name,
            "studentlimit": studentlimit,
        }
        res = requests.post(g_api_class, json=payloads)
        self.print_response(res)
        return res

    # 修改班级

    def modify_class(self, classid, vcode, action, name, studentlimit):
        payloads = {
            "classid": classid,
            "vcode": g_vcode,
            "action": "add",
            "name": name,
            "studentlimit": studentlimit,
        }
        res = requests.put(g_api_class, json=payloads)
        self.print_response(res)
        return res

    # 删除班级

    def del_class(self, classid, vcode):
        payloads = {"classid": classid, "vcode": g_vcode}
        res = requests.delete(g_api_class, json=payloads)
        self.print_response(res)
        return res

    # 删除全部班级

    def del_all(self):
        res = self.class_list()
        theList = res.json()["retlist"]
        for i in theList:
            self.del_class(i["id"], g_vcode)


sclass = SClass()
