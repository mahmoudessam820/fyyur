from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from datetime import datetime

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# Establish connections with database
db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String()))
    image_link = db.Column(db.String())
    facebooK_link = db.Column(db.String())
    seeking_talent = db.Column(db.Boolean())
    website_link = db.Column(db.String())
    seeking_description = db.Column(db.String(500))

    show_venue = db.relationship('Show', backref='venue', lazy=True)

    def __repr(self):
        return f'<Venue {self.id} name: {self.name}>'


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String()))
    image_link = db.Column(db.String())
    facebook_link = db.Column(db.String())
    seeking_talent = db.Column(db.Boolean())
    website_link = db.Column(db.String())
    seeking_description = db.Column(db.String(500))

    show_artist = db.relationship('Show', backref='artist', lazy=True)

    def __repr(self):
        return f'<Artist {self.id} name: {self.name}>'


class Show(db.Model):
    __tablename__ = 'Show' 

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Show {self.id}, Artist {self.artist_id}, Venue {self.venue_id}>'