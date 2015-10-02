from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class DatesModel(models.Model):
    """
    Abstract model for dates
    """
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        """
        Soft-deletes the records in the current QuerySet, i.e. marks it as inactive
        """
        self.update(active=False)


class SoftDeleteManager(models.Manager):
    """
    Object Manager to handle soft delete models.
    """
    use_for_related_fields = True

    def get_queryset(self):
        """
        Returns a new SoftDeleteQuerySet object.
        """
        return SoftDeleteQuerySet(self.model, using=self._db).filter(active=True)


class RemovableObjectModel(models.Model):
    """
    Abstract model to model tables having soft-deletable objects
    """
    active = models.BooleanField(default=True)

    objects = SoftDeleteManager()
    # Default manager, see: https://docs.djangoproject.com/en/1.5/topics/db/managers/#modifying-initial-manager-querysets
    all_objects = models.Manager()

    def delete(self, *args, **kwargs):
        self.active = False
        self.save()

    def undelete(self):
        self.active = True
        self.save()

    def permanent_delete(self, *args, **kwargs):
        super(RemovableObjectModel, self).delete(*args, **kwargs)

    class Meta:
        abstract = True
