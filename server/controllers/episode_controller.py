from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import db
from models.episode import Episode
from models.appearance import Appearance

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    episode_data = episode.to_dict()
    episode_data['appearances'] = [appearance.to_dict() for appearance in appearances]
    return jsonify(episode_data), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'}), 200