from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Higher(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Type must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Lower(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    mass = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()
    higher = models.ForeignKey('higher', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
