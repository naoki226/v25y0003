from bs4 import BeautifulSoup
import pandas as pd

# HTMLファイルを読み込む
with open("hyou.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# テーブルを取得
table = soup.find("table")
data = []

# 各行から都道府県と優勝回数（計）を抽出
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    if len(cols) >= 5:
        prefecture = cols[1].text.strip()
        total_wins = cols[4].text.strip()
        data.append([prefecture, total_wins])

# DataFrameに変換
df = pd.DataFrame(data, columns=["都道府県", "優勝回数（計）"])

# CSVファイルとして保存（Excelで開けるようにUTF-8 BOM付きで保存）
df.to_csv("yusho_counts.csv", index=False, encoding="utf-8-sig")

print("✅ CSVファイルを保存しました: yusho_counts.csv")
