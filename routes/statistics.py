from flask import Blueprint, jsonify, send_file
from models import Recognition, Camera
from sqlalchemy import func
import csv
from io import StringIO

bp = Blueprint('statistics', __name__, url_prefix='/statistics')

@bp.route('/daily', methods=['GET'])
def daily_statistics():
    daily_stats = db.session.query(
        func.date(Recognition.timestamp).label('date'),
        func.count(Recognition.id).label('count')
    ).group_by(func.date(Recognition.timestamp)).all()
    
    return jsonify([{"date": str(stat.date), "count": stat.count} for stat in daily_stats])

@bp.route('/camera', methods=['GET'])
def camera_statistics():
    camera_stats = db.session.query(
        Camera.name,
        func.count(Recognition.id).label('count')
    ).join(Recognition).group_by(Camera.id).all()
    
    return jsonify([{"camera": stat.name, "count": stat.count} for stat in camera_stats])

@bp.route('/export', methods=['GET'])
def export_data():
    recognitions = Recognition.query.all()
    
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['ID', 'Camera ID', 'Plate Number', 'Timestamp', 'Image Path'])
    for r in recognitions:
        cw.writerow([r.id, r.camera_id, r.plate_number, r.timestamp, r.image_path])
    
    output = si.getvalue()
    si.close()
    
    return send_file(
        StringIO(output),
        mimetype='text/csv',
        as_attachment=True,
        attachment_filename='recognition_data.csv'
    )
