import requests
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
from urllib import request
import re


url = 'https://www.aozora.gr.jp/cards/000879/files/128_15261.html'
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')
response.close()

main_text = soup.find('div', class_='main_text')
tags_to_delete = main_text.find_all(['rp', 'rt'])
for tag in tags_to_delete:
    tag.decompose()
main_text = main_text.get_text()
print(main_text)

main_text = re.sub(r"[\u3000 \n \r]", "", main_text)
print(main_text)

url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

stopwords_text = soup.text
stopwords_list = stopwords_text.split("\r\n")
stopwords_list = [word for word in stopwords_list if word]
print(stopwords_list)

split_text_list = ['近頃','は','何か','と','いう','と','文壇','の','趨勢','を','論じ','よう','と','する','人','が','多い']
result_text_list = list()
for split_text in split_text_list:
  if split_text not in stopwords_list:
    result_text_list.append(split_text)

print(result_text_list)