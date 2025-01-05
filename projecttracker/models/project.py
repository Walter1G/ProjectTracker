from datetime import datetime
from ..extensions import db, ma




class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(20), nullable=False, unique=True)
    budget = db.Column(db.Float, nullable=False)
    amount_paid = db.Column(db.Float, default=0)    
    start_date = db.Column(db.DateTime, default=None)
    completion_date = db.Column(db.DateTime, default=None)
    created_on = db.Column(db.DateTime, default=datetime.now)  
    last_update = db.Column(db.DateTime, onupdate=datetime.now)   
    description = db.Column(db.String(100), nullable=True)   
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship('User', back_populates='added_projects', lazy=True)
    
    budget_items = db.relationship('BudgetItem', back_populates='project', lazy=True)
    
    
    
    
    

    
    def __init__(self, title, budget, description=None):
        self.title = title
        self.budget = budget
        self.description = description        
        

    def __repr__(self):
        return f"<Project {self.title} with budget {self.budget} and expected due on {self.expected_due}>"


    def save(self):
        db.session.add(self)
        db.session.commit()
        
