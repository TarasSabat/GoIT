from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from pymongo import MongoClient

@receiver(post_save, sender=CustomUser)
def create_user_database(sender, instance, created, **kwargs):
    if created and CustomUser.objects.count() == 1:
        # Підключення до MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        # Створення бази даних 'users'
        db = client['users']
    else:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['users']

    # Додавання інформації про користувача до бази даних
    db.users.insert_one({
        'full_name': instance.userprofile.full_name,
        'password': instance.password
    })