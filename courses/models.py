from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django_jsonform.models.fields import ArrayField
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import Student


class CourseType(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип курса"
        verbose_name_plural = "Типы курсов"


class Course(models.Model):
    coursetype = models.ForeignKey(CourseType, verbose_name="Тип курса", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название")

    def __str__(self):
        return f"{self.coursetype.name}: {self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Level(models.Model):
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE)

    def order(self):
        return [*self.course.level_set.order_by("id")].index(self) + 1

    def __str__(self):
        return f"{self.course.coursetype.name}: {self.course.name} - {self.order()} уровень"

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"


class Question(models.Model):
    level = models.ForeignKey(Level, verbose_name="Уровень", on_delete=models.CASCADE)
    text = models.CharField(verbose_name="Текст вопроса", max_length=1000)
    choise = ArrayField(models.CharField(), verbose_name="Выбор", size=4)
    correct = models.IntegerField(verbose_name="Номер правильного выбора", validators=[MinValueValidator(1), MaxValueValidator(4)])

    def answered(self, user: User | Student):
        try:
            if isinstance(user, User):
                answer = self.answer_set.get(student=user.student)

            if isinstance(user, Student):
                answer = self.answer_set.get(student=user)

            return "correct" if answer.correct else "wrong"
        except ObjectDoesNotExist:
            return "notanswered"

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    student = models.ForeignKey(Student, verbose_name="Пользователь", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name="Вопрос", on_delete=models.CASCADE)
    correct = models.BooleanField(verbose_name="Правильно")

    def __str__(self):
        return f"Ответ {self.student.user.username} на {self.question.text}"

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
