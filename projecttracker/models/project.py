from datetime import datetime
from projecttracker.extensions import db, ma


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(20), nullable=False, unique=True)
    budget = db.Column(db.Float, nullable=False)
    amount_paid = db.Column(db.Float, default=0)
    start_date = db.Column(db.DateTime, nullable=False)
    expected_due = db.Column(db.DateTime, nullable=False)
    actual_due = db.Column(db.DateTime, default=None)
    created_on = db.Column(db.DateTime, default=datetime.now)  
    last_update = db.Column(db.DateTime, onupdate=datetime.now)  

    # One-to-many relationship
    # budget_items = db.relationship(
    #     'BudgetItem',
    #     back_populates='project',
    #     cascade='all, delete-orphan'
    # )

    def __init__(self, title, budget, start_date, expected_due):
        self.title = title
        self.budget = budget
        self.start_date = start_date
        self.expected_due = expected_due

    def __repr__(self):
        return f"<Project {self.title} with budget {self.budget} and expected due on {self.expected_due}>"


    def save(self):
        db.session.add(self)
        db.session.commit()