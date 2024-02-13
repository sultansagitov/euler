from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Student
from courses.models import CourseType, Course, Level, Question, Answer
from django.db.utils import IntegrityError
from datetime import timedelta


class Command(BaseCommand):
    help = "Initializes all"

    def handle(self, *args, **options):
        math, _ = CourseType.objects.get_or_create(name="Математика")
        
        ariphmetic = Course.objects.create(coursetype=math, name="Арифметика")
        geometry = Course.objects.create(coursetype=math, name="Геометрия")
        math3 = Course.objects.create(coursetype=math, name="Алгебра")
        math4 = Course.objects.create(coursetype=math, name="Теория чисел")
        math5 = Course.objects.create(coursetype=math, name="Тригонометрия")
        math6 = Course.objects.create(coursetype=math, name="Математическая логика и алгоритмы")
        math7 = Course.objects.create(coursetype=math, name="Математическая статистика и вероятность")

        ariphmetic_1 = Level.objects.create(course=ariphmetic)
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(5 + 3\\)",
            choise=["8", "2", "15", "7"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(4 - 2\\)",
            choise=["6", "2", "1", "3"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(6 \\times 4\\)",
            choise=["18", "10", "24", "16"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(9 \\div 3\\)",
            choise=["6", "3", "2", "5"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(10 + 7\\)",
            choise=["14", "17", "21", "8"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(8 - 5\\)",
            choise=["2", "3", "6", "1"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(3 \\times 5\\)",
            choise=["8", "10", "6", "15"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(18 \\div 6\\)",
            choise=["6", "3", "2", "5"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(12 + 9\\)",
            choise=["15", "24", "21", "18"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(10 - 4\\)",
            choise=["6", "2", "14", "8"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(7 \\times 3\\)",
            choise=["15", "24", "21", "18"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_1,
            text="\\(25 \\div 5\\)",
            choise=["6", "5", "2", "10"],
            correct=2
        )

        ariphmetic_2 = Level.objects.create(course=ariphmetic)
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(20 \\div 4\\)",
            choise=["2", "10", "5", "4"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(16 + 7\\)",
            choise=["14", "20", "23", "15"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(18 \\times 3\\)",
            choise=["24", "15", "54", "21"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(14 - 6\\)",
            choise=["4", "7", "8", "10"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(36 \\div 6\\)",
            choise=["6", "10", "8", "4"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(9 \\times 5\\)",
            choise=["36", "20", "14", "45"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(22 + 13\\)",
            choise=["20", "30", "25", "35"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(24 - 9\\)",
            choise=["21", "15", "18", "12"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(7 \\div 2\\)",
            choise=["3", "4", "2.5", "3.5"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(15 \\times 2\\)",
            choise=["20", "30", "18", "25"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(45 \\div 9\\)",
            choise=["3", "6", "4", "5"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_2,
            text="\\(11 + 8\\)",
            choise=["14", "20", "15", "19"],
            correct=4
        )

        ariphmetic_3 = Level.objects.create(course=ariphmetic)
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(4 + 3 \\times 2\\)",
            choise=["10", "8", "14", "7"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(15 \\div 3 + 2\\)",
            choise=["7", "5", "6", "8"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(5 \\times 2 - 3\\)",
            choise=["6", "7", "10", "2"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(12 - 4 \\div 2\\)",
            choise=["4", "8", "10", "6"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(3 + 2 \\times 4\\)",
            choise=["11", "15", "9", "10"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(18 \\div 3 + 1\\)",
            choise=["6", "7", "4", "9"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(5 \\times 3 - 2\\)",
            choise=["15", "9", "8", "13"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(14 - 6 \\div 2\\)",
            choise=["7", "8", "5", "11"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(7 + 2 \\times 3\\)",
            choise=["13", "11", "9", "15"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(21 \\div 3 + 2\\)",
            choise=["8", "10", "9", "7"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(8 \\times 2 - 4\\)",
            choise=["14", "12", "16", "10"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_3,
            text="\\(15 - 4 \\div 2\\)",
            choise=["13", "11", "9", "7"],
            correct=1
        )

        ariphmetic_4 = Level.objects.create(course=ariphmetic)
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(4 + 3 \\times 2 + 5\\)",
            choise=["18", "14", "16", "15"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(15 \\div 3 + 2 \\times 4\\)",
            choise=["15", "13", "18", "20"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(5 \\times 2 - 3 + 7\\)",
            choise=["14", "16", "18", "15"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(12 - 4 \\div 2 + 3\\)",
            choise=["10", "8", "13", "11"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(3 + 2 \\times 4 - 6\\)",
            choise=["9", "11", "5", "7"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(18 \\div 3 + 1 \\times 2\\)",
            choise=["7", "6", "9", "8"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(5 \\times 3 - 2 + 4\\)",
            choise=["17", "15", "9", "12"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(14 - 6 \\div 2 + 1\\)",
            choise=["12", "7", "9", "8"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(7 + 2 \\times 3 - 1\\)",
            choise=["13", "12", "9", "15"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(21 \\div 3 + 2 \\times 3\\)",
            choise=["10", "9", "13", "7"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(8 \\times 2 - 4 + 6\\)",
            choise=["14", "16", "20", "18"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_4,
            text="\\(15 - 4 \\div 2 + 3\\)",
            choise=["20", "9", "13", "7"],
            correct=1
        )

        ariphmetic_5 = Level.objects.create(course=ariphmetic)
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(2x + 5 = 15\\)",
            choise=["8", "5", "7", "10"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(3y - 7 = 11\\)",
            choise=["7", "4", "6", "9"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(4z + 8 = 20\\)",
            choise=["3", "5", "4", "6"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(2a - 3 = 5\\)",
            choise=["2", "3", "4", "6"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(5b + 2 = 27\\)",
            choise=["4", "3", "5.4", "5"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(3c - 4 = 11\\)",
            choise=["7", "6", "5", "5.5"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(4x + 9 = 25\\)",
            choise=["5", "4", "3", "4.5"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(2y - 5 = 11\\)",
            choise=["7", "6", "5", "8"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(5z + 7 = 32\\)",
            choise=["5", "4", "6", "5.5"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(3a - 2 = 10\\)",
            choise=["3", "4", "5", "6"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(2b + 6 = 20\\)",
            choise=["7", "8", "6", "7.5"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_5,
            text="\\(4c - 10 = 14\\)",
            choise=["6", "5", "7", "6.5"],
            correct=1
        )

        ariphmetic_6 = Level.objects.create(course=ariphmetic)
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 2x+y=10 \\\\ 2y-x=5 \\end{array} \\right.\\)",
            choise=["(2, 6)", "(3, 4)", "(1, 8)", "(4, 2)"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} x-2y=8 \\\\ 500x=0 \\end{array} \\right.\\)",
            choise=["(0, -4)", "(3, 2)", "(4, 3)", "(1, 2)"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 2x+y=14 \\\\ 2x-2y=2 \\end{array} \\right.\\)",
            choise=["(4, 6)", "(3, 4)", "(5, 4)", "(1, 8)"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 5x+2.5y=20 \\\\ 2x-y=4 \\end{array} \\right.\\)",
            choise=["(3, 6)", "(2, 4)", "(4, 2)", "(3, 2)"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 2x+2y=16 \\\\ 4x-2y=8 \\end{array} \\right.\\)",
            choise=["(4, 4)", "(3, 2)", "(4, 1)", "(1, 5)"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 2x-y=5 \\\\ 2x+2y=8 \\end{array} \\right.\\)",
            choise=["(2, 1)", "(3, 2)", "(3, 1)", "(4, 3)"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 4y - x = 3 \\\\ 2x + 3y = 16 \\end{array} \\right.\\)",
            choise=["(3, 4)", "(5, 2)", "(4, 1)", "(1, 2)"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 5x + 3y = 23 \\\\ 2x - y = 4 \\end{array} \\right.\\)",
            choise=["\\((1{1 \\over 3}, -1{1 \\over 3})\\)", "(2, 5)", "(4, 3)", "(1, 6)"],
            correct=1
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 3x-y=6 \\\\ 2x+2y=20 \\end{array} \\right.\\)",
            choise=["(2, 1)", "(3, 2)", "(4, 3)", "(4, 6)"],
            correct=4
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 2x+4y=18 \\\\ 2x-y=-7 \\end{array} \\right.\\)",
            choise=["(2, 3)", "(3, 2)", "(-1, 5)", "(1, 5)"],
            correct=3
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \\begin{array}{c} 4x-y=0 \\\\ 4x+4y=30 \\end{array} \\right.\\)",
            choise=["(2, 3)", "(1.5, 6)", "(4, 1)", "(1, 2)"],
            correct=2
        )
        Question.objects.create(
            level=ariphmetic_6,
            text="\\(\\left\\{ \begin{array}{c} 6x-2y=12 \\\\ 3x+y=9 \\end{array} \\right.\\)",
            choise=["(2, 1)", "(3, 2)", "(4, 3)", "(2.5, 1.5)"],
            correct=4
        )

        geometry_1 = Level.objects.create(course=geometry)
        Question.objects.create(
            level=geometry_1,
            text="What is the area of a square with side length 5m?",
            choise=["\\(20m^2\\)", "\\(25m^2\\)", "\\(30m^2\\)", "\\(35m^2\\)"],
            correct=2
        )
        Question.objects.create(
            level=geometry_1,
            text="Find the perimeter of a rectangle with length 8m and width 4m.",
            choise=["\\(16m\\)", "\\(24m\\)", "\\(32m\\)", "\\(40m\\)"],
            correct=3
        )
        Question.objects.create(
            level=geometry_1,
            text="Calculate the circumference of a circle with radius 6m.",
            choise=["\\(12\\pim\\)", "\\(18\\pim\\)", "\\(24\\pim\\)", "\\(36\\pim\\)"],
            correct=1
        )
        Question.objects.create(
            level=geometry_1,
            text="A triangle has angles of 30°, 60°, and 90°. What is the length of the hypotenuse if the leg opposite the 60° angle is 3m?",
            choise=["\\(3m\\)", "\\(4m\\)", "\\(5m\\)", "\\(6m\\)"],
            correct=3
        )
        Question.objects.create(
            level=geometry_1,
            text="Find the volume of a rectangular prism with length 5m, width 3m, and height 2m.",
            choise=["\\(20\\)m^3", "\\(30\\)m^3", "\\(40\\)m^3", "\\(50\\)m^3"],
            correct=1
        )
        Question.objects.create(
            level=geometry_1,
            text="Calculate the area of a parallelogram with base 7m and height 4m.",
            choise=["\\(24m^2\\)", "\\(28m^2\\)", "\\(30m^2\\)", "\\(32m^2\\)"],
            correct=2
        )
        Question.objects.create(
            level=geometry_1,
            text="What is the surface area of a cube with side length 3m?",
            choise=["\\(18m^2\\)", "\\(27m^2\\)", "\\(36m^2\\)", "\\(54m^2\\)"],
            correct=4
        )
        Question.objects.create(
            level=geometry_1,
            text="Determine the angle sum of a hexagon.",
            choise=["\\(360\\deg\\)", "\\(420\\deg\\)", "\\(480\\deg\\)", "\\(540\\deg\\)"],
            correct=3
        )
        Question.objects.create(
            level=geometry_1,
            text="If the diagonal of a square is 10m, what is the length of each side?",
            choise=["\\(5m\\)", "\\(7m\\)", "\\(8m\\)", "\\(10m\\)"],
            correct=1
        )
        Question.objects.create(
            level=geometry_1,
            text="Find the area of a circle with diameter 12m.",
            choise=["\\(36πm^2\\)", "\\(48πm^2\\)", "\\(64πm^2\\)", "\\(72πm^2\\)"],
            correct=3
        )
        Question.objects.create(
            level=geometry_1,
            text="A right-angled triangle has legs of length 9m and 12m. What is the length of the hypotenuse?",
            choise=["\\(15m\\)", "\\(18m\\)", "\\(21m\\)", "\\(24m\\)"],
            correct=1
        )
        Question.objects.create(
            level=geometry_1,
            text="Calculate the volume of a cylinder with radius 4m and height 10m.",
            choise=["\\(80\\pim^3\\)", "\\(120\\pim^3\\)", "\\(160\\pim^3\\)", "\\(200\\pim^3\\)"],
            correct=2
        )
