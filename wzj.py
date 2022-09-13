import requests
import json
import time
openId = 'b405c3c7eff166d1de5ce62a2b7454e6' #openId
lat = 30.508898 #维度
lon = 114.407159 #经度
def getCourse():
    headers = {'Host' : 'v18.teachermate.cn','Accept' : '*/*','openId': openId,'Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-CN,zh-Hans;q=0.9','content-type': 'application/json','Origin' : 'https://v18.teachermate.cn','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b35) NetType/WIFI Language/zh_CN','Connection': 'keep-alive','Referer': 'https://v18.teachermate.cn/wechat-pro-ssr/student/sign/list/1198612'}
    url = 'https://v18.teachermate.cn/wechat-api/v1/class-attendance/student/active_signs'
    response = requests.get(url=url,
                                headers=headers
                            )
    res = response.json()
    if(len(json.dumps(res)) == 2): return (-1,-1)
    courseId = res[0]['courseId']
    signId = res[0]['signId']
    print((courseId,signId))
    return (courseId,signId)
def wzj():
    courseId,signId =(-1,-1)
    while (1):
        courseId,signId = getCourse()
        if(courseId == -1): 
            print("暂未开启签到...")
            time.sleep(10);
        else: break
    time.sleep(10);
    headers = {'Host' : 'v18.teachermate.cn','Accept' : '*/*','openId': openId,'Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-CN,zh-Hans;q=0.9','content-type': 'application/json','Origin' : 'https://v18.teachermate.cn','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b35) NetType/WIFI Language/zh_CN','Connection': 'keep-alive','Referer': 'https://v18.teachermate.cn/wechat-pro-ssr/student/sign/list/1198612','Content-Length' : '87'}
    url = 'https://v18.teachermate.cn/wechat-api/v1/class-attendance/student-sign-in'
    response = requests.post(url=url,
                                data=json.dumps({
                                    "signId":signId,"lat":lat,"courseId":courseId,"lon":lon
                                },sort_keys=True, indent=4, separators=(',', ': ')),
                                headers=headers,
                                )
    res = response.json()
    # print('签到成功!')
    print(res)

if __name__ == '__main__':
    wzj()
