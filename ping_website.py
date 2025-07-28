import requests


def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"{url} is UP. Status Code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"{url} is DOWN!")


check_website("https://example.com")
