import requests
import json

# 获取天气参数
# 使用API接口即数据接口，输入请求，返回天气情况
# 用的学弟的接口哈哈哈哈
url = "http://apis.juhe.cn/simpleWeather/query" # 路径
#设置参数
params = {
     "city": "长沙",
     "key": "fb44de1e6bee842dd3bf0d60073a8178"
}

def getWeather():
    try:
        response = requests.get(url,params=params).json()
        # 字典的嵌套取值
        obj = response
        print(response)
    except:
        obj = {
            'error_code': 1,
            'reason':'无法连接到网络！请检查网络连接。'
        }
    return obj

# 用于测试结果
print(getWeather())