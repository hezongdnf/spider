import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opt = Options()
opt.add_argument("--headless")

web = Chrome()
web.get("https://cnki.net")

web.find_element_by_xpath('//*[@id="txt_SearchText"]').send_keys("中国管理科学", Keys.ENTER)

time.sleep(10)

table = web.find_element_by_xpath('//*[@id="gridTable"]/table')

trs = table.find_elements_by_class_name("odd")

ls = []

for tr in trs:
    ls.append(tr.text)

print(ls)