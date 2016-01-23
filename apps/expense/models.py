from django.db import models as db_models

from apps.account import models as account_models
from apps.activity import models as activity_models
from libs import models as libs_models


class ExpenseCategory(libs_models.DatesModel):
    """
    Stores static info of expense category
    """
    name = db_models.CharField(max_length=255, unique=True)
    description = db_models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Expense Categories'


class Expense(libs_models.DatesModel):
    """
    Stores info of expense
    """
    name = db_models.CharField(max_length=255)
    category = db_models.ForeignKey(ExpenseCategory)
    activity = db_models.ForeignKey(activity_models.Activity)

    def __unicode__(self):
        return u'{}({})'.format(self.name, self.activity.name)


class UserExpense(libs_models.DatesModel):
    """
    Stores info of expense of a user
    """
    user = db_models.ForeignKey(account_models.User)
    expense = db_models.ForeignKey(Expense)
    paid = db_models.DecimalField(max_digits=15, decimal_places=2)
    dues = db_models.DecimalField(max_digits=15, decimal_places=2)

    def __unicode__(self):
        return u'{}({})'.format(self.expense, self.dues)
