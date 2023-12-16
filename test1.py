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
# 楽天証券の配当金明細書のCSVファイルを読み込む
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


