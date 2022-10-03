'''
This script is designed to quickly check if
your internet connection is on.

You can run this automatically.
'''

# imports
from urllib.request import urlopen

def wifi():
    try:
        response = urlopen('http://www.example.com/')
        return True
    except Exception:
        return False

def main():
    internet = wifi()
    if internet:
        print("Your internet is ON!")
    else:
        print("Your internet is OFF!")

if __name__ == "__main__":
    main()
