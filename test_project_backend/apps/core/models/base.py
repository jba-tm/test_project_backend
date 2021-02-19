from django.conf import settings
from django.db import models


class CreationModificationDateBase(models.Model):
    """
    Abstract base class with a creation and modification date and time
    """

    created_at = models.DateTimeField(
        'created_at',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        'updated_at',
        auto_now=True,
    )

    class Meta:
        ordering = ['created_at']
        abstract = True

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     print("save() from CreationModificationDateBase called")
    #
    # save.alters_data = True
    #
    # def delete(self, *args, **kwargs):
    #     super().delete(*args, **kwargs)
    #     print("delete() from CreationModificationDateBase called")
    #
    # def test(self):
    #     print("test() from CreationModificationDateBase called")

