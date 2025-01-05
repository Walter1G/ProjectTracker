from ..extensions import db, ma
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.now)
    last_update = db.Column(db.DateTime, onupdate=datetime.now)
    phone_number = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    
    added_projects = db.relationship('Project', back_populates='creator', lazy=True)
    added_budget_Items = db.relationship('BudgetItem', back_populates='creator', lazy=True)
    added_invoices = db.relationship('Invoice', back_populates='creator', lazy=True)
    added_payments = db.relationship('Payment', back_populates='creator', lazy=True)
    
    
    
    #relations
    
    
    
    
    def __init__(self, email, password, phone_number, first_name, last_name):
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        
    def __repr__(self):
        return f"<User {self.email} with phone number {self.phone_number}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
