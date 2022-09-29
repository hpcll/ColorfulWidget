import json
import xmltodict

list = []

# 定义xml转json的函数
def xmltojson(xmlstr):
    xmlparse = xmltodict.parse(xmlstr)
    jsonstr = json.dumps(xmlparse, indent=1)
    return jsonstr


f = open('yuan.xml')
data = f.read()
f2 = open('country.json', 'a')
data2 = xmltojson(data)
data3 = data2.encode('utf-8').decode('unicode_escape')
f2.write(data3)
f2.close()



f = open('country.json')
jsondata = json.loads(f.read())
jsondata1 = jsondata["plist"]["dict"]["array"]["dict"]
for i in range(0, len(jsondata1)):
    name = jsondata1[i]["string"][0]
    bundleid = jsondata1[i]["string"][6]
    url = jsondata1[i]["string"][7]
    list.append({"id": name, "name": name, "bundle_id": bundleid, "url": url})
print(list)

f = open("applink.json","w")
c =json.dumps(list)  #无须str()将字典转为字符串
f.write(c)
f.close()

