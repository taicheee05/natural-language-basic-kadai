import MeCab

mecab_tagger = MeCab.Tagger()

text = '''自然言語処理（しぜんげんごしょり、英語: natural language processing、略称：NLP）は、
人間が日常的に使っている自然言語をコンピュータに処理させる一連の技術であり、人工知能と言語学の
一分野である。「計算言語学」（computational linguistics）との類似もあるが、自然言語処理は工学的
な視点からの言語処理をさすのに対して、計算言語学は言語学的視点を重視する手法をさす事が多い[1]。
データベース内の情報を自然言語に変換したり、自然言語の文章をより形式的な（コンピュータが理解し
やすい）表現に変換するといった処理が含まれる。応用例としては予測変換、IMEなどの文字変換が挙げら
れる。自然言語の理解をコンピュータにさせることは、自然言語理解とされている。自然言語理解と、自
然言語処理の差は、意味を扱うか、扱わないかという説もあったが、最近は数理的な言語解析手法（統計
や確率など）が広められた為、パーサ（統語解析器）などの精度や速度が一段と上がり、その意味合いは
違ってきている。もともと自然言語の意味論的側面を全く無視して達成できることは非常に限られている。
このため、自然言語処理には形態素解析と構文解析、文脈解析、意味解析などをSyntaxなど表層的な観点
から解析をする学問であるが、自然言語理解は、意味をどのように理解するかという個々人の理解と推論
部分が主な研究の課題になってきており、両者の境界は意思や意図が含まれるかどうかになってきている。'''
node = mecab_tagger.parseToNode(text)
count_dict = {}

while node:
    word = node.surface
    hinshi = node.feature.split(",")[0]
    if word in count_dict.keys() and hinshi == "名詞":
        count_dict[word] += 1
    elif hinshi == "名詞":
        count_dict[word] = 1
    else:
        pass
    node = node.next

word_counts = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
print(word_counts)