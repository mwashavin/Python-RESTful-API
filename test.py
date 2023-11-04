import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 1780, "name": "Kevin", "views":10000},
        {"likes": 10040, "name": "mwas", "views":10300},
        {"likes": 15600, "name": "tim", "views":123000},
        {"likes": 1467000, "name": "Kevin", "views":1090000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/1" + str(i), data[i])
#     print(response.json())

# input()
# response = requests.delete(BASE + "video/0")
# print(response)
# input()
response = requests.patch(BASE + "video/10", {"views":100})
print(response.json())