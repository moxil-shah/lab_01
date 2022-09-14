import requests

# print(requests.__version__)

print(requests.get("https://raw.githubusercontent.com/moxil-shah/lab_01/master/version_of_requests_&_print_sc.py").text)
