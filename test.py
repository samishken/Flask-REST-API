import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/2", {})
print(response.json())

# data = [{"likes": 14, "name": "Joe", "views": 7600},
#         {"likes": 18, "name": "Kim", "views": 14300},
#         {"likes": 10, "name": "Toni", "views": 10000}]

# for i in range(len(data)):
#   response = requests.put(BASE + "video/" + str(i), data[i])
#   print(response.json())


# input()
# response = requests.get(BASE + "video/6")
# print(response.json())
