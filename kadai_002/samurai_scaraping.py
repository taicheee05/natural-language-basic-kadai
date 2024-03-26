import requests
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer

url = "https://www.aozora.gr.jp/cards/000148/files/2371_13943.html"

response = requests.get(url)
response.encoding = response.apparent_encoding  # Ensure correct encoding

soup = BeautifulSoup(response.text, 'html.parser')

main_text = soup.get_text()  # If there's a specific class for main text, use soup.find(class_="...").get_text()

print(main_text[:500])  # Display the first 500 characters for example

clean_text = main_text.replace('\r', '').replace('\n', '').replace('\u3000', '')

# トークナイザーのインスタンスを作成
t = Tokenizer()

text = '近頃は何かというと文壇の趨勢を論じようとする人が多い。'
tokens = t.tokenize(text)

for token in tokens:
    print(token.surface)