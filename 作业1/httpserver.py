from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from db_connection import MySQLDatabase
import os
import uvicorn

app = FastAPI()

# 初始化数据库
db = MySQLDatabase(user='root', password='123456', host='127.0.0.1', database='trainingDB', port=3208)
db.connect()
db.create_database()
db.use_database()

@app.get("/query_by_image/{image_name}")
def query_by_image(image_name: str):
    result = db.query_data_by_image(image_name)
    if result:
        # 构建图片的本地HTTP地址
        image_http_address = f"http://localhost:8000/images/{os.path.basename(result['image_path'])}"
        result['image_http_address'] = image_http_address
        return result
    else:
        raise HTTPException(status_code=404, detail="Image not found")

@app.get("/images/{image_name}")
def get_image(image_name: str):
    image_path = os.path.join(db.front_str, 'image', image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        raise HTTPException(status_code=404, detail="Image not found")

def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)
