from ..extensions import ma


class UserSchema(ma.Schema):
    projects = ma.Nested('ProjectSchema', many=True, only=('id', 'title', 'budget', 'amount_paid', 'description'))
    budget_items = ma.Nested('BudgetItemSchema', many=True, only=('id', 'title', 'budget_amount', 'description'))
    invoices = ma.Nested('InvoiceSchema', many=True, only=('id', 'invoiceNumber', 'amount_due', 'amount_paid'))
    payments = ma.Nested('PaymentSchema', many=True, only=('id', 'amount', 'date_paid', 'transaction_id'))

    class Meta:
        fields = ('id', 'email', 'created_on', 'last_update', 'phone_number', 
                  'first_name', 'last_name', 'projects', 'budget_items', 'invoices', 'payments')


class ProjectSchema(ma.Schema):
    budget_items = ma.Nested('BudgetItemSchema', many=True, only=('id', 'title', 'budget_amount', 'date_created', 'description'))
    creator = ma.Nested('UserSchema', only=('id', 'email', 'first_name', 'last_name'))

    class Meta:
        fields = ('id', 'title', 'budget', 'amount_paid', 'start_date', 'expected_due', 
                  'actual_due', 'created_on', 'last_update', 'description', 'creator', 'budget_items')


class BudgetItemSchema(ma.Schema):
    project = ma.Nested('ProjectSchema', only=('id', 'title', 'budget', 'amount_paid'))
    creator = ma.Nested('UserSchema', only=('id', 'email', 'first_name', 'last_name'))

    class Meta:
        fields = ('id', 'title', 'budget_amount', 'actual_amount', 'date_created', 
                  'description', 'project_id', 'creator_id', 'project', 'creator')


class InvoiceSchema(ma.Schema):
    creator = ma.Nested('UserSchema', only=('id', 'email', 'first_name', 'last_name'))
    budget_item = ma.Nested('BudgetItemSchema', only=('id', 'title', 'budget_amount', 'description'))
    payments = ma.Nested('PaymentSchema', many=True, only=('id', 'amount', 'date_paid', 'transaction_id'))

    class Meta:
        fields = ('id', 'invoiceNumber', 'amount_due', 'amount_paid', 'date_created', 
                  'creator', 'budget_item', 'payments')


class PaymentSchema(ma.Schema):
    creator = ma.Nested('UserSchema', only=('id', 'email', 'first_name', 'last_name'))
    invoice = ma.Nested('InvoiceSchema', only=('id', 'invoiceNumber', 'amount_due', 'amount_paid'))

    class Meta:
        fields = ('id', 'amount', 'date_paid', 'transaction_id', 'creator', 'invoice')


# Instantiate schemas globally
user_schema = UserSchema()
users_schema = UserSchema(many=True)
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
budget_item_schema = BudgetItemSchema()
budget_items_schema = BudgetItemSchema(many=True)
invoice_schema = InvoiceSchema()
invoices_schema = InvoiceSchema(many=True)
payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)
