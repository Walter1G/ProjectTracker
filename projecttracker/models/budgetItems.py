from ..extensions import db, ma
from datetime import datetime




class BudgetItem(db.Model):
    __tablename__='budget_items'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(20), nullable=False)
    budget_amount=db.Column(db.Float, nullable=False)
    actual_amount=db.Column(db.Float, default=0)
    date_created=db.Column(db.DateTime, default=datetime.now)
    description=db.Column(db.String(100), nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    project = db.relationship('Project', back_populates='budget_items', lazy=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship('User', back_populates='added_budget_Items', lazy=True)
    
    invoices = db.relationship('Invoice', back_populates='budget_item', lazy=True)
    
    
    
    
    
    def __repr__(self):
        return f"<BudgetItem {self.title} with budget {self.budget_amount} for project {self.project.title}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    

