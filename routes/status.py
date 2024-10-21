from flask import Blueprint, request, jsonify
from models import db, Camera
from datetime import datetime

bp = Blueprint('status', __name__, url_prefix='/api')

@bp.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.json
    timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S')
    sn = data['sn']
    
    camera = Camera.query.filter_by(serial_number=sn).first()
    if camera:
        camera.status = 'online'
        camera.last_heartbeat = timestamp
        db.session.commit()
        return jsonify({"code": 0, "msg": "success"}), 200
    else:
        return jsonify({"code": 1, "msg": "Camera not found"}), 404

@bp.route('/check', methods=['GET'])
def check_status():
    cameras = Camera.query.all()
    current_time = datetime.utcnow()
    for camera in cameras:
        if camera.last_heartbeat and (current_time - camera.last_heartbeat).total_seconds() > 300:  # 5分钟没有心跳就认为离线
            camera.status = 'offline'
    db.session.commit()
    return jsonify([{"id": c.id, "name": c.name, "status": c.status} for c in cameras])

@bp.route('/<int:camera_id>', methods=['GET'])
def get_camera_status(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    # 这里应该从实际相机获取详细状态
    status = {
        "online": camera.status == 'online',
        "ip_address": camera.ip_address,
        "last_heartbeat": camera.last_heartbeat.strftime('%Y-%m-%d %H:%M:%S') if camera.last_heartbeat else None,
        "cpu_usage": "30%",  # 示例数据
        "memory_usage": "50%",  # 示例数据
        "disk_space": "70%"  # 示例数据
    }
    return jsonify(status)

@bp.route('/status', methods=['POST'])
def report_status():
    data = request.json
    camera = Camera.query.filter_by(serial_number=data['sn']).first()
    if not camera:
        return jsonify({"code": 1, "msg": "Camera not found"}), 404

    camera.last_status_report = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S')
    camera.cpu_usage = data['cpu']
    camera.memory_usage = data['memory']
    camera.disk_usage = data['disk']
    camera.temperature = data['temperature']

    db.session.commit()

    return jsonify({"code": 0, "msg": "success"})
