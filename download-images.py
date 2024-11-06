from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin

# スクレイピングするURLを指定
targetUrl = input("url : ")

response = requests.get(targetUrl)
soup = BeautifulSoup(response.text, 'html.parser')

# get image urls (JPEG only)
image_url_list = []
for img in soup.find_all('img'):
    img_url = img.get('src')

    if img_url:  # src属性が存在する場合
        # 完全なURLを作成
        img_url = urljoin(targetUrl, img_url)

        # JPEG形式の画像だけを対象にする
        if img_url.lower().endswith(('.jpg', '.jpeg')):
            image_url_list.append(img_url)

# 画像URLを表示
for i_url in image_url_list:
    print(i_url)

# ダウンロードした画像を保存するディレクトリを作成
os.makedirs('images', exist_ok=True)

# 画像をダウンロード
for i, img_url in enumerate(image_url_list):
    try:
        # 画像データを取得
        img_data = requests.get(img_url).content

        # 画像を保存
        with open(f'./images/image_{i}.jpg', 'wb') as f:
            f.write(img_data)

        print(f"Downloaded {img_url} as image_{i}.jpg")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {img_url}: {e}")
        continue

    except Exception as e:
        print(f"An error occurred while saving {img_url}: {e}")
        continue
