from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import MyCourse,Lesson,Comment,Category
from .serializers import CourseListSerializer,CourseDetailSerializer,LessonListSerializer,SendCommentSerializer,CategorysListSerializer,QuizSerializer

@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    comment=lesson.comments.all()
    serializer = SendCommentSerializer(comment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_quiz(request,course_slug,lesson_slug):
 lesson=Lesson.objects.get(slug=lesson_slug)
 my_quiz=lesson.quizzes.all()
 serializer = QuizSerializer(my_quiz,many=True)
 return Response(serializer.data)



@api_view(['GET'])
def get_categorys(request):
 categorys=Category.objects.all()
 serializer=CategorysListSerializer(categorys, many=True)
 return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_courses(request):
 category_id = request.GET.get('category_id', '')
 courses=MyCourse.objects.all()
 if category_id:
    courses = courses.filter(categories__in=[int(category_id)])
 serializer = CourseListSerializer(courses,many=True)
 return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_course(request,slug):
 course=MyCourse.objects.get(slug=slug)

 lesson_serializer = LessonListSerializer(course.lessons.all(),many=True)
 course_serializer = CourseDetailSerializer(course)
 
 data= {
  'course': course_serializer.data,
  'lesson': lesson_serializer.data
 }
 return Response(data) 


@api_view(['POST'])
def add_comment(request,course_slug,lesson_slug):
 data=request.data
 name=data.get('name')
 content= data.get('content')

 course=MyCourse.objects.get(slug=course_slug)
 lesson=Lesson.objects.get(slug=lesson_slug)
 comment=Comment.objects.create(name=name,content=content,course=course,lesson=lesson,created_by=request.user)
 return Response({'message':'comment is added'})


# @api_view(['GET'])
# def send_comment(request,course_slug,lesson_slug):
 
