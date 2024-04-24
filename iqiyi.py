import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import os
import webbrowser
def open_url(url):
    webbrowser.open("https://vip.bljiex.com/?v="+url)

def create_buttons_from_file(filename,name):
    root = tk.Tk()
    root.title(name)

    urls = []
    with open(filename, 'r') as file:
        urls = [line.strip() for idx, line in enumerate(file.readlines()) if idx != 0]

    row_num = 0
    col_num = 0
    for idx, url in enumerate(urls, start=1):
        button = tk.Button(root, text=f"第{idx}集", command=lambda u=url: open_url(u))
        button.grid(row=row_num, column=col_num, padx=5, pady=5)
        col_num += 1
        if col_num == 10:  # 每行十个按钮
            row_num += 1
            col_num = 0

    root.mainloop()
def lis(url,title):
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--mute-audio")
    edge_options.add_argument("--driver-path=./msedgedriver.exe")
    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(4)
    driver.get(url)
    l = 0  # 判断是否成功
    if l == 0:
        try:
            driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/a/div/div[3]').click()
            try:
                tr = driver.find_element(By.XPATH,'//*[@id="_tvg_layer_body_"]/div[1]/div[2]').find_elements(By.TAG_NAME,'div')
            except:
                pass
            if tr:
                try:
                    os.remove('log.txt')
                except:
                    pass
                with open('log.txt', 'a') as f:
                    f.write(title+'\n')
                    for tt in tr:
                        try:
                            tt.click()
                        except:
                            pass
                        ts = driver.find_elements(By.XPATH, '//*[@id="_tvg_layer_body_"]/div[1]/div[3]/div')
                        for t in ts:
                            t.click()
                            time.sleep(0.5)
                            current_url = driver.current_url
                            f.write(current_url + '\n')
            l = 1
        except:
            pass
    if l == 0:
        try:
            ols = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]').find_elements(By.TAG_NAME,'div')
            if ols:
                try:
                    os.remove('log.txt')
                except:
                    pass
                with open('log.txt', 'a') as f:
                    f.write(title+'\n')
                    for ol in ols:
                        try:
                            ol.click()
                        except:
                            pass
                        rts = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]').find_elements(By.TAG_NAME,'a')
                        for rt in rts:
                            rt.click()
                            time.sleep(0.5)
                            current_url = driver.current_url
                            f.write(current_url + '\n')
                l = 1
        except:
            pass
    driver.quit()
    create_buttons_from_file('log.txt',name)

def open_new_window():#打开新的tk
    new_window = tk.Toplevel()
    new_window.geometry("400x100+500+500")
    new_window.title("说明")
    label = tk.Label(new_window, text="集数可能会多，不用在意",font=('Arial', 20))
    label.pack()
def play_episode(url):
    driver = webdriver.Edge(options=edge_options)
    driver.get(url)
    wait_for_completion(driver)
    driver.quit()

def wait_for_completion(driver):
    while True:
        if driver.current_url == 'about:blank':
            break
        time.sleep(1)
#等待用户播放完视频或者关闭
def play_movie(url):
    # 使用无头模式打开链接并等待加载完成
    driver_headless = get_headless_driver()
    driver_headless.get(url)
    driver_headless.implicitly_wait(10)
    new_url = driver_headless.current_url
    driver_headless.quit()
    
    # 使用有头模式打开新链接
    driver = get_normal_driver()
    driver.get("https://vip.bljiex.com/?v="+new_url)
    wait_for_completion(driver)
def get_headless_driver():
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--mute-audio")
    edge_options.add_argument("--driver-path=./msedgedriver.exe")
    return webdriver.Edge(options=edge_options)

def get_normal_driver():
    edge_options = Options()
    edge_options.add_argument("--driver-path=./msedgedriver.exe")
    return webdriver.Edge(options=edge_options)

def on_button_click(url):
    messagebox.showinfo("播放", f"将要播放的链接为：{url}")
    play_episode(url)
def find_url1(name):#电视剧
    url = f'https://www.iqiyi.com/search/{name}.html'
    driver.get(url)

    driver.find_element(By.XPATH, '//*[@id="search_item_1"]/div[3]/div/div/span').click()

    elements = driver.find_elements(By.XPATH, '//*[@id="search_item_1"]/div[3]/div//a')
    urls = [element.get_attribute('href') for element in elements]
    with open('log.txt','w') as f:
        f.write(name+'\n')
        f.writelines(url + '\n' for url in urls)
    urls2 = ["https://vip.bljiex.com/?v="+u for u in urls]
    driver.quit()
    return urls2
def find_url2(name):#电影
    url = f'https://www.iqiyi.com/search/{name}.html'
    driver.get(url)
    url_element  = driver.find_element(By.XPATH,'//*[@id="search_item_1"]/div/div[1]/a')
    url = url_element.get_attribute('href')
    urls2 = ["https://vip.bljiex.com/?v="+url]
    driver.quit()
    return urls2
def find_url3(name):#系列
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--driver-path=./msedgedriver.exe")
    driver = webdriver.Edge(options=edge_options)

    url = f"https://www.iqiyi.com/search/{name}.html"
    driver.get(url)

    parent_div = driver.find_element(By.XPATH, '//*[@id="card_page"]/div/div[1]/div[1]/div/div[3]/div/div')
    child_divs = parent_div.find_elements(By.XPATH, './div')

    movie_info_list = []

    for div in child_divs:
        try:
            mm_elements = div.find_elements(By.XPATH, './div[1]//*')  # 使用.//*查找所有子元素
            mm = None  # 初始化mm为None，表示未找到包含'集全'的元素
            for m in mm_elements:
                text = m.text.strip()  # 获取元素的文本内容，并去除首尾空白字符
                if '集' in text:
                    mm = 1  # 找到包含'集全'的元素，将mm设置为1
                    break  # 找到后跳出循环
        except:
            mm = None  # 出现异常时，将mm设置为None
        second_div = div.find_element(By.XPATH, './div[2]')  # 找到第二个 div 元素
        first_a = second_div.find_element(By.XPATH, './a[1]')  # 找到第一个 a 元素
        if mm is not None:
            title = first_a.text  # 获取片名
        else:
            title = first_a.text+'(movie)'
        href = first_a.get_attribute('href')  # 获取链接
        movie_info_list.append((title, href))  # 将片名和链接添加到列表中
    driver.quit()
    return movie_info_list
def display_movie_info():#系列的ui
    movie_info_list = urls2
    root = tk.Tk()
    root.title("列表")

    # 显示电影信息
    for idx, (title, href) in enumerate(movie_info_list, start=1):
        label = tk.Label(root, text=f"片名: {title}")
        label.grid(row=idx, column=0, padx=5, pady=5)  # 设置片名的位置和间距
        if title.endswith('(movie)'):# 判断类型
            button = tk.Button(root, text=f"播放电影", command=lambda h=href: play_movie(h))
        else:
            button = tk.Button(root, text=f"解析剧集", command=lambda h=href: lis(h,title))
        button.grid(row=idx, column=1, padx=5, pady=5)  # 设置按钮的位置和间距
    root.mainloop()
if os.name == 'nt': 
    os.system('cls')
else: 
    os.system('clear')
name = input("\033[1;32m输入片名:\033[0m")
edge_options = Options()
edge_options.add_argument("--headless")
edge_options.add_argument("--driver-path=./msedgedriver.exe")
driver = webdriver.Edge(options=edge_options)
oooo = 0 # 判断是否找到url
tv = 0 #判断为电视剧/电影/系列
#多种方法查询地址直到找到为止
if oooo == 0:
    try:
        urls2 = find_url1(name)
        oooo = 1
    except:
        pass
if oooo == 0:
    try:
        urls2 = find_url2(name)
        oooo = 1
        tv = 1
    except:
        pass
if oooo == 0:
    try:
        urls2 = find_url3(name)
        oooo = 1
        tv = 2
    except:
        pass
#信息查询完毕

edge_options = Options()
edge_options.add_argument("--driver-path=./msedgedriver.exe")
if tv == 0:#电视剧的界面布局
    root = tk.Tk()
    root.title(name) 
    for idx, url in enumerate(urls2, start=1):
        row_num, col_num = divmod(idx - 1, 10)
        button = tk.Button(root, text=f"第{idx}集", width=6, height=3, font=('Arial', 10), command=lambda u=url: on_button_click(u))
        button.grid(row=row_num, column=col_num, padx=5, pady=5)

    # 创建说明按钮
    button_explain = tk.Button(root, text="说明", width=6, height=3, font=('Arial', 10), command=open_new_window)
    button_explain.grid(row=row_num + 1, column=0, padx=5, pady=5)  
    root.mainloop()
elif tv ==1 : # 电影的界面布局
    root = tk.Tk()
    root.title(name)
    root.geometry("400x100+1000+500")

    for idx, url in enumerate(urls2, start=1):
        row_num, col_num = divmod(idx - 1, 10)
        button = tk.Button(root, text=f"电影{idx}", width=6, height=3, font=('Arial', 10), command=lambda u=url: on_button_click(u))
        button.grid(row=row_num, column=col_num, padx=5, pady=5) 

    root.mainloop()
elif tv ==2 :#系列布局
    display_movie_info()
            
