from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField()
    kurs = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism

class Reja(models.Model):
    sarlavha = models.CharField(max_length=255)
    batafsil = models.TextField(blank=True, null=True)
    sana = models.DateField()
    bajarildi = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
