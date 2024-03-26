import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
print(nlp)

nlp = spacy.load('ja_ginza')
text = """
        プログラムは、高速処理ができます。私たち人間も、決して処理が遅いというわけではありません。
        2019年に開催された全日本珠算選手権大会の「フラッシュ暗算競技」部門では、画面に次々と表示される3桁の数字、15個を加算して答えを求めるという問題が出されました。
        この大会の優勝者は、この問題をわずか「1.66秒」で成功させました。これは驚くべきスピードであり、人間のさらなる可能性を感じさせるものでした。
        しかし富士通が開発した世界一のスパコンである「富岳」は、1秒間で41.5京回(京は1兆の1万倍)の処理を行うことに成功しました。これはどんなに計算が得意な人間であっても、到底かなわない圧倒的なスピードです。
        まさに、プログラムならではの「できること」だといえるでしょう。
      """
doc = nlp(text)

for token in doc:
  print(token.text, type(token))

print(displacy.render(doc, style="ent", options={"compact":True}))
