import requests
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer

# URL of the "Bundan no Suusei" on Aozora Bunko
url = "https://www.aozora.gr.jp/cards/000148/files/2371_13943.html"

# Fetch the content from the URL
response = requests.get(url)
response.encoding = response.apparent_encoding  # Ensure correct encoding

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the main text from the document, assuming it is within <div class="main_text">
main_text = soup.get_text()  # If there's a specific class for main text, use soup.find(class_="...").get_text()

# Output the text or process it as needed
print(main_text[:500])  # Display the first 500 characters for example

clean_text = main_text.replace('\r', '').replace('\n', '').replace('\u3000', '')
# Add more replacements as needed to remove unwanted characters

# トークナイザーのインスタンスを作成
t = Tokenizer()

# 文章をトークン化（分かち書き）
text = '近頃は何かというと文壇の趨勢を論じようとする人が多い。'
tokens = t.tokenize(text)

# トークン化された文章を出力
for token in tokens:
    print(token.surface)