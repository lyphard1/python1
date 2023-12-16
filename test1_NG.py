#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import glob

def read_and_standardize_csv(file_path, encoding='shift_jis'):
    max_columns = 0
    data = []

    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            splitted_line = line.strip().split(',')
            max_columns = max(max_columns, len(splitted_line))
            data.append(splitted_line)

    standardized_data = [row + [''] * (max_columns - len(row)) for row in data]
    return pd.DataFrame(standardized_data)

files_distribution = glob.glob('DISTRIBUTION*.csv')
files_dividendlist = glob.glob('dividendlist*.csv')

df1_no_header = pd.concat([read_and_standardize_csv(f) for f in files_distribution])
df2_no_header = pd.concat([read_and_standardize_csv(f) for f in files_dividendlist])


# df1_no_headerの3列目と４列目のあいだに列を挿入し、値をAとする
df1_no_header.insert(4, '', 'A')

# デバッグ、ファイルに出力
df1_no_header.to_csv('test_distribution.csv', index=False)

# df2_no_headerの先頭行を削除
df2_no_header = df2_no_header.drop(index=0)
# df2_no_headerの2列目と3列目を入れ替え
df2_no_header[[df2_no_header.columns[1], df2_no_header.columns[2]]] = df2_no_header[[df2_no_header.columns[2], df2_no_header.columns[1]]]

# デバッグ、ファイルに出力
df2_no_header = pd.concat([df2_no_header], ignore_index=True)
df2_no_header.to_csv('test_dividendlist.csv', index=False)



# df1_no_headerとdf2_no_headerを結合
merged_df_no_header = pd.concat([df1_no_header, df2_no_header], ignore_index=True)


# デバッグ用
merged_df_no_header.to_csv('merged_file_no_header.csv', index=False)




# 先頭から10行を削除
merged_df_no_header = merged_df_no_header.drop(index=range(10))
# merged_df_no_headerの４列目の列名を銘柄コードに変更
merged_df_no_header = merged_df_no_header.rename(columns={merged_df_no_header.columns[3]: '銘柄コード'})



merged_df_no_header.to_csv('merged_file_no_header.csv', index=False)

# 最終行を取得
last_row = merged_df_no_header.iloc[-1]
# 最終行が空行であるかどうかを確認
is_empty = last_row.isnull().all()

print(is_empty)




pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#print(merged_df_no_header)
print(merged_df_no_header.to_string())

pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')


# In[ ]:


import pandas as pd
import glob

def read_and_standardize_csv(file_path, encoding='shift_jis'):
    max_columns = 0
    data = []

    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            splitted_line = line.strip().split(',')
            splitted_line = [item.replace(',', '') if item.replace('.', '', 1).isdigit() else item for item in splitted_line]
            max_columns = max(max_columns, len(splitted_line))
            data.append(splitted_line)

    standardized_data = [row + [''] * (max_columns - len(row)) for row in data]
    return pd.DataFrame(standardized_data)

files_distribution = glob.glob('DISTRIBUTION*.csv')
files_dividendlist = glob.glob('dividendlist*.csv')

df1_no_header = pd.concat([read_and_standardize_csv(f) for f in files_distribution])
df2_no_header = pd.concat([read_and_standardize_csv(f) for f in files_dividendlist])


# df1_no_headerの3列目と４列目のあいだに列を挿入し、値をAとする
df1_no_header.insert(4, '', 'A')

# デバッグ、ファイルに出力
df1_no_header.to_csv('test_distribution.csv', index=False)

# df2_no_headerの先頭行を削除
df2_no_header = df2_no_header.drop(index=0)
# df2_no_headerの2列目と3列目を入れ替え
df2_no_header[[df2_no_header.columns[1], df2_no_header.columns[2]]] = df2_no_header[[df2_no_header.columns[2], df2_no_header.columns[1]]]

# デバッグ、ファイルに出力
df2_no_header = pd.concat([df2_no_header], ignore_index=True)
df2_no_header.to_csv('test_dividendlist.csv', index=False)



# df1_no_headerとdf2_no_headerを結合
merged_df_no_header = pd.concat([df1_no_header, df2_no_header], ignore_index=True)


# デバッグ用
merged_df_no_header.to_csv('merged_file_no_header.csv', index=False)




# 先頭から10行を削除
merged_df_no_header = merged_df_no_header.drop(index=range(10))
# merged_df_no_headerの４列目の列名を銘柄コードに変更
merged_df_no_header = merged_df_no_header.rename(columns={merged_df_no_header.columns[3]: '銘柄コード'})



merged_df_no_header.to_csv('merged_file_no_header.csv', index=False)

# 最終行を取得
last_row = merged_df_no_header.iloc[-1]
# 最終行が空行であるかどうかを確認
is_empty = last_row.isnull().all()

print(is_empty)




pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#print(merged_df_no_header)
print(merged_df_no_header.to_string())

pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')


# In[ ]:


import pandas as pd
import csv
import glob

def read_and_standardize_csv(file_path, encoding='shift_jis'):
    data = []

    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file)
        for row in reader:
            # クオートに囲まれた数値のカンマを取り除く
            row = [item.replace(',', '') if item.replace('.', '', 1).isdigit() else item for item in row]
            data.append(row)

    return pd.DataFrame(data)

files_distribution = glob.glob('DISTRIBUTION*.csv')
files_dividendlist = glob.glob('dividendlist*.csv')

df1_no_header = pd.concat([read_and_standardize_csv(f) for f in files_distribution])
df2_no_header = pd.concat([read_and_standardize_csv(f) for f in files_dividendlist])

# df1_no_headerの3列目と４列目のあいだに列を挿入し、値をAとする
df1_no_header.insert(4, '', 'A')
# 先頭から10行を削除
df1_no_header = df1_no_header.drop(index=range(10))
# df1_no_headerの４列目の列名を銘柄コードに変更
df1_no_header = df1_no_header.rename(columns={df1_no_header.columns[3]: '銘柄コード'})






# デバッグ、ファイルに出力
df1_no_header.to_csv('test_distribution.csv', index=False)

# df2_no_headerの先頭行を削除
df2_no_header = df2_no_header.drop(index=0)
# df2_no_headerの2列目と3列目を入れ替え
df2_no_header[[df2_no_header.columns[1], df2_no_header.columns[2]]] = df2_no_header[[df2_no_header.columns[2], df2_no_header.columns[1]]]

# デバッグ、ファイルに出力
df2_no_header = pd.concat([df2_no_header], ignore_index=True)
df2_no_header.to_csv('test_dividendlist.csv', index=False)



# df1_no_headerとdf2_no_headerを結合
merged_df_no_header = pd.concat([df1_no_header, df2_no_header], ignore_index=True)


# デバッグ、ファイルに出力
merged_df_no_header.to_csv('merged_file_no_header.csv', index=False)






merged_df_no_header.to_csv('merged_file_no_header.csv', index=False)

# 最終行を取得
last_row = merged_df_no_header.iloc[-1]
# 最終行が空行であるかどうかを確認
is_empty = last_row.isnull().all()

print(is_empty)




pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#print(merged_df_no_header)
print(merged_df_no_header.to_string())

pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')


# In[6]:


import pandas as pd
import csv
import glob

def read_and_standardize_csv(file_path, encoding='shift_jis', skip_lines=10):
  data = []

  with open(file_path, 'r', encoding=encoding) as file:
    for _ in range(skip_lines):
      next(file)  # Skip the line

    reader = csv.reader(file)
    for row in reader:
      # クオートに囲まれた数値のカンマを取り除く
      row = [item.replace(',', '') if item.replace('.', '', 1).isdigit() else item for item in row]
      data.append(row)

  return pd.DataFrame(data)

files_distribution = glob.glob('DISTRIBUTION*.csv')
files_dividendlist = glob.glob('dividendlist*.csv')

df1_no_header = pd.concat([read_and_standardize_csv(f) for f in files_distribution])
df2_no_header = pd.concat([read_and_standardize_csv(f) for f in files_dividendlist])



# df1_no_headerの3列目と４列目のあいだに列を挿入し、値をAとする
df1_no_header.insert(4, '', 'A')
# 先頭から10行を削除
df1_no_header = df1_no_header.drop(index=range(10))
# df1_no_headerの４列目の列名を銘柄コードに変更
df1_no_header = df1_no_header.rename(columns={df1_no_header.columns[3]: '銘柄コード'})






# デバッグ、ファイルに出力
df1_no_header.to_csv('test_distribution.csv', index=False)

# df2_no_headerの先頭行を削除
df2_no_header = df2_no_header.drop(index=0)
# df2_no_headerの2列目と3列目を入れ替え
df2_no_header[[df2_no_header.columns[1], df2_no_header.columns[2]]] = df2_no_header[[df2_no_header.columns[2], df2_no_header.columns[1]]]

# デバッグ、ファイルに出力
df2_no_header = pd.concat([df2_no_header], ignore_index=True)
df2_no_header.to_csv('test_dividendlist.csv', index=False)



# df1_no_headerとdf2_no_headerを結合
merged_df_no_header = pd.concat([df1_no_header, df2_no_header], ignore_index=True)


# デバッグ、ファイルに出力
merged_df_no_header.to_csv('merged_file_no_header.csv', index=False)






merged_df_no_header.to_csv('merged_file_no_header.csv', index=False)

# 最終行を取得
last_row = merged_df_no_header.iloc[-1]
# 最終行が空行であるかどうかを確認
is_empty = last_row.isnull().all()

print(is_empty)




pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#print(merged_df_no_header)
print(merged_df_no_header.to_string())

pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')


# In[24]:


import pandas as pd

file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'
df = pd.read_csv(file_path, skiprows=0, encoding='cp932')  # Shift_JIS (CP932) を使用
print(df)



# In[28]:


import pandas as pd

# ファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'

# CSVファイルを読み込む際に、最初の行をスキップ（削除）する
#df = pd.read_csv(file_path, skiprows=1, encoding='cp932')

df = pd.read_csv(file_path, header=None)

# 結果を確認するために最初の数行を表示
print(df.head())

# 必要に応じて加工したデータを新しいファイルとして保存
df.to_csv('C:/Users/hdmae/Documents/python1/test_dividendlist.csv', index=False)




# In[35]:


# OK
import pandas as pd

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_dividendlist.csv'

# 元のファイルを読み込む（エンコーディングには注意が必要です）
df = pd.read_csv(file_path, encoding='cp932')  # または 'utf-8' など、ファイルに合わせて変更してください
# 結果を確認するために最初の数行を表示
print(df.head())

# ヘッダーを削除して新しいファイルに保存
df.to_csv(new_file_path, index=False, header=False)

#########################################
# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/DISTRIBUTION.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_DISTRIBUTION.csv'



# 最初の10行をスキップし、11行目をヘッダーとして読み込む
df = pd.read_csv(file_path, skiprows=10, encoding='cp932')

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(df.head())



# In[38]:


# OK
import pandas as pd

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_dividendlist.csv'

# 元のファイルを読み込む（エンコーディングには注意が必要です）
df = pd.read_csv(file_path, encoding='cp932')  # または 'utf-8' など、ファイルに合わせて変更してください

# dfの2列目と3列目を入れ替え
df[df.columns[1]], df[df.columns[2]] = df[df.columns[2]], df[df.columns[1]]

# 結果を確認するために最初の数行を表示
print(df.head())

# ヘッダーを削除して新しいファイルに保存
df.to_csv(new_file_path, index=False, header=False)

#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/DISTRIBUTION.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_DISTRIBUTION.csv'

# 最初の10行をスキップし、11行目をヘッダーとして読み込む
df = pd.read_csv(file_path, skiprows=10, encoding='cp932')

# dfの2列目と3列目のあいだに列を挿入し、ヘッダーを銘柄コードとする。
df.insert(3, '銘柄コード', '')


# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(df.head())



# In[2]:


# OK
import pandas as pd

#########################################
#　楽天証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_dividendlist.csv'

# 元のファイルを読み込む（エンコーディングには注意が必要です）
df = pd.read_csv(file_path, encoding='cp932')  # または 'utf-8' など、ファイルに合わせて変更してください

# dfの2列目と3列目を入れ替え
df[df.columns[1]], df[df.columns[2]] = df[df.columns[2]], df[df.columns[1]]
#df[df.columns[1]], df[df.columns[2]] = df[df.columns[1]], df[df.columns[2]]

# 結果を確認するために最初の数行を表示
print(df.head())

# ヘッダーを削除して新しいファイルに保存
df.to_csv(new_file_path, index=False, header=False)

#########################################
# SBI証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/DISTRIBUTION.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_DISTRIBUTION.csv'

# 最初の10行をスキップし、11行目をヘッダーとして読み込む
df = pd.read_csv(file_path, skiprows=10, encoding='cp932')

# dfの2列目と3列目のあいだに列を挿入し、ヘッダーを銘柄コードとする。
df.insert(3, '銘柄コード', '')

# dfの6列目と7列目のあいだに4個の列を挿入し、ヘッダーは、適当な名前とする。

# 適当な名前のリスト
column_names = ['適当な名前1', '適当な名前2', '適当な名前3', '適当な名前4']

# 列の挿入
for i, name in enumerate(column_names, start=6):
  df.insert(i, name, '')

# 11列目の値から円の文字を取り除く
df[df.columns[10]] = df[df.columns[10]].str.replace('円', '')

# 5列目の文字列の最後のスペースの後ろの文字列を取得する。なければ、すべての文字列を取得する。
df[df.columns[3]] = df[df.columns[4]].str.rsplit(n=1).str[-1]
df[df.columns[3]] = df[df.columns[4]].str.split().str[-1]
# 取得した文字列を4列目に入れる

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(df.head())



# 
# はい、Visual Studio Codeでは、任意のGitリポジトリを作業フォルダとして使用することが可能です。以下の手順で`python1.git`を作業フォルダとして設定できます。
# 
# 1. Visual Studio Codeを開きます。
# 2. 左側のメニューバーから「ソース管理」アイコンをクリックします。
# 3. 「リポジトリをクローン」をクリックします。
# 4. `python1.git`のURLを入力します。
# 5. ローカルに保存するディレクトリを選択します。
# 
# これで`python1.git`が作業フォルダとして設定され、その中のファイルを編集したり、変更をコミットしたりすることができます。

# In[3]:


# OK (Windowsで動作確認済み)
import pandas as pd

#########################################
#　楽天証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_dividendlist.csv'

# 元のファイルを読み込む（エンコーディングには注意が必要です）
df = pd.read_csv(file_path, encoding='cp932')  # または 'utf-8' など、ファイルに合わせて変更してください

# dfの2列目と3列目を入れ替え
df[df.columns[1]], df[df.columns[2]] = df[df.columns[2]], df[df.columns[1]]

# 結果を確認するために最初の数行を表示
print(df.head())

# ヘッダーを削除して新しいファイルに保存
df.to_csv(new_file_path, index=False, header=False)

#########################################
# SBI証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/DISTRIBUTION.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_DISTRIBUTION.csv'

# 最初の10行をスキップし、11行目をヘッダーとして読み込む
df = pd.read_csv(file_path, skiprows=10, encoding='cp932')

# dfの2列目と3列目のあいだに列を挿入し、ヘッダーを銘柄コードとする。
df.insert(3, '銘柄コード', '')

# dfの6列目と7列目のあいだに4個の列を挿入し、ヘッダーは、適当な名前とする。

# 適当な名前のリスト
column_names = ['適当な名前1', '適当な名前2', '適当な名前3', '適当な名前4']

# 列の挿入
for i, name in enumerate(column_names, start=6):
  df.insert(i, name, '')

# 11列目の値から円の文字を取り除く
df[df.columns[10]] = df[df.columns[10]].str.replace('円', '')

#5列目の文字列の最後のスペースの後ろのアルファベットの文字列を取得する。アルファベット文字列と異なれば、
# すべての文字列を取得する。5列目の文字列はそのままとする。取得した文字列を4列目に入れる
df[df.columns[3]] = df.iloc[:, 4].str.extract(r'([A-Za-z]+)$').fillna(df.iloc[:, 4])

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(df.head())



# In[13]:


# OK (Windowsで動作確認済み)
import pandas as pd
import re  # 正規表現ライブラリをインポート

#########################################
# 5列目のデータからアルファベットのみの文字列を抽出する関数の定義

def extract_alpha(cell):
    if pd.isna(cell):
        return cell
    extracted = re.search(r'([A-Za-z]+)$', cell)
    return extracted.group(0) if extracted else cell
#########################################

#########################################
#　楽天証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_dividendlist.csv'

# 元のファイルを読み込む（エンコーディングには注意が必要です）
df = pd.read_csv(file_path, encoding='cp932')  # または 'utf-8' など、ファイルに合わせて変更してください

# dfの2列目と3列目を入れ替え
df[df.columns[1]], df[df.columns[2]] = df[df.columns[2]], df[df.columns[1]]

# 一列目が日付だが、一列目でソートする。日付の昇順になる。
# 日付列を日付型に変換
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.sort_values(df.columns[0])

# 結果を確認するために最初の数行を表示
print(df.head())

# ヘッダーを削除して新しいファイルに保存
df.to_csv(new_file_path, index=False, header=False)

#########################################
# SBI証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/DISTRIBUTION.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_DISTRIBUTION.csv'

# 最初の10行をスキップし、11行目をヘッダーとして読み込む
df = pd.read_csv(file_path, skiprows=10, encoding='cp932')

# dfの2列目と3列目のあいだに列を挿入し、ヘッダーを銘柄コードとする。
df.insert(3, '銘柄コード', '')

# dfの6列目と7列目のあいだに4個の列を挿入し、ヘッダーは、適当な名前とする。

# 適当な名前のリスト
column_names = ['適当な名前1', '適当な名前2', '適当な名前3', '適当な名前4']

# 列の挿入
for i, name in enumerate(column_names, start=6):
  df.insert(i, name, '')

# 11列目の値から円の文字を取り除く
df[df.columns[10]] = df[df.columns[10]].str.replace('円', '')

#5列目の文字列の最後のスペースの後ろのアルファベットの文字列を取得する。アルファベット文字列と異なれば、
# すべての文字列を取得する。5列目の文字列はそのままとする。取得した文字列を4列目に入れる
# df[df.columns[3]] = df[df.columns[4]].str.rsplit(n=1).str[-1]
# df[df.columns[3]] = df[df.columns[4]].str.split().str[-1]
#df['銘柄コード'] = df.iloc[:, 4].str.extract(r'([A-Za-z]+)$').fillna(df.iloc[:, 4])

# 新しい列を4列目に挿入
#df.insert(3, '銘柄コード', df['銘柄コード'])

#df['銘柄コード'] = df.iloc[:, 4].str.extract(r'([A-Za-z]+)$').fillna(df.iloc[:, 4])

# 5列目のデータからアルファベットのみの文字列を抽出する関数を各行に適用して、
# 結果を4列目の「銘柄コード」列に格納
df['銘柄コード'] = df.iloc[:, 4].apply(extract_alpha)


# 一列目が日付だが、一列目でソートする。日付の昇順になる。
# 日付列を日付型に変換
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.sort_values(df.columns[0])

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(df.head())



# In[ ]:


# OK (Windowsで動作確認済み)
import pandas as pd
import re  # 正規表現ライブラリをインポート

#########################################
# 5列目のデータからアルファベットのみの文字列を抽出する関数の定義

def extract_alpha(cell):
    if pd.isna(cell):
        return cell
    extracted = re.search(r'([A-Za-z]+)$', cell)
    return extracted.group(0) if extracted else cell
#########################################

#########################################
#　楽天証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_dividendlist.csv'

# 元のファイルを読み込む（エンコーディングには注意が必要です）
df = pd.read_csv(file_path, encoding='cp932')  # または 'utf-8' など、ファイルに合わせて変更してください

# dfの2列目と3列目を入れ替え
df[df.columns[1]], df[df.columns[2]] = df[df.columns[2]], df[df.columns[1]]

# 一列目が日付だが、一列目でソートする。日付の昇順になる。
# 日付列を日付型に変換
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.sort_values(df.columns[0])

# 結果を確認するために最初の数行を表示
print(df.head())

# ヘッダーを削除して新しいファイルに保存
df.to_csv(new_file_path, index=False, header=False)

#########################################
# SBI証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/DISTRIBUTION.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_DISTRIBUTION.csv'

# 最初の10行をスキップし、11行目をヘッダーとして読み込む
df = pd.read_csv(file_path, skiprows=10, encoding='cp932')

# dfの2列目と3列目のあいだに列を挿入し、ヘッダーを銘柄コードとする。
df.insert(3, '銘柄コード', '')

# dfの6列目と7列目のあいだに4個の列を挿入し、ヘッダーは、適当な名前とする。

# 適当な名前のリスト
column_names = ['適当な名前1', '適当な名前2', '適当な名前3', '適当な名前4']

# 列の挿入
for i, name in enumerate(column_names, start=6):
  df.insert(i, name, '')

# 11列目の値から円の文字を取り除く
df[df.columns[10]] = df[df.columns[10]].str.replace('円', '')

#5列目の文字列の最後のスペースの後ろのアルファベットの文字列を取得する。アルファベット文字列と異なれば、
# すべての文字列を取得する。5列目の文字列はそのままとする。取得した文字列を4列目に入れる
# df[df.columns[3]] = df[df.columns[4]].str.rsplit(n=1).str[-1]
# df[df.columns[3]] = df[df.columns[4]].str.split().str[-1]
#df['銘柄コード'] = df.iloc[:, 4].str.extract(r'([A-Za-z]+)$').fillna(df.iloc[:, 4])

# 新しい列を4列目に挿入
#df.insert(3, '銘柄コード', df['銘柄コード'])

#df['銘柄コード'] = df.iloc[:, 4].str.extract(r'([A-Za-z]+)$').fillna(df.iloc[:, 4])

# 5列目のデータからアルファベットのみの文字列を抽出する関数を各行に適用して、
# 結果を4列目の「銘柄コード」列に格納
df['銘柄コード'] = df.iloc[:, 4].apply(extract_alpha)


# 一列目が日付だが、一列目でソートする。日付の昇順になる。
# 日付列を日付型に変換
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.sort_values(df.columns[0])

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(df.head())



# In[2]:


import pandas as pd

# Read the CSV file
df = pd.read_csv('array1.csv')

# Display the dataframe
print(df)


# ファイルの変更を保存した後、以下の手順で変更をGitにコミットできます。
# 
# 1. Visual Studio Codeの左側のメニューバーから「ソース管理」アイコンをクリックします。
# 2. 変更をステージングします。これは、変更をコミットに含めるための準備ステップです。変更したファイルの横にある「＋」アイコンをクリックします。
# 3. コミットメッセージを入力します。メッセージは、あなたが何を変更したかを簡潔に説明するべきです。
# 4. 「✔」アイコンをクリックしてコミットします。
# 
# これで、あなたの変更はローカルのGitリポジトリに保存されます。リモートのGitHubリポジトリにプッシュするには、ターミナルで`git push`コマンドを実行します。
# 
# 

# はい、Visual Studio CodeではGUIを使用してリモートのGitHubリポジトリにプッシュすることも可能です。以下の手順で操作できます。
# 
# 1. Visual Studio Codeの左側のメニューバーから「ソース管理」アイコンをクリックします。
# 2. ソース管理パネルの上部にある「...」メニューをクリックします。
# 3. ドロップダウンメニューから「プッシュ」を選択します。
# 
# これで、あなたの変更はリモートのGitHubリポジトリにプッシュされます。

# 「ソース管理」は、Visual Studio Codeの機能の一つで、Gitなどのバージョン管理システムを統合して操作できるようにするものです。ここからファイルの変更をステージング、コミット、プッシュなどの操作を行うことができます。
# 
# 一方、「ソース管理リポジトリ」は、「ソース管理」機能内で管理されている個々のリポジトリを指します。一つのVS Codeのワークスペース内で複数のリポジトリを管理することが可能で、それぞれのリポジトリは独立して操作を行うことができます。
# 
# したがって、「ソース管理」はバージョン管理の操作全体を指し、「ソース管理リポジトリ」はその中で管理されている個々のリポジトリを指すという違いがあります。

# Gitにおける各コマンドの基本的な意味は以下の通りです：
# 
# - **プル（Pull）**: リモートリポジトリの変更をローカルリポジトリに取り込む操作です。具体的には、リモートリポジトリの内容をフェッチ（Fetch）してから、それを現在のブランチにマージ（Merge）します。
# 
# - **プッシュ（Push）**: ローカルリポジトリの変更をリモートリポジトリに送信する操作です。これにより、他の人もあなたの変更を見ることができます。
# 
# - **クローン（Clone）**: リモートリポジトリのコピーを新たに作成する操作です。これにより、リモートリポジトリの全てのファイルと履歴があなたのローカルマシンにコピーされます。
# 
# - **チェックアウト（Checkout）**: 特定のブランチやコミットに切り替える操作です。これにより、そのブランチやコミットの状態のコードを見ることができます。
# 
# - **フェッチ（Fetch）**: リモートリポジトリの最新の内容をローカルに取得する操作です。ただし、フェッチした内容は自動的に現在のブランチにマージされません。
# 
# - **スタッシュ（Stash）**: 現在の作業ディレクトリの変更を一時的に保存する操作です。これにより、別の作業を行うために作業ディレクトリをクリーンな状態に戻すことができます。
# 
# - **タグ（Tag）**: 特定のコミットにラベルを付ける操作です。これは通常、リリースのバージョンなど、特定のコミットを後から簡単に見つけられるようにするために使用されます。

# Gitにおける「コミット（Commit）」と「ブランチ（Branch）」の基本的な意味は以下の通りです：
# 
# - **コミット（Commit）**: ファイルやディレクトリの変更を保存する操作です。コミットを作成すると、その時点のプロジェクトのスナップショットが作られ、後からその状態に戻ることができます。また、コミットには一意のID（ハッシュ値）が付けられ、これにより特定のコミットを参照することができます。
# 
# - **ブランチ（Branch）**: 作業の流れを分岐させるためのポインタです。ブランチを作成すると、新たな作業の流れが作られ、そのブランチ上での変更は他のブランチに影響を与えません。これにより、同じリポジトリ内で複数の作業を並行して行うことができます。ブランチはコミットを指すポインタであり、特定のブランチが指すコミットを更新することで、ブランチの位置を移動することができます。

# Gitのコミットにサインオフ（Sign-off）を追加するというのは、コミットメッセージの最後に「Signed-off-by: Your Name <your.email@example.com>」を追加することを意味します。これは、コミットが特定の要件を満たしていること（例えば、貢献者ライセンス契約に同意していること）を示すために使用されます。
# 
# Visual Studio Code (VS Code) では、Gitの設定を変更することで、自動的にサインオフを追加することができます。以下の手順で設定を変更します：
# 
# 1. VS Codeを開き、左側のアクティビティバーから「ソース管理」（ブランチのアイコン）をクリックします。
# 
# 2. 「ソース管理」パネルが開きます。ここで、「...」メニューをクリックし、「設定」を選択します。
# 
# 3. 「Git: Enable Commit Signing」を検索し、チェックボックスをオンにします。
# 
# これにより、今後のコミットには自動的にサインオフが追加されます。

# Gitのスタッシュ機能は、現在の作業ディレクトリの状態を一時的に保存し、作業ディレクトリをクリーンな状態に戻すためのものです。これは、別のタスクに移る前に現在の作業を一時的に保存したいときなどに便利です。
# 
# Visual Studio Code (VS Code) では、以下の手順でスタッシュを作成できます：
# 
# 1. VS Codeを開き、左側のアクティビティバーから「ソース管理」（ブランチのアイコン）をクリックします。
# 
# 2. 「ソース管理」パネルが開きます。ここで、リポジトリの変更を確認できます。
# 
# 3. 「...」メニューをクリックし、「スタッシュ」を選択します。これにより、現在の作業ディレクトリの状態が一時的に保存され、作業ディレクトリはクリーンな状態に戻ります。
# 
# スタッシュした内容を再度適用するには、「...」メニューから「スタッシュの適用」を選択します。これにより、最後にスタッシュした内容が作業ディレクトリに再度適用されます。

# Gitの操作をGUIで行いたい場合、以下の手順で行うことができます。ここでは、Visual Studio Code (VS Code) のGit拡張機能を使用した手順を説明します。
# 
# 1. VS Codeを開き、左側のアクティビティバーから「ソース管理」（ブランチのアイコン）をクリックします。
# 
# 2. 「ソース管理」パネルが開きます。ここで、リポジトリの変更を確認できます。
# 
# 3. リモートリポジトリから最新の変更を取得するには、「...」メニューをクリックし、「Pull」を選択します。
# 
# 4. ローカルリポジトリをリモートリポジトリの状態に更新するには、「...」メニューをクリックし、「Discard All Changes」を選択します。これにより、ローカルの変更はすべて破棄され、リモートリポジトリの状態と同じになります。
# 
# 注意: 「Discard All Changes」はローカルの変更をすべて破棄するので、未コミットの変更がある場合は注意が必要です。

# そのメッセージは、現在の作業ツリーに未コミットの変更があるため、新しいブランチにチェックアウトする前にそれらの変更を消去するかコミットする必要があることを示しています。
# 
# GUIで操作する場合、Visual Studio Code (VS Code) のGit拡張機能を使用して以下の手順を実行します。
# 
# 1. VS Codeを開き、左側のアクティビティバーから「ソース管理」（ブランチのアイコン）をクリックします。
# 
# 2. 「ソース管理」パネルが開きます。ここで、リポジトリの変更を確認できます。
# 
# 3. 未コミットの変更を破棄するには、「...」メニューをクリックし、「Discard All Changes」を選択します。これにより、ローカルの変更はすべて破棄されます。
# 
# 注意: 「Discard All Changes」はローカルの変更をすべて破棄するので、未コミットの変更がある場合は注意が必要です。これらの変更は復元できません。
# 
# もしくは、変更を保存したい場合は、新しいコミットを作成します。変更をステージに追加し、コミットメッセージを入力した後、「✓」（コミット）ボタンをクリックします。
# 
# これらの手順を実行した後、新しいブランチに安全にチェックアウトできます。

# In[ ]:


# OK (Windowsで動作確認済み)
import pandas as pd
import re  # 正規表現ライブラリをインポート

#########################################
# 5列目のデータからアルファベットのみの文字列を抽出する関数の定義

def extract_alpha(cell):
    if pd.isna(cell):
        return cell
    extracted = re.search(r'([A-Za-z]+)$', cell)
    return extracted.group(0) if extracted else cell
#########################################

#########################################
#　楽天証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/dividendlist.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_dividendlist.csv'

# 元のファイルを読み込む（エンコーディングには注意が必要です）
df = pd.read_csv(file_path, encoding='cp932')  # または 'utf-8' など、ファイルに合わせて変更してください

# dfの2列目と3列目を入れ替え
df[df.columns[1]], df[df.columns[2]] = df[df.columns[2]], df[df.columns[1]]

# 一列目が日付だが、一列目でソートする。日付の昇順になる。
# 日付列を日付型に変換
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.sort_values(df.columns[0])

#6列目の文字列を削除する
df[df.columns[5]] = df[df.columns[5]].str.replace('.*', '', regex=True)

# 2列目に楽天証券という文字列を挿入
df.insert(1, '証券会社', '楽天証券')

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(df.head())

#########################################
# SBI証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'C:/Users/hdmae/Documents/python1/DISTRIBUTION.csv'
# 新しいファイルパスを指定
new_file_path = 'C:/Users/hdmae/Documents/python1/test_DISTRIBUTION.csv'

# 最初の10行をスキップし、11行目をヘッダーとして読み込む
df = pd.read_csv(file_path, skiprows=10, encoding='cp932')

# dfの2列目と3列目のあいだに列を挿入し、ヘッダーを銘柄コードとする。
df.insert(3, '銘柄コード', '')

# dfの6列目と7列目のあいだに4個の列を挿入し、ヘッダーは、適当な名前とする。

# 適当な名前のリスト
column_names = ['適当な名前1', '適当な名前2', '適当な名前3', '適当な名前4']

# 列の挿入
for i, name in enumerate(column_names, start=6):
  df.insert(i, name, '')

# 11列目の値から円の文字を取り除く
df[df.columns[10]] = df[df.columns[10]].str.replace('円', '')

#5列目の文字列の最後のスペースの後ろのアルファベットの文字列を取得する。アルファベット文字列と異なれば、
# すべての文字列を取得する。5列目の文字列はそのままとする。取得した文字列を4列目に入れる
# df[df.columns[3]] = df[df.columns[4]].str.rsplit(n=1).str[-1]
# df[df.columns[3]] = df[df.columns[4]].str.split().str[-1]
#df['銘柄コード'] = df.iloc[:, 4].str.extract(r'([A-Za-z]+)$').fillna(df.iloc[:, 4])

# 新しい列を4列目に挿入
#df.insert(3, '銘柄コード', df['銘柄コード'])

#df['銘柄コード'] = df.iloc[:, 4].str.extract(r'([A-Za-z]+)$').fillna(df.iloc[:, 4])

# 5列目のデータからアルファベットのみの文字列を抽出する関数を各行に適用して、
# 結果を4列目の「銘柄コード」列に格納
df['銘柄コード'] = df.iloc[:, 4].apply(extract_alpha)

# 一列目が日付だが、一列目でソートする。日付の昇順になる。
# 日付列を日付型に変換
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.sort_values(df.columns[0])

# 2列目にSBI証券という文字列を挿入
df.insert(1, '証券会社', 'SBI証券')

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
#print(df.head())

#　SBI証券の配当金明細書のCSVファイルと楽天証券の配当金明細書のCSVファイルを読み込み、
#  SBI証券の下に楽天証券の配当金明細書のCSVファイルをマージする。
#　マージした結果をCSVファイルに保存する。
# ファイルパスを指定
sbi_file_path = 'C:/Users/hdmae/Documents/python1/test_DISTRIBUTION.csv'
rakuten_file_path = 'C:/Users/hdmae/Documents/python1/test_dividendlist.csv'
merged_dfmerged_file_path = 'C:/Users/hdmae/Documents/python1/merged.csv'

# SBI証券のCSVファイルを読み込む
sbi_df = pd.read_csv(sbi_file_path)
#print(sbi_df.head())

# 楽天証券のCSVファイルを読み込む
rakuten_df = pd.read_csv(rakuten_file_path)
#print(rakuten_df.head())

# SBI証券のCSVファイルのヘッダを楽天証券のCSVファイルのヘッダとする
rakuten_df.columns = sbi_df.columns
# 楽天証券のCSVファイルに保存（ヘッダーを含む）
rakuten_df.to_csv(rakuten_file_path, index=False)
#print(rakuten_df.head())

#SBI証券のCSVファイルの一番下の行の次の行に楽天証券のCSVファイルをマージする
merged_df = pd.concat([sbi_df, rakuten_df])

#8列目から11列目の列を削除する
merged_df = merged_df.drop(merged_df.columns[[7, 8, 9, 10]], axis=1)

# マージ結果をCSVファイルに保存
merged_df.to_csv(merged_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(merged_df.head())



# In[45]:


# OK (Windowsで動作確認済み)
import pandas as pd
import re  # 正規表現ライブラリをインポート

#########################################
# 5列目のデータからアルファベットのみの文字列を抽出する関数の定義

def extract_alpha(cell):
    if pd.isna(cell):
        return cell
    extracted = re.search(r'([A-Za-z]+)$', cell)
    return extracted.group(0) if extracted else cell
#########################################

#########################################
#　楽天証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'dividendlist.csv'
# 新しいファイルパスを指定
new_file_path = 'test_dividendlist.csv'

# 元のファイルを読み込む（エンコーディングには注意が必要です）
df = pd.read_csv(file_path, encoding='cp932')  # または 'utf-8' など、ファイルに合わせて変更してください

# dfの2列目と3列目を入れ替え
df[df.columns[1]], df[df.columns[2]] = df[df.columns[2]], df[df.columns[1]]

# 一列目が日付だが、一列目でソートする。日付の昇順になる。
# 日付列を日付型に変換
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.sort_values(df.columns[0])

#6列目の文字列を削除する
df[df.columns[5]] = df[df.columns[5]].str.replace('.*', '', regex=True)

# 2列目に楽天証券という文字列を挿入
df.insert(1, '証券会社', '楽天証券')

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(df.head())

#########################################
# SBI証券の配当金明細書のCSVファイルを読み込む
#########################################

# 元のファイルパスを指定
file_path = 'DISTRIBUTION.csv'
# 新しいファイルパスを指定
new_file_path = 'test_DISTRIBUTION.csv'

# 最初の10行をスキップし、11行目をヘッダーとして読み込む
df = pd.read_csv(file_path, skiprows=10, encoding='cp932')

# dfの2列目と3列目のあいだに列を挿入し、ヘッダーを銘柄コードとする。
df.insert(3, '銘柄コード', '')

# dfの6列目と7列目のあいだに4個の列を挿入し、ヘッダーは、適当な名前とする。

# 適当な名前のリスト
column_names = ['適当な名前1', '適当な名前2', '適当な名前3', '適当な名前4']

# 列の挿入
for i, name in enumerate(column_names, start=6):
  df.insert(i, name, '')

# 11列目の値から円の文字を取り除く
df[df.columns[10]] = df[df.columns[10]].str.replace('円', '')

#5列目の文字列の最後のスペースの後ろのアルファベットの文字列を取得する。アルファベット文字列と異なれば、
# すべての文字列を取得する。5列目の文字列はそのままとする。取得した文字列を4列目に入れる
# 5列目のデータからアルファベットのみの文字列を抽出する関数を各行に適用して、
# 結果を4列目の「銘柄コード」列に格納
df['銘柄コード'] = df.iloc[:, 4].apply(extract_alpha)

# 一列目が日付だが、一列目でソートする。日付の昇順になる。
# 日付列を日付型に変換
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
df = df.sort_values(df.columns[0])

# 2列目にSBI証券という文字列を挿入
df.insert(1, '証券会社', 'SBI証券')

# 新しいファイルに保存（ヘッダーを含む）
df.to_csv(new_file_path, index=False)

# 結果を確認するために最初の数行を表示
#print(df.head())

#　SBI証券の配当金明細書のCSVファイルと楽天証券の配当金明細書のCSVファイルを読み込み、
#  SBI証券の下に楽天証券の配当金明細書のCSVファイルをマージする。
#　マージした結果をCSVファイルに保存する。
# ファイルパスを指定
sbi_file_path = 'test_DISTRIBUTION.csv'
rakuten_file_path = 'test_dividendlist.csv'
merged_dfmerged_file_path = 'merged.csv'

# SBI証券のCSVファイルを読み込む
sbi_df = pd.read_csv(sbi_file_path)
#print(sbi_df.head())

# 楽天証券のCSVファイルを読み込む
rakuten_df = pd.read_csv(rakuten_file_path)
#print(rakuten_df.head())

# SBI証券のCSVファイルのヘッダを楽天証券のCSVファイルのヘッダとする
rakuten_df.columns = sbi_df.columns
# 楽天証券のCSVファイルに保存（ヘッダーを含む）
rakuten_df.to_csv(rakuten_file_path, index=False)
#print(rakuten_df.head())

#SBI証券のCSVファイルの一番下の行の次の行に楽天証券のCSVファイルをマージする
merged_df = pd.concat([sbi_df, rakuten_df])

#8列目から11列目の列を削除する
merged_df = merged_df.drop(merged_df.columns[[7, 8, 9, 10]], axis=1)

# マージ結果をCSVファイルに保存
merged_df.to_csv(merged_file_path, index=False)

# 結果を確認するために最初の数行を表示
print(merged_df.head())


