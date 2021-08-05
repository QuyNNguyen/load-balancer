#Name: Quy Nguyen
#python3



import requests


def main():
	req = requests.get("http://csec.rit.edu")
	print(req)


main()
