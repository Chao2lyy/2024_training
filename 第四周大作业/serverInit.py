from db_connection import MySQLDatabase
from download_extract import download_and_extract_zip
import json
import threading
import httpserver as server

if __name__ == "__main__":
    url = 'https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16206132983635968.zip?authorization=bce-auth-v1/62ff93831d5840338d0fcc9585430b3a/2024-06-18T05:11:09Z/604800//86e8ad98e8f6e6080922c47d5595c948fdf5f88b2e2b050a5dfbdfee463a90d0'
    extract_to = 'download'
    
    print("Starting download and extraction...")
    download_and_extract_zip(url, extract_to=extract_to)
    print("Download and extraction completed.")

    db = MySQLDatabase(user='root', password='123456', host='127.0.0.1', database='trainingDB', port=3208)

    db.connect()
    if db.connection and db.cursor:
        db.create_database()
        db.use_database()

        db.create_table()

        # 读取并解析JSON文件
        with open('download/single-vehicle-side-example/data_info.json', 'r') as file:
            data = json.load(file)

        db.insert_json_data(data)

        #db.close()

    # 启动FastAPI服务
    print("Starting FastAPI server...")
    server_thread = threading.Thread(target=server.start_server, daemon=True)
    server_thread.start()

    # 保持主线程活动以确保服务器继续运行
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down server...")
