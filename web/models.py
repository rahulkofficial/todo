from django.db import models


class Tasks(models.Model):
    title=models.CharField(max_length=225)
    date_time=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)
    student=models.ForeignKey('web.Students',on_delete=models.CASCADE)

    class Meta:
        db_table="web_tasks"
        verbose_name_plural="tasks"
    
    def __str__(self):
        return str(self.id)
    

class Students(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    st_class=models.IntegerField()
    division=models.CharField(max_length=1)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    password=models.CharField()

    class Meta:
        db_table="web_students"
        verbose_name_plural="students"
    
    def __str__(self):
        return str(self.id)


