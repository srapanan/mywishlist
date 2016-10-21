from django.db import models
from django.core.exceptions import ObjectDoesNotExist

import bcrypt, re

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def register(self, data):
        errors = []
        if not NAME_REGEX.match(data['name']) or len(data['name']) < 3:
            errors.append("Name must have atleast 3 characters")
        if not NAME_REGEX.match(data['user_name']) or len(data['user_name']) < 3:
            errors.append("Username has to have a minimum length of 2 characters and cannot be empty")
        if len(data['password']) < 8:
            errors.append("You must enter more than 8 characters")
        if not data['password'] == data['password_confirm']:
            errors.append("Password don't match")
        same = User.objects.filter(user_name=data['user_name'])
        if same:
            errors.append("Username already in use")
        if len(errors) == 0:
            password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(name = data['name'], user_name = data['user_name'], password = password, date = data['date'])
            print ("*******************user added******************")
            return (True, user)
        else:
            return (False, errors)

    def login(self, data):
        errors = []
        try:
            user = User.objects.get(user_name = data['user_name'])
            password = data['password'].encode()
            if bcrypt.checkpw(password, user.password.encode()):
                return(True, user)
        except ObjectDoesNotExist:
            errors.append("Wrong password")
            pass
        return(False, errors)

class ItemManager(models.Manager):
    def items(self, data):
        errors = []
        if len(data['item']) < 3:
            errors.append("item name too short")
        if len(data['item']) > 3:
            item = Item.objects.create(item=data['item'], user_name=data['user_name'])
            print ("****************item added****************")
            return (True, item)

class User(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=250)
    date = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Item(models.Model):
    item = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
