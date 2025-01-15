from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Shift(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="shifts")
    date = models.DateField()
    shift_time = models.CharField(max_length=50,
        choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('night', 'Night')])
    def __str__(self):
        return f"{self.employee.name} - {self.date} ({self.shift_time})"
