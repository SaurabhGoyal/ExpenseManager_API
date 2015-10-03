from django.contrib import admin

from apps.expense.models import ExpenseCategory, Expense, UserExpense

admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(UserExpense)
