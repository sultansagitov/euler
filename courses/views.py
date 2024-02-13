from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import CourseType, Course, Level, Question, Answer


@admin_required
def createlevel(request: WSGIRequest):
    if request.method != "POST":
        return render(request, "create_level.html", {
            "coursetypes": CourseType.objects.all()
        })
    else:
        level = Level.objects.create(
            course=Course.objects.get(id=request.POST.get("course"))
        )

        ques_count = int(request.POST.get("question-count"))
        for que in range(ques_count):
            Question.objects.create(
                level=level,
                text=request.POST.get(f"question-{que}"),
                choise=[
                    *(request.POST.get(f"question-{que}-choise-{i}") for i in range(1, 5))
                ],
                correct=int(request.POST.get(f"question-{que}-correct"))
            )

        return redirect(reverse("levels"))


@admin_required
def createcourse(request):
    if request.method == "POST":
        Course.objects.create(
            coursetype=CourseType.objects.get(
                id=int(request.POST.get("coursetype"))
            ),
            name=request.POST.get("course")
        )

        return redirect(reverse("levels"))
    else:
        return render(request, "create_course.html", {"coursetypes": CourseType.objects.all()})


@login_required
def levels(request):
    return render(request, "levels.html", {"coursetypes": CourseType.objects.all()})


@login_required
def level(request, lvl):
    obj_level: Level

    # Level finding check
    try:
        obj_level = Level.objects.get(id=lvl)
    except ObjectDoesNotExist:
        return render(request, "messages/levelnotfound.html", {"lvl_index": lvl}, status=404)

    curr_que = -1

    for que_index, question in enumerate(obj_level.question_set.all()):
        if question.answer_set.filter(student=request.user.student).count() == 0:
            curr_que = que_index + 1
            break

    return render(request, "level.html", {"level": obj_level, "next_que": curr_que})


@login_required
def question(request, lvl, que):
    obj_level: Level
    obj_question: Question

    # Level finding check
    if Level.objects.filter(id=lvl).count() != 0:
        obj_level = Level.objects.get(id=lvl)
    else:
        return render(request, "messages/levelnotfound.html", {"lvl_index": lvl}, status=404)

    # Question finding check
    try:
        obj_question = obj_level.question_set.all()[que - 1]
    except IndexError:
        return render(request, "messages/questionnotfound.html", {"lvl_index": lvl, "que_index": que}, status=404)

    if obj_question.answered(request.user) != "notanswered":
        return render(request, "messages/alreadyanswered.html", {"level_pk": obj_level.pk}, status=400)

    if que != 1 and obj_level.question_set.all()[que - 2].answered(request.user) == "notanswered":
        return render(request, "messages/notansweredyet.html", {"lvl_index": lvl, "que_index": que}, status=400)

    if request.user.student.lifes > 0:
        return render(request, "question.html", {"level": obj_level, "question": obj_question, "que_index": que})
    else:
        return render(request, "messages/lifesover.html", {"level_pk": obj_level.pk}, status=400)


@login_required
def math_course(request):
    return render(request, 'mathematics_courses.html', {
        "courses": Course.objects.filter(coursetype=CourseType.objects.get(name="Математика")).all()
    })


@login_required
def tutorial(request, lvl):
    obj_course: Course

    # Course finding check
    if Course.objects.filter(id=lvl).count() != 0:
        obj_course = Course.objects.get(id=lvl)
    else:
        return render(request, "messages/levelnotfound.html", {"lvl_index": lvl}, status=404)

    return render(request, 'tutorial.html', {"tutorial": obj_course.tutorial})
