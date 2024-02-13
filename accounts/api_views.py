from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.core.exceptions import ObjectDoesNotExist

import json
from .models import Student, FriendRequest, FriendNotification


def sendrequest(request, touser):
    response_data = {
        "to_user_find": None,

        "to_user": None,
        "to_user_username": None,

        "from_user": None,
        "from_user_username": None,

        "alreadysended": None,
        "myself": None,
    }

    obj_fromuser = request.user.student
    obj_touser: Student

    try:
        obj_touser = Student.objects.get(code=touser)
        response_data["to_user_find"] = True
        response_data["to_user"] = touser
        response_data["to_user_username"] = obj_touser.user.username

    except ObjectDoesNotExist:
        response_data["to_user_find"] = False
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=404)

    if obj_fromuser == obj_touser:
        response_data["myself"] = True
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=300)
    else:
        response_data["myself"] = False

    friendrequest, created = FriendRequest.objects.get_or_create(
        fromuser=obj_fromuser,
        touser=obj_touser,
    )
    
    friendnotification, _ = FriendNotification.objects.get_or_create(
        type="request",
        fromuser=obj_fromuser,
        touser=obj_touser,
    )

    if created:
        response_data["alreadysended"] = False
    else:
        response_data["alreadysended"] = True
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def acceptrequest(request, friendrequest):
    response_data = {
        "friendrequest": None,
        "friendrequest_find": None,

        "fromuser": None,
        "fromuser_username": None,

        "touser": None,
        "touser_username": None,
    }

    obj_friendrequest: FriendRequest

    try:
        obj_friendrequest = FriendRequest.objects.get(id=friendrequest)
        response_data["friendrequest_find"] = True
        response_data["friendrequest"] = friendrequest

        response_data["touser"] = obj_friendrequest.touser.code
        response_data["touser_username"] = obj_friendrequest.touser.user.username

        response_data["fromuser"] = obj_friendrequest.fromuser.code
        response_data["fromuser_username"] = obj_friendrequest.fromuser.user.username

    except ObjectDoesNotExist:
        response_data["friendrequest_find"] = False
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=404)

    obj_friendrequest.fromuser.friends.add(obj_friendrequest.touser)
    obj_friendrequest.touser.friends.add(obj_friendrequest.fromuser)
    obj_friendrequest.fromuser.save()
    obj_friendrequest.touser.save()

    friendnotification, _ = FriendNotification.objects.get_or_create(
        type="accept",
        fromuser=obj_friendrequest.touser,
        touser=obj_friendrequest.fromuser,
    )

    obj_friendrequest.delete()

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def declinerequest(request, friendrequest):
    response_data = {
        "friendrequest": None,
        "friendrequest_find": None,

        "fromuser": None,
        "fromuser_username": None,

        "touser": None,
        "touser_username": None,
    }

    obj_friendrequest: FriendRequest

    try:
        obj_friendrequest = FriendRequest.objects.get(id=friendrequest)
        response_data["friendrequest_find"] = True
        response_data["friendrequest"] = friendrequest

        response_data["touser"] = obj_friendrequest.touser.code
        response_data["touser_username"] = obj_friendrequest.touser.user.username

        response_data["fromuser"] = obj_friendrequest.fromuser.code
        response_data["fromuser_username"] = obj_friendrequest.fromuser.user.username

    except ObjectDoesNotExist:
        response_data["friendrequest_find"] = False
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=404)

    obj_friendrequest.delete()

    
    friendnotification, _ = FriendNotification.objects.get_or_create(
        type="decline",
        fromuser=obj_friendrequest.touser,
        touser=obj_friendrequest.fromuser,
    )

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def unfriend(request, exfriend):
    response_data = {
        "friend": None,
        "friend_find": None,
    }

    obj_exfriend: Student

    try:
        obj_exfriend = Student.objects.get(code=exfriend)
        response_data["friend_find"] = True
        response_data["friend"] = exfriend
        response_data["friend_username"] = obj_exfriend.user.username
    except ObjectDoesNotExist:
        response_data["friend_find"] = False
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=404)

    request.user.student.friends.remove(obj_exfriend)
    obj_exfriend.friends.remove(request.user.student)
    request.user.student.save()
    obj_exfriend.save()

    friendnotification, _ = FriendNotification.objects.get_or_create(
        type="unfriend",
        fromuser=request.user.student,
        touser=obj_exfriend,
    )

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def upload_avatar(request: WSGIRequest):
    if request.method == "POST":
        response_data = {
            "correct": None
        }

        try:
            request.user.student.avatar = request.FILES.get("avatar_img")
            request.user.student.save()
            response_data["correct"] = True
        except:
            response_data["correct"] = False

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse("Method not allowed", content_type="text/plain", status=403)


def change_theme(request: WSGIRequest):
    if request.method == "POST":
        response_data = {
            "correct": None
        }

        try:
            request.user.student.theme = int(request.POST.get("theme"))
            request.user.student.save()
            response_data["correct"] = True
        except:
            response_data["correct"] = False

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse("Method not allowed", content_type="text/plain", status=403)
