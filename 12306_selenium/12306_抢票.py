from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
ts1 = time.time()
wb = webdriver.Chrome()
wb.implicitly_wait(10)
wb.get("https://kyfw.12306.cn/otn/resources/login.html")
#-----------------扫码登录------------------------------#
link = wb.find_element(By.LINK_TEXT,"扫码登录")    
# 执行JavaScript点击事件  
wb.execute_script("arguments[0].click();", link)  
#--------------------------------------------------------#
wb.find_element(By.XPATH,'//*[@id="toolbar_Div"]/div[1]/div[2]/ul/li[2]/a').click()
wb.find_element(By.XPATH,'//*[@id="megamenu-3"]/div[1]/ul/li[1]/a').click()
time.sleep(1)
#----------------------输入地址----------------------------#
el = wb.find_element(By.ID,"fromStationText")
el.click()
# try:
#     el.clear()
# except:
#     pass
el.send_keys("重庆")  # 选择起始地点
wb.find_element(By.ID,'citem_0').click()
#----------------------------------------------------#
el = wb.find_element(By.ID,"toStationText")
el.click()
# try:
#     el.clear()
# except:
#     pass
el.send_keys("成都")  # 选择到达地点
wb.find_element(By.ID,'citem_0').click()
#--------------------地址输入完毕-----------------------#

#-------------------------查询并选择日期------------------------#
el = wb.find_element(By.ID,"train_date")
el.click()
el.clear()
el.send_keys("2023-12-18")#选择时间
# time.sleep(0.5)
wb.find_element(By.ID,'query_ticket').click()
# time.sleep(0.5)
# wb.switch_to.window(wb.window_handles[-1])切换窗口
#---------------------查询完毕------------------------#
#----------------------订购-------------------------#
# wait = WebDriverWait(wb, 10)
# tbody = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="queryLeftTable"]')))
trs = wb.find_elements(By.XPATH, "//tbody[@id='queryLeftTable']//tr[position() mod 2 = 1]")
for tr in trs:
    try:
        texts = tr.find_element(By.XPATH, './td[4]').text
    except:
        continue
    if texts == '有' or texts.isdigit():
        name = tr.find_element(By.XPATH,'./td[1]/div/div/div/a').text
        print(f"车次为：{name}")
        time_start = tr.find_element(By.XPATH,'./td[1]/div/div[3]/strong[1]').text
        time_arrive = tr.find_element(By.XPATH,'./td[1]/div/div[3]/strong[2]').text
        time_all = tr.find_element(By.XPATH,'./td[1]/div/div[4]/strong[1]').text
        print(f"发车时间：{time_start}\n到达时间：{time_arrive}\n用时{time_all}")
        tr.find_element(By.XPATH, './td[last()]').click()
        break
# link = wb.find_element(By.XPATH,'//*[@id="ticket_240000K4111E_01_02"]/td[13]/a')
# wb.execute_script("arguments[0].click();", link)
print("列车班次找到")
# time.sleep(1000)
#------------临近车次弹窗检验--------------------------#
# try:
#     link = wb.find_element(By.LINK_TEXT,'确定')
#     wb.execute_script("arguments[0].click();", link)
# except:
#     pass
#------------------订单处理----------------------------------#
ts2 = time.time()
link = wb.find_element(By.XPATH, '//*[@id="normalPassenger_0"]')
wb.execute_script("arguments[0].click();", link)
wb.find_element(By.ID,"submitOrder_id").click()
#-------------座位选择-------------------------------------#
# link = wb.find_element(By.LINK_TEXT,'F')
# wb.execute_script("arguments[0].click();", link)
#---------------------------------------------------------#
link = wb.find_element(By.ID, 'qr_submit_id')
t = 0
while t < 100:
    try:
        link.click()
        t += 1
    except:
        print("订购成功!")
        break
ts3 = time.time()
#看情况加，下面是直接输入乘客信息，上面是选择已经有的乘客
# wb.find_element(By.ID,"passenger_name_1").send_keys("NAME")
# wb.find_element(By.ID,"passenger_id_no_1").send_keys("ID")
# link = wb.find_elementI(By.LINK_TEXT,"提交订单")
# wb.execute_script("arguments[0].click();", link)
ts = ts3 - ts2
print(f"购票用时{ts}")
time.sleep(1100)