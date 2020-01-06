from django.db import models, connection


class MixinOverview(models.Model):

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} CASCADE'.format(cls._meta.db_table))

    class Meta:
        abstract = True
        managed = True
