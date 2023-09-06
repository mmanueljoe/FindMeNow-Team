from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define any relationships with other tables (e.g., lost_items or found_items)

class LostItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_lost = db.Column(db.DateTime, nullable=False)
    photo_url = db.Column(db.String(255))  # You can store image URLs here
    status = db.Column(db.String(20), default='Lost')
    found_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    found_at = db.Column(db.DateTime)

    # Define relationships with other tables


class FoundItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lost_item_id = db.Column(db.Integer, db.ForeignKey('lost_item.id'))
    date_found = db.Column(db.DateTime, nullable=False)
    photo_url = db.Column(db.String(255))  # You can store image URLs here
    status = db.Column(db.String(20), default='Not Returned')

    # Define relationships with other tables
