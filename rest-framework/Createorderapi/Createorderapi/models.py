from django.db import models

class Shop_transaction(models.Model):
   
    id = models.IntegerField(db_column='id',primary_key=True)
    user_id = models.CharField(db_column='user_id',max_length=100)
    orderdate = models.CharField(db_column='transaction_type',max_length=100)
    user_email = models.CharField(db_column='user_email',max_length=100)
    pos_name = models.CharField(db_column='pos_name',max_length=100)


    class Meta:
        db_table = 'orders'
