from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'category'
    categoryid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

# Model for the 'account' table


class Account(db.Model):
    __tablename__ = 'account'
    accountid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bank = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)

# Model for the 'transaction' table


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

# Model for the 'budget' table


class Budget(db.Model):
    __tablename__ = 'budget'
    budgetid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    startdate = db.Column(db.Date, nullable=False)
    enddate = db.Column(db.Date, nullable=False)

# Model for the 'budgetentry' table


class BudgetEntry(db.Model):
    __tablename__ = 'budgetentry'
    budgetentryid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    categoryid = db.Column(db.Integer, db.ForeignKey('category.categoryid'))
    budgetid = db.Column(db.Integer, db.ForeignKey('budget.budgetid'))
