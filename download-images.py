from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin

# set target url
targetUrl = input("url : ")

response = requests.get(targetUrl)
soup = BeautifulSoup(response.text, 'html.parser')

# get image urls (JPEG only)
image_url_list = []
for img in soup.find_all('img'):
    img_url = img.get('src')

    if img_url:
        # make full url 
        img_url = urljoin(targetUrl, img_url)

        # JPEG形式の画像だけを対象にする
        if img_url.lower().endswith(('.jpg', '.jpeg')):
            image_url_list.append(img_url)

# print image url
for i_url in image_url_list:
    print(i_url)

# make downloaded image directory
os.makedirs('images', exist_ok=True)

# download images
for i, img_url in enumerate(image_url_list):
    try:
        img_data = requests.get(img_url).content
        with open(f'./images/image_{i}.jpg', 'wb') as f:
            f.write(img_data)

        print(f"Downloaded {img_url} as image_{i}.jpg")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {img_url}: {e}")
        continue

    except Exception as e:
        print(f"An error occurred while saving {img_url}: {e}")
        continue
