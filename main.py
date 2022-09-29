import requests
import json

url = "http://api.widget.filtoapp.com/src/category?type=5&language=zh-Hans&devid=8F2BCC85-01D2-42C0-8C9E-8436E7FD2CA4"

response = json.loads(requests.request("GET", url).text)
Data = response["data"]
CategoryList =  []
for i in range(0, len(Data)):
    CategoryName = Data[i]["name"]  # 分类展示名
    # print(CategoryName)
    SourceList = Data[i]["sourceList"]  # 分类下的资源
    for source in SourceList:
        SourceLnk = source["src_path"]
        print(SourceLnk)
