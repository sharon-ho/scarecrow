# -*- encoding: utf-8 -*-
"""
Argon Dashboard - coded in Flask

Author  : AppSeed App Generator
Design  : Creative-Tim.com
License : MIT 
Support : https://appseed.us/support 
"""

from app         import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))

    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        return '<User %r - %s>' % (self.id) % (self.email)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 

class Stats(db.Model):

    id    = db.Column(db.Integer,     primary_key=True)
    key   = db.Column(db.String(64),  unique=True)
    val   = db.Column(db.Integer)
    val_s = db.Column(db.String(256))

    def __init__(self, key):
        self.key   = key

        db_obj = Stats.query.filter_by(key=key).first()
        if db_obj:
            self.id    = db_obj.id
            self.key   = db_obj.key
            self.val   = db_obj.val
            self.val_s = db_obj.val_s

        else:

            db.session.add ( self )

            self.val   = 0
            self.val_s = ''

    def __repr__(self):
        return '<Stats %s / %r / %s >' % ( self.key, self.val, self.val_s )

    def save(self):

        db_obj = Stats.query.filter_by(key=self.key).first()

        # update the existing db object
        if db_obj:

            db_obj.val   = self.val
            db_obj.val_s = self.val_s

        # commit change and save the object
        db.session.commit( )

        return self
