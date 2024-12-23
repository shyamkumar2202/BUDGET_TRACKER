from django import forms
from .models import Income, Expense, Category

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'description']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
