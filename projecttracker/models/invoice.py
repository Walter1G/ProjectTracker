from ..extensions import db, ma
from datetime import datetime



class Invoice(db.Model):
    __tablename__='invoices'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    invoiceNumber = db.Column(db.String(20), nullable=False)
    amount_due = db.Column(db.Float, nullable=False)
    amount_paid = db.Column(db.Float, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship('User', back_populates='added_invoices', lazy=True)
    budget_item_id = db.Column(db.Integer, db.ForeignKey('budget_items.id'), nullable=False)
    budget_item = db.relationship('BudgetItem', back_populates='invoices', lazy=True)
    payments = db.relationship('Payment', back_populates='invoice', lazy=True)
    
    
    
    
    
    def __repr__(self):
        return f"<Invoice {self.invoiceNumber} with amount due {self.amount_due} for budget item {self.budget_item.title}>"
    
