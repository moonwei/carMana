from extensions import db
from datetime import datetime

class Camera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200))  # 新增：相机位置
    ip_address = db.Column(db.String(15))  # 新增：IP地址
    username = db.Column(db.String(50))  # 新增：用户名
    password = db.Column(db.String(50))  # 新增：密码
    status = db.Column(db.String(20), default='offline')
    last_heartbeat = db.Column(db.DateTime)
    last_status_report = db.Column(db.DateTime)
    cpu_usage = db.Column(db.Float)
    memory_usage = db.Column(db.Float)
    disk_usage = db.Column(db.Float)
    temperature = db.Column(db.Float)

class Whitelist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(20), nullable=False, unique=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

class Recognition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camera_id = db.Column(db.Integer, db.ForeignKey('camera.id'), nullable=False)
    plate_number = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    confidence = db.Column(db.Float)
    image_url = db.Column(db.String(200))

# 移除这行，我们将在 app.py 中创建表
# db.create_all()
