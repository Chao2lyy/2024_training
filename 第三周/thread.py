import threading  
import requests  
import os  
from urllib.parse import urlparse  
  
# 锁
lock = threading.Lock()  
  
def get_filename_from_url(url):  
    # 域名解析，使用域名作为文件名 
    parsed_url = urlparse(url)  
    domain = parsed_url.netloc.replace('www.', '')  
    return f"{domain}_html.txt"  
  
def download_html(url):  
    filename = get_filename_from_url(url)  
    try:  
        response = requests.get(url, timeout=5)  
          
        if response.status_code == 200:   
            with lock:  
                print(f"Downloaded {url} successfully.")  
  
            # 打开文件并写入HTML内容  
            with open(filename, 'w', encoding='utf-8') as f:  
                f.write(response.text)  
  
            print(f"HTML saved to {filename}")  
        else:  
            print(f"Failed to download {url}. Status code: {response.status_code}")  
    except requests.RequestException as e:  
        print(f"An error occurred while downloading {url}: {e}")  
  
# 线程列表  
threads = []  
  
# 下载的url
urls = ['http://www.baidu.com', 'http://www.bing.com']  
  

for url in urls:  
    t = threading.Thread(target=download_html, args=(url,))  
    t.start()  
    threads.append(t)  

for t in threads:  
    t.join()  
  
print("All threads finished.")