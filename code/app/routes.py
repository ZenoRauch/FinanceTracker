from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Category, Account, Transaction, Budget, BudgetEntry

main = Blueprint('main', __name__)

# ###############
# Index Routing
# ###############

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/index2')
def index2():
    return render_template('index2.html')

# ###############
# Read Routing
# ###############

# Read - Display all categories


@main.route('/categories')
def list_categories():
    categories = Category.query.all()
    return render_template('items.html', items=categories, type='Categories')

# Read - Display all accounts


@main.route("/accounts")
def list_accounts():
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

# ###############
# Create Routing
# ###############

# Create - Add a new category


@main.route('/category/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        flash('Category added successfully!', 'success')
        return redirect(url_for('main.list_categories'))
    return render_template('add_category.html')

# Create - Add a new account


@main.route('/account/add', methods=['GET', 'POST'])
def add_account():
    if request.method == 'POST':
        name = request.form['name']
        bank = request.form['bank']
        new_account = Account(name=name,bank=bank)
        db.session.add(new_account)
        db.session.commit()
        flash('Account added successfully!', 'success')
        return redirect(url_for('main.list_accounts'))
    return render_template('add_account.html')

# Create - Add a new transaction


@main.route('/transaction/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        date = request.form['date']
        amount = request.form['amount']
        description = request.form['description']
        account_id = request.form['account_id']
        category_id = request.form['category_id']
        paymentforperiod = request.form['paymentforperiod']
        isprepayment = 'isprepayment' in request.form
        
        new_transaction = Transaction(
            date=date, 
            amount=amount, 
            description=description, 
            accountid=account_id, 
            categoryid=category_id, 
            paymentforperiod=paymentforperiod, 
            isprepayment=isprepayment
        )
        
        db.session.add(new_transaction)
        db.session.commit()
        
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('main.list_transactions'))
    
    accounts = Account.query.all()
    categories = Category.query.all()
    return render_template('add_transaction.html', accounts=accounts, categories=categories)

# Create -  Add a new budget


@main.route('/budget/add', methods=['GET', 'POST'])
def add_budget():
    if request.method == 'POST':
        startdate = request.form['startdate']
        enddate = request.form['enddate']
        
        new_budget = Budget(startdate=startdate, enddate=enddate)
        db.session.add(new_budget)
        db.session.commit()
        
        flash('Budget added successfully!', 'success')
        return redirect(url_for('main.list_budgets'))
    
    return render_template('add_budget.html')

# Create - Add a new budgetentry


@main.route('/budgetentry/add', methods=['GET', 'POST'])
def add_budgetentry():
    if request.method == 'POST':
        amount = request.form['amount']
        category_id = request.form['category_id']
        budget_id = request.form['budget_id']
        
        new_budgetentry = BudgetEntry(amount=amount, categoryid=category_id, budgetid=budget_id)
        db.session.add(new_budgetentry)
        db.session.commit()
        
        flash('Budget Entry added successfully!', 'success')
        return redirect(url_for('main.list_budgetentries'))
    
    categories = Category.query.all()
    budgets = Budget.query.all()
    return render_template('add_budgetentry.html', categories=categories, budgets=budgets)

# ###############
# Update Routing
# ###############

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

# Update - Edit an existing account


@main.route('/account/edit/<int:id>', methods=['GET', 'POST'])
def edit_account(id):
    account = Account.query.get_or_404(id)
    
    if request.method == 'POST':
        account.bank = request.form['bank']
        account.name = request.form['name']
        
        db.session.commit()
        flash('Account updated successfully!', 'success')
        return redirect(url_for('main.list_accounts'))
    
    return render_template('edit_account.html', account=account)


# Update - Edit an existing transaction


@main.route('/transaction/edit/<int:id>', methods=['GET', 'POST'])
def edit_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    
    if request.method == 'POST':
        transaction.date = request.form['date']
        transaction.amount = request.form['amount']
        transaction.description = request.form['description']
        transaction.accountid = request.form['account_id']
        transaction.categoryid = request.form['category_id']
        transaction.paymentforperiod = request.form['paymentforperiod']
        transaction.isprepayment = 'isprepayment' in request.form
        
        db.session.commit()
        flash('Transaction updated successfully!', 'success')
        return redirect(url_for('main.list_transactions'))
    
    accounts = Account.query.all()
    categories = Category.query.all()
    return render_template('edit_transaction.html', transaction=transaction, accounts=accounts, categories=categories)


# Update - Edit an existing budget


@main.route('/budget/edit/<int:id>', methods=['GET', 'POST'])
def edit_budget(id):
    budget = Budget.query.get_or_404(id)
    
    if request.method == 'POST':
        budget.startdate = request.form['startdate']
        budget.enddate = request.form['enddate']
        
        db.session.commit()
        flash('Budget updated successfully!', 'success')
        return redirect(url_for('main.list_budgets'))
    
    return render_template('edit_budget.html', budget=budget)



# Update - Edit an existing budgetentry


@main.route('/budgetentry/edit/<int:id>', methods=['GET', 'POST'])
def edit_budgetentry(id):
    budgetentry = BudgetEntry.query.get_or_404(id)
    
    if request.method == 'POST':
        budgetentry.amount = request.form['amount']
        budgetentry.categoryid = request.form['category_id']
        budgetentry.budgetid = request.form['budget_id']
        
        db.session.commit()
        flash('Budget Entry updated successfully!', 'success')
        return redirect(url_for('main.list_budgetentries'))
    
    categories = Category.query.all()
    budgets = Budget.query.all()
    return render_template('edit_budgetentry.html', budgetentry=budgetentry, categories=categories, budgets=budgets)
