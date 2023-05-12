import requests

url = """https://api.github.com/repos/DiLilloDaniele/gradle-python-testing/releases/latest"""

response = requests.get(url)
print(response.json()["tag_name"])
