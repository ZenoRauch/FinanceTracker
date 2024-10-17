from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/financetracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for 'category' table
class Category(db.Model):
    __tablename__ = 'category'
    categoryid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    # Relationship with 'Transaction' and 'BudgetEntry'
    transactions = db.relationship('Transaction', backref='category', lazy=True)
    budget_entries = db.relationship('BudgetEntry', backref='category', lazy=True)

# Model for 'account' table
class Account(db.Model):
    __tablename__ = 'account'
    accountid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bank = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    # Relationship with 'Transaction'
    transactions = db.relationship('Transaction', backref='account', lazy=True)

# Model for 'transaction' table
class Transaction(db.Model):
    __tablename__ = 'transaction'
    transactionid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.String(255))
    accountid = db.Column(db.Integer, db.ForeignKey('account.accountid'))
    categoryid = db.Column(db.Integer, db.ForeignKey('category.categoryid'))
    paymentforperiod = db.Column(db.Date)
    isprepayment = db.Column(db.Boolean)

# Model for 'budget' table
class Budget(db.Model):
    __tablename__ = 'budget'
    budgetid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    startdate = db.Column(db.Date, nullable=False)
    enddate = db.Column(db.Date, nullable=False)

    # Relationship with 'BudgetEntry'
    budget_entries = db.relationship('BudgetEntry', backref='budget', lazy=True)

# Model for 'budgetentry' table
class BudgetEntry(db.Model):
    __tablename__ = 'budgetentry'
    budgetentryid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    categoryid = db.Column(db.Integer, db.ForeignKey('category.categoryid'))
    budgetid = db.Column(db.Integer, db.ForeignKey('budget.budgetid'))

# To create the tables in the database
if __name__ == '__main__':
    db.create_all()
