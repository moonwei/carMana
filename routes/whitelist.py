from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from extensions import db
from models import Whitelist, Camera
from datetime import datetime

bp = Blueprint('whitelist', __name__, url_prefix='/whitelist')

@bp.route('/', methods=['GET'])
def list_whitelist():
    whitelists = Whitelist.query.all()
    return render_template('whitelist.html', whitelist=whitelists)

@bp.route('/add', methods=['GET', 'POST'])
def add_whitelist():
    if request.method == 'POST':
        new_whitelist = Whitelist(
            plate_number=request.form['plate_number'],
            start_time=request.form['start_time'],
            end_time=request.form['end_time']
        )
        db.session.add(new_whitelist)
        db.session.commit()
        return redirect(url_for('whitelist.list_whitelist'))
    return render_template('add_whitelist.html')

@bp.route('/<int:whitelist_id>/edit', methods=['GET', 'POST'])
def edit_whitelist(whitelist_id):
    whitelist = Whitelist.query.get_or_404(whitelist_id)
    if request.method == 'POST':
        whitelist.plate_number = request.form['plate_number']
        whitelist.start_time = request.form['start_time']
        whitelist.end_time = request.form['end_time']
        db.session.commit()
        return redirect(url_for('whitelist.list_whitelist'))
    return render_template('edit_whitelist.html', whitelist=whitelist)

@bp.route('/<int:whitelist_id>/delete', methods=['POST'])
def delete_whitelist(whitelist_id):
    whitelist = Whitelist.query.get_or_404(whitelist_id)
    db.session.delete(whitelist)
    db.session.commit()
    return redirect(url_for('whitelist.list_whitelist'))

@bp.route('/whitelist', methods=['GET'])
def get_whitelist():
    sn = request.args.get('sn')
    camera = Camera.query.filter_by(serial_number=sn).first()
    if not camera:
        return jsonify({"code": 1, "msg": "Camera not found"}), 404

    whitelists = Whitelist.query.all()
    whitelist_data = [{
        "plateNumber": w.plate_number,
        "startTime": w.start_time.strftime('%Y-%m-%d %H:%M:%S') if w.start_time else None,
        "endTime": w.end_time.strftime('%Y-%m-%d %H:%M:%S') if w.end_time else None
    } for w in whitelists]

    return jsonify({
        "code": 0,
        "msg": "success",
        "data": whitelist_data
    })
