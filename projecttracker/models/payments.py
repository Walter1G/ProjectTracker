from ..extensions import db, ma
from datetime import datetime




class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_paid = db.Column(db.DateTime, default=datetime.now)
    transaction_id = db.Column(db.String(20), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship('User', back_populates='added_payments', lazy=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    invoice = db.relationship('Invoice', back_populates='payments', lazy=True)
  
    
    def __repr__(self):
        return f"<Payment of {self.amount} made on {self.date_paid} for invoice {self.invoice.invoiceNumber}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
