from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Category, Account, Transaction, Budget, BudgetEntry

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/index2')
def index2():
    return render_template('index2.html')

# Read - Display all categories


@main.route('/categories')
def list_categories():
    categories = Category.query.all()
    return render_template('items.html', items=categories, type='Categories')

# Read - Display all accounts


@main.route("/accounts")
def list_acounts():
    accounts = Account.query.all()
    return render_template('items.html', items=accounts, type="Accounts")

# Read - Display all transactions


@main.route("/transactions")
def list_transactions():
    transactions = Transaction.query.all()
    return render_template('items.html', items=transactions, type="Transactions")

# Read - Display all Budgets


@main.route("/budgets")
def list_budgets():
    budgets = Budget.query.all()
    return render_template('items.html', items=budgets, type="Budgets")

# Read - Display all budgetentry


@main.route("/budgetentries")
def list_budgetentries():
    budgetentries = BudgetEntry.query.all()
    return render_template('items.html', items=budgetentries, type="Budgetentries")

# Create - Add a new category


@main.route('/category/add', methods=['GET', 'POST'])
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


@main.route('/category/edit/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        flash('Category updated successfully!', 'success')
        return redirect(url_for('list_categories'))
    return render_template('edit_category.html', category=category)

# Delete - Remove a category


@main.route('/category/delete/<int:id>', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully!', 'danger')
    return redirect(url_for('list_categories'))
