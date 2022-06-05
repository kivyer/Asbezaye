from django.db import models


# Create your models here.
class Serial(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return str(self.code)


class UserOn(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    password=models.CharField(max_length=100,null=False,blank=False,default='Asbezaye')
    company = models.CharField(max_length=80)
    email = models.EmailField(max_length=60)
    serial = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    company = models.CharField(max_length=80)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Orders(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    amount = models.IntegerField()
    unit = models.CharField(max_length=5)
    for_when = models.DateTimeField('when to deliver')


class Product(models.Model):
    name = models.CharField(max_length=150)
    picture = models.ImageField(null=True, blank=True, upload_to='images/')


class Advertisement(models.Model):
    Title = models.CharField(max_length=40)
    description = models.CharField(max_length=1200)
    video = models.URLField(max_length=1200)


class OrderState(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    state = models.BooleanField()

    def __str__(self):
        return self.state


class FromComp(models.Model):
    post = models.CharField(max_length=350)
    links = models.URLField(max_length=1200)


class Setting(models.Model):
    name = models.CharField(max_length=40)
    state = models.BooleanField()


class CommentsP(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    url = models.URLField(null=True, blank=True)


class CommentsB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
