# Asia University CSIE 教師資料爬蟲

本專案使用 Python 的 Selenium 自動爬取亞洲大學資訊工程學系副教授的「姓名」與「研究專長」，並儲存為 CSV、JSON、SQLite 三種格式。

---

## 📌 功能說明

- 自動開啟網站並滾動頁面
- 擷取副教授姓名與研究專長
- 輸出資料為：
  - `csie_professors.csv`
  - `csie_professors.json`
  - SQLite 資料庫 `csie_professors.db`，表名為 `professors`

---

## 🛠 環境與安裝

```bash
pip install -r requirements.txt
需另行安裝：

Google Chrome 瀏覽器

ChromeDriver（版本需對應你的 Chrome）

🚀 執行方式
bash
Copy
Edit
python csie_scraper.py
執行後將自動：

開啟網站並滾動頁面

擷取所有副教授資料

輸出成 CSV、JSON 與 SQLite 格式的資料檔案

📂 輸出檔案說明
csie_professors.csv
UTF-8 with BOM 格式，可直接用 Excel 開啟：

Name	Expertise
王小明教授	機器學習、人工智慧

csie_professors.json
json
Copy
Edit
[
  {
    "Name": "王小明教授",
    "Expertise": "機器學習、人工智慧"
  }
]
csie_professors.db
內含 professors 資料表，可用 SQLite 工具（如 DB Browser for SQLite）查詢。

❗ 注意事項
若網站結構變動，需手動調整爬蟲中的 CSS 選擇器。

為無頭模式執行，不會打開實體瀏覽器視窗。

請尊重網站服務條款，勿頻繁大量抓取。

📜 授權
本專案僅供學術與學習用途，請勿用於商業行為。

yaml
Copy
Edit

---
