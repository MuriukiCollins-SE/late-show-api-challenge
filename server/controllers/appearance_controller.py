from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db
from models.appearance import Appearance
from models.guest import Guest
from models.episode import Episode

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    
    if not all([rating, guest_id, episode_id]):
        return jsonify({'error': 'All fields required'}), 400
    
    try:
        Appearance.validate_rating(rating)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    if not Guest.query.get(guest_id):
        return jsonify({'error': 'Guest not found'}), 404
    
    if not Episode.query.get(episode_id):
        return jsonify({'error': 'Episode not found'}), 404
    
    appearance = Appearance(
        rating=rating,
        guest_id=guest_id,
        episode_id=episode_id
    )
    db.session.add(appearance)
    db.session.commit()
    return jsonify({'message': 'Appearance created successfully', 'appearance': appearance.to_dict()}), 201