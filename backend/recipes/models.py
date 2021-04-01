from django.db import models

class Recipe(models.Model):
    name = models.CharField("Name", max_length=240)
    description = models.TextField("Description")

    def __str__(self) -> str:
        return self.name

class Ingredients(models.Model):
    name = models.CharField("Name", max_length=240)
    qty = models.FloatField("Quantity", default=0.0)
    unit = models.CharField("Unit", max_length=20)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name 

    class Meta:
        ordering = ['name']


class Procedure(models.Model):
    order = models.IntegerField("Order")
    process = models.TextField("Process")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.order + ": " + self.process
    
    class Meta:
        ordering = ['order']
