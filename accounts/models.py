from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import timedelta
from django.conf import settings
import random


def get_rand_theme():
    return random.randint(1, 4)


def get_rand_bio():
    return random.choice([
        "Поел пельмени в Китае",
        "Мой кот пианист-виртуоз",
        "Коллекционирую пустые кофеины",
        "Хотел стать котом, стал человеком :(",
        "Живу в мире, где все зеленое",
        "Победил на чемпионате по смеху",
        "Освоил язык жирафов на высоте",
        "Мой дом - космический корабль",
        "Выиграл гонку с тенью",
        "Люблю медитировать в магазинах",
        "Путешествую по зонам комфорта",
    ] + (["Клоун"] if settings.DEBUG else []))


def get_rand_country():
    return random.choice([
        "Вестерос",
        "Нарния",
        "Татуин",
        "Мидгард",
        "Оз",
        "Пандора",
        "Эндор",
        "Мордор",
        "Криптон",
        "Ривия",
        "Альтернативная Земля-616",
        "Темный Лес",
    ])


def get_rand_city():
    return random.choice([
        "Готэм",
        "Ривендэл",
        "Корускант",
        "Метрополис",
        "Вайтран",
        "Мидгар",
        "Ракапоши",
        "Атлантида",
        "Ракуль",
        "Зибилин",
        "Новый Рим",
        "Новый Ковентри",
    ])



def get_rand_code():
    res = ""

    for i in range(6):
        res += random.choice("QWERTYUIPASDFGHJKLZXCVBNM123456789")

    while res in [st.code for st in Student.objects.iterator()]:
        for i in range(6):
            res += random.choice("QWERTYUIPASDFGHJKLZXCVBNM123456789")

    return res


class Student(models.Model):
    user = models.OneToOneField(
        User, verbose_name="Пользователь", on_delete=models.CASCADE)
    lifes = models.IntegerField(verbose_name="Жизни", default=5)
    recoverytime = models.DurationField(
        verbose_name="Время до восстановления жизни", default=timedelta(minutes=10))
    crystals = models.IntegerField(verbose_name="Кристалы", default=100)
    admin = models.BooleanField(verbose_name="Права админа", default=False)
    friends = models.ManyToManyField(
        "Student", verbose_name="Друзья", blank=True)
    avatar = models.FileField(verbose_name="Аватар",
                              upload_to="avatars", blank=True)
    theme = models.IntegerField(verbose_name="Тема", validators=[
                                MinValueValidator(1), MaxValueValidator(4)], default=get_rand_theme)
    bio = models.TextField(verbose_name="Биография", default=get_rand_bio)
    country = models.CharField(
        verbose_name="Страна", max_length=30, default=get_rand_country)
    city = models.CharField(verbose_name="Город",
                            max_length=30, default=get_rand_city)
    code = models.CharField(
        verbose_name="Код", max_length=6, default=get_rand_code, unique=True)
 
    def __str__(self):
        return "Студент " + self.user.username

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class FriendRequest(models.Model):
    fromuser = models.ForeignKey(Student, verbose_name="От кого",
                                 related_name="friendrequests_to", on_delete=models.CASCADE)
    touser = models.ForeignKey(Student, verbose_name="Кому",
                               related_name="friendrequests_from", on_delete=models.CASCADE)

    def __str__(self):
        return "Запрос от " + self.fromuser.user.username + " к " + self.touser.user.username

    class Meta:
        verbose_name = "Запрос на дружбу"
        verbose_name_plural = "Запросы на дружбу"


class FriendNotification(models.Model):
    type = models.CharField(verbose_name="Тип", max_length=50)
    fromuser = models.ForeignKey(Student, verbose_name="От кого",
                                 related_name="friendnotification_to", on_delete=models.CASCADE)
    touser = models.ForeignKey(Student, verbose_name="Кому",
                               related_name="friendnotification_from", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
