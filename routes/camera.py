from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from extensions import db
from models import Camera

bp = Blueprint('camera', __name__, url_prefix='/camera')

@bp.route('/', methods=['GET'])
def list_cameras():
    cameras = Camera.query.all()
    return render_template('cameras.html', cameras=cameras)

@bp.route('/add', methods=['GET', 'POST'])
def add_camera():
    if request.method == 'POST':
        new_camera = Camera(
            name=request.form['name'],
            serial_number=request.form['serial_number'],
            location=request.form['location'],
            ip_address=request.form['ip_address'],
            username=request.form['username'],
            password=request.form['password']
        )
        db.session.add(new_camera)
        db.session.commit()
        return redirect(url_for('camera.list_cameras'))
    return render_template('add_camera.html')

@bp.route('/<int:camera_id>/edit', methods=['GET', 'POST'])
def edit_camera(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    if request.method == 'POST':
        camera.name = request.form['name']
        camera.serial_number = request.form['serial_number']
        camera.location = request.form['location']
        camera.ip_address = request.form['ip_address']
        camera.username = request.form['username']
        camera.password = request.form['password']
        db.session.commit()
        return redirect(url_for('camera.list_cameras'))
    return render_template('edit_camera.html', camera=camera)

@bp.route('/<int:camera_id>/delete', methods=['POST'])
def delete_camera(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    db.session.delete(camera)
    db.session.commit()
    return redirect(url_for('camera.list_cameras'))

@bp.route('/<int:camera_id>', methods=['PUT'])
def update_camera(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    data = request.json
    camera.name = data.get('name', camera.name)
    camera.ip_address = data.get('ip_address', camera.ip_address)
    camera.location = data.get('location', camera.location)
    camera.username = data.get('username', camera.username)
    camera.password = data.get('password', camera.password)
    db.session.commit()
    return jsonify({"message": "相机信息更新成功"})

@bp.route('/', methods=['GET'])
def get_cameras():
    cameras = Camera.query.all()
    return jsonify([{"id": c.id, "name": c.name, "ip_address": c.ip_address, "location": c.location, "status": c.status} for c in cameras])

@bp.route('/<int:camera_id>/config', methods=['GET', 'POST'])
def camera_config(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    if request.method == 'GET':
        # 获取相机配置
        # 这里应该从相机获取实际配置
        config = {
            "resolution": "1920x1080",
            "frame_rate": 30,
            "night_mode": False
        }
        return jsonify(config)
    elif request.method == 'POST':
        # 设置相机配置
        data = request.json
        # 这里应该将配置发送到实际的相机
        return jsonify({"message": "相机配置已更新"})

@bp.route('/<int:camera_id>/reboot', methods=['POST'])
def reboot_camera(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    # 这里应该发送重启命令到实际的相机
    return jsonify({"message": "相机重启命令已发送"})
