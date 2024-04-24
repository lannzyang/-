import tkinter as tk
import webbrowser

def open_url(url):
    webbrowser.open("https://vip.bljiex.com/?v=" + url)

def load_urls_from_file(filename):
    urls = []
    with open(filename, 'r') as file:
        content = file.readlines()
        title = content[0].strip()  # 获取标题
        urls = [line.strip() for line in content[1:]]  # 获取URL列表
    return title, urls

def create_buttons(root, title, urls):
    root.title(title)  # 设置窗口标题

    row = 1
    col = 0
    for idx, url in enumerate(urls, start=1):
        if idx % 10 == 0:  # 每行最多显示十个按钮
            row += 1
            col = 0
        button = tk.Button(root, text=f"第{idx}集", command=lambda u=url: open_url(u))
        button.grid(row=row, column=col, padx=5, pady=5)
        col += 1

def main():
    root = tk.Tk()

    # 加载URL文件
    filename = "log.txt"  # 指定要加载的文件名
    title, urls = load_urls_from_file(filename)

    # 创建按钮
    create_buttons(root, title, urls)

    root.mainloop()

if __name__ == "__main__":
    main()
