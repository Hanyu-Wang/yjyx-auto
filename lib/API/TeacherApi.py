import requests
from cfg.cfg import g_api_teacher, g_vcode

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888',
}


class STeacher:

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

    # 列出老师

    def teacher_list(self, subjectid=None):
        payloads = {"vcode": g_vcode, "action": "search_with_pagenation"}
        if subjectid is not None:
            payloads["subjectid"] = subjectid
        res = requests.get(g_api_teacher, params=payloads)
        self.print_response(res)
        return res

    # 新增老师

    def add_teacher(self, username, realname, subjectid, classlist, phonenumber, email, idcardnumber):
        payloads = {
            "vcode": g_vcode,
            "action": "add",
            "username": username,
            "realname": realname,
            "subjectid": subjectid,
            "classlist": classlist,
            "phonenumber": phonenumber,
            "email": email,
            "idcardnumber": idcardnumber
        }
        res = requests.post(g_api_teacher, data=payloads)
        self.print_response(res)
        return res

    # 修改老师

    def modify_teacher(self, teacherid, realname, subjectid, classlist, phonenumber, email, idcardnumber):
        url = f'{g_api_teacher}/{teacherid}'
        payloads = {
            "vcode": g_vcode,
            "action": "modify",
            "realname": realname,
            "subjectid": subjectid,
            "classlist": classlist,
            "phonenumber": phonenumber,
            "email": email,
            "idcardnumber": idcardnumber
        }
        res = requests.put(url, data=payloads)
        self.print_response(res)
        return res

    # 删除老师

    def del_teacher(self, teacherid):
        payloads = {"vcode": g_vcode}
        url = f'{g_api_teacher}/{teacherid}'
        res = requests.delete(url, data=payloads)
        self.print_response(res)
        return res

    # 删除全部老师

    def del_teacher_all(self):
        res = self.teacher_list()
        teacherlist = res.json()["retlist"]
        for i in teacherlist:
            self.del_teacher(i["id"])


steacher = STeacher()
