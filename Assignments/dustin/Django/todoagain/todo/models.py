from django.db import models

class AddedItem(models.Model):
    bool_complete = models.BooleanField(default=False)
    new_value = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')

    def newItem(self, new_value):
        item_text = new_value
        return self.item_text
    
    def finishedItem(self, newItem):
        item_text = newItem
        pub_date = models.DateTimeField('date completed')
        return self.item_text

    def __str__(self):
        return self.new_value


# Create your models here.
