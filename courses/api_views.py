from django.http import HttpResponse
import json
from .models import CourseType, Course, Level, Question, Answer


def getanswer(request, lvl, que, ans):
    response_data = {
        "correct": None,
        "answered": None,
        "levelfind": None,
        "questionfind": None,
    }

    obj_level: Level
    obj_question: Question

    # Level finding check
    if Level.objects.filter(id=lvl).count() != 0:
        obj_level = Level.objects.get(id=lvl)
        response_data['levelfind'] = True
    else:
        response_data['levelfind'] = False
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=404)

    # Question finding check
    try:
        obj_question = obj_level.question_set.all()[que - 1]
        response_data['questionfind'] = True
    except IndexError:
        response_data['questionfind'] = False
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=404)

    # Already answered check
    if Answer.objects.filter(student=request.user.student, question=obj_question).count() == 0:
        response_data["answered"] = False
    else:
        response_data["answered"] = True
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)

    is_correct = ans == obj_question.correct

    Answer.objects.create(
        student=request.user.student,
        question=obj_question,
        correct=is_correct
    )

    response_data["correct"] = is_correct

    if is_correct:
        request.user.student.crystals += 20
    else:
        request.user.student.lifes -= 1

    request.user.student.save()

    return HttpResponse(json.dumps(response_data), content_type="application/json")
