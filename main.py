import MeCab

wakati = MeCab.Tagger("-Owakati")
print(wakati.parse("各種スクリプト言語 (perl, ruby, python, Java) から, MeCab が提供する形態素解析の機能を利用可能です. 各バインディングは SWIG というプログラ ムを用いて, 自動生成されています. SWIG がサポートする他の言語も 生成可能だと思われますが, 現在は, 作者の管理できる範囲内ということで, 上記の4つの言語のみを提供しております.").split())
