from django.db import models

# Create your models here.
class at(models.Model):
    
    Name =models.CharField(max_length=200)
    AllCategoriesAppearedBoys=models.IntegerField()
    AllCategoriesAppearedGirls=models.IntegerField()
    AllCategoriesTotal=models.IntegerField()
    AllCategoriesPassedBoys=models.IntegerField()
    AllCategoriesPassedGirls=models.IntegerField()
    AllCategoriesPassedTotal=models.IntegerField()
    ScheduledCasteStudentsAppearedBoys=models.IntegerField()
    ScheduledCasteStudentsAppearedGirls=models.IntegerField()
    ScheduledCasteStudentsAppearedTotal=models.IntegerField()
    ScheduledCasteStudentsPassedBoys=models.IntegerField()
    ScheduledCasteStudentsPassedGirls=models.IntegerField()
    ScheduledCasteStudentsPassedTotal=models.IntegerField()
    ScheduledTribeStudentsAppearedBoys=models.IntegerField()
    ScheduledTribeStudentsAppearedGirls=models.IntegerField()
    ScheduledTribeStudentsAppearedTotal=models.IntegerField()
    ScheduledTribeStudentsPassedBoys=models.IntegerField()
    ScheduledTribeStudentsPassedGirls=models.IntegerField()
    ScheduledTribeStudentsPassedTotal=models.IntegerField()
