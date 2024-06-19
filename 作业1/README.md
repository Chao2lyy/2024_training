## 自动驾驶数据加工与清洗
### 整体流程
+ 步骤1（数据下载、初始化数据库、启动服务器）
`python serverinit.py` 
如下
```Connection successful
Database 'trainingDB' created or already exists
Using database 'trainingDB'
Starting download and extraction...
single-vehicle-side-example_16206132983635968.zip: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 203M/203M [00:19<00:00, 11.2MB/s]
解压缩: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 433/433 [00:01<00:00, 318.88it/s]
文件已下载并解压至 /home/hyq/work/2024_training/作业1/download
Download and extraction completed.
Connection successful
Database 'trainingDB' created or already exists
Using database 'trainingDB'
Table created successfully
calib/camera_intrinsic/000000.json 200
Data inserted successfully
calib/camera_intrinsic/000001.json 200
Data inserted successfully
calib/camera_intrinsic/000002.json 200
Data inserted successfully
...
Starting FastAPI server...
INFO:     Started server process [10186]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
+ 步骤2（启动客户端）
`python client.py`
如下（输入image名称进行查询或输入exit退出）
```
Enter image name (or 'exit' to quit): 000001.jpg
{
    "calib_lidar_to_camera_json": {
        "rotation": [
            [
                0.006283,
                -0.999979,
                -0.001899
            ],
            [
                -0.005334,
                0.001865,
                -0.999984
            ],
            [
                0.999966,
                0.006293,
                -0.005322
            ]
        ],
        "translation": [
            [
                -0.298036
            ],
            [
                -0.666812
            ],
            [
                -0.516927
            ]
        ]
    },
    "label_camera_std_json": [
        {
            "type": "Car",
            "alpha": 0.19320927745804112,
            "2d_box": {
                "xmax": 457.211487,
                "xmin": 0,
                "ymax": 661.1854860000001,
                "ymin": 404.296692
            },
            "rotation": -1.570282,
            "3d_location": {
                "x": 32.80635,
                "y": 6.04457,
                "z": -0.8653639
            },
            "3d_dimensions": {
                "h": 2.017057,
                "l": 3.916855,
                "w": 2.197865
            },
            "occluded_state": 2,
            "truncated_state": 0
        }
    ],
    "label_lidar_std_json": [
        {
            "type": "Car",
            "alpha": 0.18958860213516604,
            "2d_box": {
                "xmax": 457.211487,
                "xmin": 0,
                "ymax": 661.1854860000001,
                "ymin": 404.296692
            },
            "rotation": -1.556342,
            "3d_location": {
                "x": 32.74374,
                "y": 6.378814,
                "z": -0.9854571
            },
            "3d_dimensions": {
                "h": 2.031636,
                "l": 4.218545,
                "w": 2.11253
            },
            "occluded_state": 2,
            "truncated_state": 0
        }
    ],
    "image_path": "image/000001.jpg",
    "image_http_address": "http://localhost:8000/images/000001.jpg"
}
```
可复制image_http_address中的链接下载该图片
### 数据库设计
**表名：data_info**

该表用于存储与图像、点云数据及其相关校准和标签数据的信息。
**表结构**

列名|数据类型|约束条件|描述
-|-|-|-
id|	INT|	PRIMARY KEY, AUTO_INCREMENT|	自动增长的主键，用于唯一标识每条记录
image_path|	VARCHAR(255)|	NOT NULL|	图像文件的路径
image_timestamp|	VARCHAR(255)|	NOT NULL|	图像的时间戳
pointcloud_path|	VARCHAR(255)|	NOT NULL|	点云文件的路径
point_cloud_stamp|	VARCHAR(255)|	NOT NULL|	点云的时间戳
calib_camera_intrinsic_path|	VARCHAR(255)|	NOT NULL|	相机内参文件的路径
calib_lidar_to_camera_path|	VARCHAR(255)|	NOT NULL|	激光雷达到相机的校准文件路径
label_camera_std_path|	VARCHAR(255)|	NOT NULL|	相机标准标签文件的路径
label_lidar_std_path|	VARCHAR(255)|	NOT NULL|	激光雷达标准标签文件的路径
calib_camera_intrinsic_json|	JSON|	NULL|	相机内参文件的JSON内容
calib_lidar_to_camera_json|	JSON|	NULL|	激光雷达到相机的校准文件的JSON内容
label_camera_std_json|	JSON|	NULL|	相机标准标签文件的JSON内容
label_lidar_std_json|	JSON|	NULL|	激光雷达标准标签文件的JSON内容
image_size|	BIGINT|	NULL|	图像文件的大小（以字节为单位）
pointcloud_size|	BIGINT|	NULL|	点云文件的大小（以字节为单位）


    主键：id 列是主键，自动增长，用于唯一标识每条记录。
    非空约束：image_path、image_timestamp、pointcloud_path、point_cloud_stamp、calib_camera_intrinsic_path、calib_lidar_to_camera_path、label_camera_std_path、label_lidar_std_path 列为非空。
    JSON 列：calib_camera_intrinsic_json、calib_lidar_to_camera_json、label_camera_std_json、label_lidar_std_json 列存储相应文件的内容，以JSON格式存储。
    大小列：image_size 和 pointcloud_size 列存储图像和点云文件的大小（以字节为单位）。
