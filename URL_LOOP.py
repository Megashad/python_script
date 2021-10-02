import requests

site = input("URL:")

for i in range(1,100):
	x = requests.get(f"{site}{i}")
	print(x.text)