from django.db import models as db_models

from apps.account import models as account_models
from libs import models as libs_models


class ActivityCategory(libs_models.DatesModel):
    """
    Stores static info of activity category
    """
    name = db_models.CharField(max_length=255, unique=True)
    description = db_models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Activity Categories'


class Activity(libs_models.DatesModel):
    """
    Stores info of activity
    """
    name = db_models.CharField(max_length=255)
    category = db_models.ForeignKey(ActivityCategory)
    ended_at = db_models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return u'{}({})'.format(self.name, self.category)

    class Meta:
        verbose_name_plural = u'Activities'


class UserActivity(libs_models.DatesModel):
    """
    Stores info of activity of a user
    """
    user = db_models.ForeignKey(account_models.User)
    activity = db_models.ForeignKey(Activity)
    order = db_models.PositiveSmallIntegerField()

    def __unicode__(self):
        return u'{}({})'.format(self.user, self.activity)

    class Meta:
        verbose_name_plural = u'User Activities'
        unique_together = (u'user', u'activity', )
        get_latest_by = u'order'
