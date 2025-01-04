from ..extensions import db, ma
from datetime import datetime

class BudgetItem(db.Model):
    __tablename__='budget_items'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(20), nullable=False)
    budget_amount=db.Column(db.Float, nullable=False)
    actual_amount=db.Column(db.Float, default=0)
    date_created=db.Column(db.DateTime, default=datetime.now)
    
    
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    project = db.relationship('Project', back_populates='budget_items')
    
    # Foreign key
    # invoce_id=db.Column(db.Integer, db.ForeignKey('invoices.id'))
    # project_id=db.Column(db.Integer, db.ForeignKey('projects.id'))
    
    
    def __repr__(self):
        return f"<BudgetItem {self.title} with budget {self.budget_amount} for project {self.project.title}>"