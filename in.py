import requests
from bs4 import BeautifulSoup

print('....enter Ctrl + c for quit....\n')


def find():
    user = input('Enter User Name: ')
    try:
        URL = (f'https://www.instagram.com/{user}/')

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.text, 'html.parser')

        meta = soup.find('meta', property='og:description')
        return get(meta.attrs['content'])
    except:
        print('error : Please Enter Valid User Name')


def get(x):
    x = x.split(" ")

    data = 'Followers = ' + x[0]
    data1 = 'Following = ' + x[2]
    data2 = 'Posts = ' + x[4]

    print('Your user detail')
    print('********************************* \n')

    print(data)
    print(data1)
    print(data2 + '\n')

    print('Finish.... \n')


if __name__ == "__main__":
    while True:
        find()
