from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
from PIL import Image, ImageTk
from io import BytesIO
import requests

#爬电视剧
def open_link(url):
    webbrowser.open("https://vip.bljiex.com/?v="+url)
def create_buttons(links, title, text, img_url):
    root = tk.Tk()
    root.title(title)

    response = requests.get(img_url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    img = img.resize((300, 300))  # 调整图片尺寸
    photo = ImageTk.PhotoImage(img)

    label_image = tk.Label(root, image=photo)
    label_image.pack(side=tk.LEFT, padx=10, pady=10)

    label_text = tk.Label(root, text=text)
    label_text.pack(side=tk.TOP, padx=10, pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=10)

    for i, link in enumerate(links):
        button = tk.Button(button_frame, text=f"第{i+1}集", command=lambda l=link: open_link(l))
        button.grid(row=i // 6, column=i % 6, padx=5, pady=5)

    root.mainloop()
def find_1(name):
    urls_list = []
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--driver-path=./msedgedriver.exe")
    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(4)
    url = f'https://so.mgtv.com/so?k={name}&lastp=ch_home'
    driver.get(url)
    text = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/p[2]').text
    img_url = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div/div/a/img').get_attribute('src')
    try:
        for s in driver.find_elements(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]//a'):
            if s.text == '全部':
                s.click()
    except:
        try:
            for s in driver.find_elements(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]//a'):
                if s.text == '全部':
                    s.click()
        except:
            for s in driver.find_elements(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]//a'):
                if s.text == '全部':
                    s.click()
    #三次查找
    
    urls = driver.find_elements(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/a')
    if urls is not []:
        pass
    else:
        urls = driver.find_elements(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/a')
    try:
        os.remove('log.txt')
    except:
        pass
    with open('log.txt','a') as f:
        f.write(name+'\n')
        for url in urls:
            ul = url.get_attribute('href')
            f.write(ul+'\n')
            urls_list.append(ul)
    driver.quit()
    m = 1
    return urls_list,name,m,text,img_url
#怕电视剧结束
 
#扒电影

def display_image_with_text(img_url, text,title,video_url):
    root = tk.Tk()  # 创建根窗口
    root.title(title)

    response = requests.get(img_url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    img = img.resize((300, 300))  # 调整图片尺寸
    photo = ImageTk.PhotoImage(img)

    label_image = tk.Label(root, image=photo)
    label_image.pack(side=tk.LEFT, padx=10, pady=10)

    label_text = tk.Label(root, text=text)
    label_text.pack(side=tk.TOP)
    button = tk.Button(root, text="播放", command=lambda l=video_url: open_link(l))
    button.pack(side=tk.TOP, pady=10)

    root.mainloop()
#电影的tk
def find_2(name):
    urls_list = []
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--driver-path=./msedgedriver.exe")
    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(4)
    url = f'https://so.mgtv.com/so?k={name}&lastp=ch_home'
    driver.get(url)
    url = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/a').get_attribute('href')
    image_url = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div/div/a/img').get_attribute('src')
    info = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/p[2]').text
    m = 1 
    return url,image_url,info,m

#扒电影结束
if os.name == 'nt': 
    os.system('cls')
else: 
    os.system('clear')
name = input("\033[1;32m输入片名:\033[0m")
#电视剧界面
m = 0
if m == 0:
    try:
        links, title,m,text,img_url= find_1(name)
        if m == 1:
            create_buttons(links,title,text,img_url)
    except:
        pass
#电影界面
if m == 0:
    try:
        url, img_url, info, m= find_2(name)
        if m == 1:
            display_image_with_text(img_url,info,name,url)
    except:
        pass