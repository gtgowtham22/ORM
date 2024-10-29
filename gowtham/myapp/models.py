from django.db import models
from django.contrib import admin
class Loan(models.Model):
	Name=models.CharField(max_length=10)
	Income=models.IntegerField(primary_key="Income")
	Interest=models.FloatField()
	Duedate=models.DateField()
	Email=models.EmailField()
class LoanAdmin(admin.ModelAdmin):
	list_display=('Name','Income','Interest','Duedate','Email')
