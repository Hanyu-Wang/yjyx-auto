import requests
from cfg.cfg import g_vcode, g_api_student


class SStudent:
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

    # 列出学生

    def student_list(self, subjectid=None):
        payloads = {"vcode": g_vcode, "action": "search_with_pagenation"}
        if subjectid is not None:
            payloads["subjectid"] = subjectid
        res = requests.get(g_api_student, params=payloads)
        self.print_response(res)
        return res

    # 新增学生

    def add_student(self, username, realname, gradeid, classid, phonenumber):
        # proxies = {
        #     'http': 'http://127.0.0.1:8888',
        #     'https': 'http://127.0.0.1:8888',
        # }
        payloads = {
            "vcode": g_vcode,
            "action": "add",
            "username": username,
            "realname": realname,
            "gradeid": gradeid,
            "classid": classid,
            "phonenumber": phonenumber,
        }
        res = requests.post(g_api_student, data=payloads)
        self.print_response(res)
        return res

    # 修改学生

    def modify_student(self, studentid, realname, phonenumber):
        url = f'{g_api_student}/{studentid}'
        payloads = {
            "vcode": g_vcode,
            "action": "modify",
            "realname": realname,
            "phonenumber": phonenumber,
        }
        res = requests.put(url, data=payloads)
        self.print_response(res)
        return res

    # 删除学生

    def del_student(self, studentid):
        payloads = {"vcode": g_vcode}
        url = f'{g_api_student}/{studentid}'
        res = requests.delete(url, data=payloads)
        self.print_response(res)
        return res

    # 删除全部老师

    def del_student_all(self):
        res = self.student_list()
        teacherlist = res.json()["retlist"]
        for i in teacherlist:
            self.del_student(i["id"])


sstudent = SStudent()
