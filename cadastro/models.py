from django.db import models


class Cadastro(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.firstname) + ' ' + str(self.lastname)
