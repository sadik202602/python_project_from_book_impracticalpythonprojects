# Chapter 2: Finding Palingram Spells

## English

This project is based on Chapter 2 of the book Impractical Python Projects by Lee Vaughan, published by No Starch Press. The chapter has three programs. The first one is load_dictionary.py which downloads a text file containing 45000 English words and loads it into Python as a list. The second one is palindromes.py which searches through all the words in the dictionary file and finds words that read the same forward and backward like radar, kayak, and civic. The third one is palingrams.py which finds two word pairs that read the same forward and backward like nurses run and stack cats. From this chapter I learned how to load an external text file into Python, how to use try and except to handle file errors, how to use string slicing with the syntax word reversed to reverse a word, how to write and call my own functions using def, how to use a set instead of a list to make the program run faster, and how to measure the runtime of a program using time.time. To run the programs type python3 palindromes.py or python3 palingrams.py in the terminal after making sure dictionary.txt is in the same folder.

---

## 日本語

このプロジェクトはNo Starch Press出版のLee Vaughan著Impractical Python Projectsという本の第2章をベースにしています。この章には3つのプログラムがあります。最初のload_dictionary.pyは45000語の英単語が入ったテキストファイルをダウンロードしてPythonのリストとして読み込みます。2番目のpalindromes.pyは辞書ファイルの全単語を検索してradar、kayak、civicのように前から読んでも後ろから読んでも同じになる単語を見つけます。3番目のpalingrams.pyはnurses runやstack catsのように2つの単語を合わせて前後同じになる組み合わせを見つけます。この章では外部テキストファイルをPythonに読み込む方法、tryとexceptを使ったファイルエラーの処理方法、スライス構文を使って単語を逆にする方法、defを使って関数を書いて呼び出す方法、リストの代わりにセットを使ってプログラムを高速化する方法、time.timeを使ってプログラムの実行時間を計測する方法を学びました。プログラムを実行するにはdictionary.txtが同じフォルダにあることを確認してからターミナルでpython3 palindromes.pyまたはpython3 palingrams.pyと入力してください。