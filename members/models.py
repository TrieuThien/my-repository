from django.db import models

# Tạo ra class Member (Django gọi là model) nó tương tự như một bảng trong cơ sở dữ liệu 
class Member(models.Model):
    # Tạo ra hai trường dữ liệu kiểu Text, có độ dài tối đa là 255 kí tự
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null = True)
    joined_date = models.DateField(null = True)

    # Change the String Representation Function
    # def __str__(self):
    #     return f"{self.lastname} {self.firstname}"