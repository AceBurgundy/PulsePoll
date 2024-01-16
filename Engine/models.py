from flask import current_app
from datetime import datetime
from typing import Dict
from Engine import db
import os

from Engine.emotion import *
RATING_TYPE = Dict[str, int]

class Candidate(db.Model):
    """
    Represents a candidate in the system.
    """
    __tablename__: str = 'candidate'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(3000), nullable=False)
    image = db.Column(db.String(100))

    comments = db.relationship('Comment', backref='candidate', lazy=True, cascade="all, delete-orphan")

    def delete(self) -> None:
        """
        Deletes the candidate and associated image if it exists.
        """
        if self.image:
            image_path: str = os.path.join(current_app.static_folder, 'candidate_pictures', self.image)
            if os.path.exists(image_path):
                os.remove(image_path)

        db.session.delete(self)
        db.session.commit()

    def get_rating(self) -> Dict[str, RATING_TYPE]:
        """
        Retrieves the number of NEGATIVE, POSITIVE, NEUTRAL counts
        """
        rating: Dict[str, int] = {
            NEGATIVE: 0,
            POSITIVE: 0,
            NEUTRAL: 0,
        }

        for comment in self.comments:
            rating[comment.emotion] += 1

        return rating

    def __repr__(self) -> str:
        """
        Returns a string representation of the Candidate object.

        Returns:
        --------
            the (str) Candidate object.
        """
        return f"Candidate('{self.name}')"

class Comment(db.Model):
    """
    Represents a comment on a candidate.
    """
    __tablename__: str = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_time_posted = db.Column(db.DateTime(), default=datetime.now)
    user_email = db.Column(db.String(120))
    username = db.Column(db.String(120))
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id', ondelete='CASCADE'), nullable=False)
    emotion = db.Column(db.String(8), nullable=False)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Comment object.

        Returns:
        --------
            the (str) Comment object.
        """
        return f"Comment('{self.text}', '{self.date_time_posted}')"
