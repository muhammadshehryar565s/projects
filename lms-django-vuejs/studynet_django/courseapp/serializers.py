from rest_framework import serializers
from .models import MyCourse,Lesson,Comment,Category,Quiz


class CategorysListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = ('id','title','slug')

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourse
        fields = ('id','title','short_discription','slug','image','status')

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=('id','question','answer','op1','op2','op3')        
        
# class CourseListSerializer(serializers.ModelSerializer):
#     image = serializers.SerializerMethodField()

#     class Meta:
#         model = MyCourse
#         fields = ('id', 'title', 'short_discription', 'slug', 'image', 'status')

#     def get_image(self, obj):
#         request = self.context.get('request')
#         if obj.image:
#             return request.build_absolute_uri(obj.image.url)
        # return None        

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourse
        fields = ('id','title','short_discription','slug','long_discription')        


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Lesson
        fields = ('id','title','short_discription','slug','long_discription','lesson_type','vedio_id')
         

class SendCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = ('id','name','content','created_at')