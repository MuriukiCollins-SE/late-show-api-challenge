from models import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    
    appearances = db.relationship('Appearance', backref='episode', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number
        }