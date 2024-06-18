import requests
import zipfile
import os
from tqdm import tqdm
from urllib.parse import urlparse, unquote

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return unquote(filename)

def download_and_extract_zip(url, extract_to='.'):
    # 获取有效文件名
    local_filename = get_filename_from_url(url)
    zip_path = os.path.join(extract_to, local_filename)

    # 检查文件是否已经下载并解压过
    if os.path.exists(extract_to) and os.listdir(extract_to):
        print(f"文件已存在于 {os.path.abspath(extract_to)}，跳过下载和解压。")
        return

    # 创建目录
    os.makedirs(extract_to, exist_ok=True)
    
    # 下载文件
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(zip_path, 'wb') as file, tqdm(
        desc=local_filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            bar.update(len(chunk))
    
    # 解压文件
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist()), desc='解压缩'):
            zip_ref.extract(member=file, path=extract_to)
    
    # 删除下载的zip文件
    os.remove(zip_path)

    print(f"文件已下载并解压至 {os.path.abspath(extract_to)}")

url = 'https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16206132983635968.zip?authorization=bce-auth-v1/62ff93831d5840338d0fcc9585430b3a/2024-06-18T05:11:09Z/604800//86e8ad98e8f6e6080922c47d5595c948fdf5f88b2e2b050a5dfbdfee463a90d0'
download_and_extract_zip(url, extract_to='/home/hyq/work/2024_training/download')