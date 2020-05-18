import requests


class APIMgr:
    def class_list(self, gradeid=range(6)):
        response = requests.get('https://192.168.3.21/api/3school/school_classes',
                                params={
                                    'vcode': '00000004074389951477',
                                    'action': 'list_classes_by_schoolgrade',
                                    'gradeid': gradeid,
                                })
        r = response.json()
        print(r)


apimgr = APIMgr()

apimgr.class_list()
