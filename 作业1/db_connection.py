import mysql.connector
from mysql.connector import errorcode
import json
import os

class MySQLDatabase:
    def __init__(self, user, password, host, database, port=3208):
        self.config = {
            'user': user,
            'password': password,
            'host': host,
            'database': database,
            'port': port,
            'raise_on_warnings': True
        }
        self.connection = None
        self.cursor = None
        self.front_str='download/single-vehicle-side-example/'

    def connect(self):
        '''数据库连接'''
        try:
            self.connection = mysql.connector.connect(
                user=self.config['user'],
                password=self.config['password'],
                host=self.config['host'],
                port=self.config['port']
            )
            self.cursor = self.connection.cursor()
            print("Connection successful")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Access denied: Username or password incorrect")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            elif err.errno == errorcode.CR_CONNECTION_ERROR:
                print("Connection error: Please check the network connection or MySQL server status")
            elif err.errno == errorcode.CR_SERVER_LOST:
                print("Lost connection to MySQL server")
            else:
                print(f"Error: {err}")
            self.connection = None
            self.cursor = None

    def close(self):
        '''关闭数据库连接'''
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")
    
    def create_database(self):
        '''创建数据库'''
        if self.cursor:
            try:
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.config['database']}")
                print(f"Database '{self.config['database']}' created or already exists")
            except mysql.connector.Error as err:
                print(f"Failed creating database: {err}")
        else:
            print("No connection to the database")

    def use_database(self):
        '''使用数据库'''
        if self.cursor:
            try:
                self.cursor.execute(f"USE {self.config['database']}")
                print(f"Using database '{self.config['database']}'")
            except mysql.connector.Error as err:
                print(f"Database '{self.config['database']}' does not exist: {err}")
        else:
            print("No connection to the database")

    def create_table(self):
        '''创建数据表'''
        if self.cursor:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS data_info (
                id INT AUTO_INCREMENT PRIMARY KEY,
                image_path VARCHAR(255),
                image_timestamp VARCHAR(255),
                pointcloud_path VARCHAR(255),
                point_cloud_stamp VARCHAR(255),
                calib_camera_intrinsic_path VARCHAR(255),
                calib_lidar_to_camera_path VARCHAR(255),
                label_camera_std_path VARCHAR(255),
                label_lidar_std_path VARCHAR(255),
                calib_camera_intrinsic_json JSON,
                calib_lidar_to_camera_json JSON,
                label_camera_std_json JSON,
                label_lidar_std_json JSON,
                image_size BIGINT,
                pointcloud_size BIGINT
            )
            '''
            try:
                self.cursor.execute(create_table_query)
                print("Table created successfully")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        else:
            print("No connection to the database")

    def insert_json_data(self, data):
        '''读取json插入数据'''
        for entry in data:
            # 读取关联的JSON文件内容
            calib_camera_intrinsic_json = self.read_json_file(self.front_str+entry['calib_camera_intrinsic_path'])
            print(entry['calib_camera_intrinsic_path'],200)
            calib_lidar_to_camera_json = self.read_json_file(self.front_str+entry['calib_lidar_to_camera_path'])
            label_camera_std_json = self.read_json_file(self.front_str+entry['label_camera_std_path'])
            label_lidar_std_json = self.read_json_file(self.front_str+entry['label_lidar_std_path'])

            # 获取二进制文件的大小
            image_size = self.get_file_size(self.front_str+entry['image_path'])
            pointcloud_size = self.get_file_size(self.front_str+entry['pointcloud_path'])

            if self.cursor:
                insert_query = '''
                INSERT INTO data_info (
                    image_path,
                    image_timestamp,
                    pointcloud_path,
                    point_cloud_stamp,
                    calib_camera_intrinsic_path,
                    calib_lidar_to_camera_path,
                    label_camera_std_path,
                    label_lidar_std_path,
                    calib_camera_intrinsic_json,
                    calib_lidar_to_camera_json,
                    label_camera_std_json,
                    label_lidar_std_json,
                    image_size,
                    pointcloud_size
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
                values = (
                    entry['image_path'],
                    entry['image_timestamp'],
                    entry['pointcloud_path'],
                    entry['point_cloud_stamp'],
                    entry['calib_camera_intrinsic_path'],
                    entry['calib_lidar_to_camera_path'],
                    entry['label_camera_std_path'],
                    entry['label_lidar_std_path'],
                    json.dumps(calib_camera_intrinsic_json),
                    json.dumps(calib_lidar_to_camera_json),
                    json.dumps(label_camera_std_json),
                    json.dumps(label_lidar_std_json),
                    image_size,
                    pointcloud_size
                )
                try:
                    self.cursor.execute(insert_query, values)
                    self.connection.commit()
                    print("Data inserted successfully")
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
            else:
                print("No connection to the database")

    def read_json_file(self, file_path):
        '''读取json'''
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}

    def get_file_size(self, file_path):
        '''获取文件大小'''
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
        return 0

    def update_data(self, record_id, data):
        '''更新数据'''
        # 读取关联的JSON文件内容
        calib_camera_intrinsic_json = self.read_json_file(self.front_str+data['calib_camera_intrinsic_path'])
        calib_lidar_to_camera_json = self.read_json_file(self.front_str+data['calib_lidar_to_camera_path'])
        label_camera_std_json = self.read_json_file(self.front_str+data['label_camera_std_path'])
        label_lidar_std_json = self.read_json_file(self.front_str+data['label_lidar_std_path'])

        # 获取二进制文件的大小
        image_size = self.get_file_size(self.front_str+data['image_path'])
        pointcloud_size = self.get_file_size(self.front_str+data['pointcloud_path'])

        if self.cursor:
            update_query = '''
            UPDATE data_info SET
                image_path = %s,
                image_timestamp = %s,
                pointcloud_path = %s,
                point_cloud_stamp = %s,
                calib_camera_intrinsic_path = %s,
                calib_lidar_to_camera_path = %s,
                label_camera_std_path = %s,
                label_lidar_std_path = %s,
                calib_camera_intrinsic_json = %s,
                calib_lidar_to_camera_json = %s,
                label_camera_std_json = %s,
                label_lidar_std_json = %s,
                image_size = %s,
                pointcloud_size = %s
            WHERE id = %s
            '''
            values = (
                data['image_path'],
                data['image_timestamp'],
                data['pointcloud_path'],
                data['point_cloud_stamp'],
                data['calib_camera_intrinsic_path'],
                data['calib_lidar_to_camera_path'],
                data['label_camera_std_path'],
                data['label_lidar_std_path'],
                json.dumps(calib_camera_intrinsic_json),
                json.dumps(calib_lidar_to_camera_json),
                json.dumps(label_camera_std_json),
                json.dumps(label_lidar_std_json),
                image_size,
                pointcloud_size,
                record_id
            )
            try:
                self.cursor.execute(update_query, values)
                self.connection.commit()
                print("Data updated successfully")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        else:
            print("No connection to the database")

    def query_data(self, query):
        '''查询数据'''
        if self.cursor:
            try:
                self.cursor.execute(query)
                results = self.cursor.fetchall()
                for row in results:
                    print(row)
                return results
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        else:
            print("No connection to the database")
        return None

    def delete_data(self, record_id):
        '''删除数据'''
        if self.cursor:
            delete_query = "DELETE FROM data_info WHERE id = %s"
            try:
                self.cursor.execute(delete_query, (record_id,))
                self.connection.commit()
                print("Data deleted successfully")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        else:
            print("No connection to the database")


# if __name__ == "__main__":
#     db = MySQLDatabase(user='root', password='123456', host='127.0.0.1', database='trainingDB', port=3208)

#     db.connect()
#     if db.connection and db.cursor:
#         db.create_database()
#         db.use_database()

#         db.create_table()

#         # 读取并解析JSON文件
#         with open('download/single-vehicle-side-example/data_info.json', 'r') as file:
#             data = json.load(file)

#         db.insert_json_data(data)

#         # 查询数据
#         print("Querying data:")
#         db.query_data("SELECT * FROM data_info")

#         # 更新数据
#         updated_data = {
#             "image_path": "image/000001.jpg",
#             "image_timestamp": "1604988999002000",
#             "pointcloud_path": "velodyne/000001.pcd",
#             "point_cloud_stamp": "1604988999007000",
#             "calib_camera_intrinsic_path": "calib/camera_intrinsic/000001.json",
#             "calib_lidar_to_camera_path": "calib/lidar_to_camera/000001.json",
#             "label_camera_std_path": "label/camera/000001.json",
#             "label_lidar_std_path": "label/lidar/000001.json"
#         }
#         db.update_data(record_id=1, data=updated_data)

#         # 查询数据
#         print("Querying data after update:")
#         db.query_data("SELECT * FROM data_info")

#         # 删除数据
#         db.delete_data(record_id=1)

#         # 查询数据
#         print("Querying data after delete:")
#         db.query_data("SELECT * FROM data_info")

#         db.close()
