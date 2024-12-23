from django.shortcuts import render, redirect
from .models import Income, Expense, Category
from .forms import IncomeForm, ExpenseForm, CategoryForm
from django.db.models import Sum

def dashboard(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expenses

    return render(request, 'tracker/dashboard.html', {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
    })

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'tracker/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})

def manage_categories(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')
    else:
        form = CategoryForm()
    return render(request, 'tracker/manage_categories.html', {
        'categories': categories,
        'form': form
    })
