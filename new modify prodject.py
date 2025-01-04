import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import re

def is_valid_url(url):
    # Simple regex to validate URL format
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def internet_connection_test(url='https://www.google.com/'):
    print(f'Attempting to connect to {url} to determine internet connection status.')
    
    if not is_valid_url(url):
        print(f'Error: The provided URL "{url}" is not valid.')
        return False

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        print(f'Connection to {url} was successful. Status Code: {resp.status_code}')
        return True
    except ConnectionError:
        print(f'Failed to connect to {url}. Connection error.')
        return False
    except Timeout:
        print(f'Failed to connect to {url}. The request timed out.')
        return False
    except RequestException as e:
        print(f'Failed to connect to {url}. Error: {e}')
        return False

def main():
    while True:
        url = input("Enter a URL to test (or press Enter for default 'https://www.google.com/'): ")
        if not url:
            url = 'https://www.google.com/'
        
        internet_connection_test(url)
        
        retry = input("Do you want to test another URL? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()