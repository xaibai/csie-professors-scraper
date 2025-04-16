import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from sqlalchemy import create_engine
import json

# 設定Selenium無頭模式
options=Options()
options.headless = True
driver=webdriver.Chrome(options=options)

driver.get('https://csie.asia.edu.tw/zh_tw/associate_professors_2')
# 等待頁面加載
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,'i-member-list'))
)
# 滾動頁面以確保所有資料載入
for _ in range(5):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)

# 抓取教師資料
professors=[]
try:
    # 找到所有教授區塊
    member_lists=driver.find_elements(By.CLASS_NAME,'i-member-list')
    for member_list in member_lists:
        teacher_elements=member_list.find_elements(By.CLASS_NAME,'i-member-item-inner.clearfix')
        print(f"找到{len(teacher_elements)}位教授")  # 打印找到的教授數量
        for teacher in teacher_elements:
            try:
                name=teacher.find_element(By.CSS_SELECTOR,'.i-member-value.member-data-value-name').text
                expertise=teacher.find_element(By.CSS_SELECTOR,'.i-member-value.member-data-value-7').text
                professors.append({'Name':name,'Expertise':expertise})
            except Exception as e:
                print(f"忽略錯誤:{e}")
except Exception as e:
    print(f"發生錯誤: {e}")
# 打印抓取到的教授資料
print(professors)

# 關閉網頁
driver.quit()

# 存成CSV
df=pd.DataFrame(professors)
df.to_csv('csie_professors.csv',index=False, encoding='utf-8-sig')

# 存成JSON
with open('csie_professors.json','w',encoding='utf-8') as f:
    json.dump(professors,f,ensure_ascii=False,indent=2)

# 儲存成 SQLite
db_engine=create_engine('sqlite:///csie_professors.db')
try:
    df.to_sql('professors',con=db_engine,if_exists='replace',index=False)
except Exception as e:
    print(f"無法寫入資料庫: {e}")
    
print("完成資料抓取與儲存")
