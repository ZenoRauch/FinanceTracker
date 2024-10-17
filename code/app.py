from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration (assuming MariaDB with root user and no password)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/financetracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Used for session management, flash messages, etc.

# Initialize the SQLAlchemy connection
db = SQLAlchemy(app)


# Model for the 'category' table
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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

# Read - Display all categories
@app.route('/categories')
def list_categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

# Create - Add a new category
@app.route('/category/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        flash('Category added successfully!', 'success')
        return redirect(url_for('list_categories'))
    return render_template('add_category.html')

# Update - Edit an existing category
@app.route('/category/edit/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        flash('Category updated successfully!', 'success')
        return redirect(url_for('list_categories'))
    return render_template('edit_category.html', category=category)

# Delete - Remove a category
@app.route('/category/delete/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully!', 'danger')
    return redirect(url_for('list_categories'))

if __name__ == '__main__':
    app.run(debug=True)