from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from extensions import db
from models import Recognition, Camera, Whitelist
from datetime import datetime

bp = Blueprint('recognition', __name__, url_prefix='/recognition')

@bp.route('/', methods=['POST'])
def add_recognition():
    data = request.json
    camera = Camera.query.filter_by(serial_number=data['sn']).first()
    if not camera:
        return jsonify({"code": 1, "msg": "Camera not found"}), 404
    
    new_recognition = Recognition(
        camera_id=camera.id,
        plate_number=data['plateNumber'],
        timestamp=datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S'),
        confidence=data['confidence'],
        image_url=data['imageUrl']
    )
    db.session.add(new_recognition)
    db.session.commit()

    # 检查是否在白名单中
    whitelist = Whitelist.query.filter_by(plate_number=data['plateNumber']).first()
    gate_control = "open" if whitelist else "close"

    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "gateControl": gate_control
        }
    }), 201

@bp.route('/', methods=['GET'])
def list_recognitions():
    recognitions = Recognition.query.all()
    return render_template('recognitions.html', recognitions=recognitions)

@bp.route('/<int:recognition_id>', methods=['GET'])
def get_recognition(recognition_id):
    recognition = Recognition.query.get_or_404(recognition_id)
    return jsonify({
        "id": recognition.id,
        "camera_id": recognition.camera_id,
        "plate_number": recognition.plate_number,
        "timestamp": recognition.timestamp.isoformat(),
        "confidence": recognition.confidence,
        "image_url": recognition.image_url
    })

@bp.route('/trigger', methods=['POST'])
def trigger_recognition():
    data = request.json
    camera = Camera.query.filter_by(ip_address=data['camera_ip']).first()
    if not camera:
        return jsonify({"message": "未找到相应的相机"}), 404
    
    # 这里应该向相机发送触发识别的命令
    # 假设相机会在识别后调用 add_recognition 接口
    
    return jsonify({"message": "已触发车牌识别"})

@bp.route('/image/<int:recognition_id>', methods=['GET'])
def get_recognition_image(recognition_id):
    recognition = Recognition.query.get_or_404(recognition_id)
    # 这里应该返回实际的图片文件
    # 为了示例，我们只返回图片路径
    return jsonify({"image_path": recognition.image_path})
