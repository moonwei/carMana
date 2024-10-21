from flask import Blueprint, request, jsonify
from models import db, Camera

bp = Blueprint('gate', __name__, url_prefix='/gate')

@bp.route('/open/<int:camera_id>', methods=['POST'])
def open_gate(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    # 这里应该向相机发送开闸命令
    return jsonify({"message": f"已向相机 {camera.name} 发送开闸命令"})

@bp.route('/close/<int:camera_id>', methods=['POST'])
def close_gate(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    # 这里应该向相机发送关闸命令
    return jsonify({"message": f"已向相机 {camera.name} 发送关闸命令"})

@bp.route('/status/<int:camera_id>', methods=['GET'])
def gate_status(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    # 这里应该从相机获取实际的闸门状态
    status = {
        "is_open": True,  # 示例数据
        "last_action_time": "2023-05-20 14:30:00"  # 示例数据
    }
    return jsonify(status)
