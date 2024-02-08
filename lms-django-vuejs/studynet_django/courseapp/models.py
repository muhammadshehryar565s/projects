from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    short_discription=models.TextField(null=True)
    created_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class MyCourse(models.Model):
    DRAFT = 'draft'
    IN_REVIEW = 'in_review'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (IN_REVIEW, 'In review'),
        (PUBLISHED, 'Published')
    )
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    short_discription=models.TextField(null=True)
    created_at=models.DateField(auto_now_add=True)
    long_discription=models.TextField(null=True)
    created_by = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title
    


class Lesson(models.Model):
    DRAFT =  'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')

    )  

    ARTICLE = 'article'
    QUIZ = 'quiz'
    VEDIO = 'vedio'

    CHOICES_LESSON_TYPE =(
        (ARTICLE,'Article'),
        (QUIZ, 'Quiz'),
        (VEDIO, 'Vedio')

    )

    course= models.ForeignKey(MyCourse,related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    short_discription=models.TextField(blank=True,null=True)
    long_discription=models.TextField(blank=True,null=True)
    state = models.CharField(max_length=20, choices=CHOICES_STATUS, default=PUBLISHED)
    lesson_type=models.CharField(max_length=20,choices=CHOICES_LESSON_TYPE, default= ARTICLE)
    vedio_id= models.CharField(max_length=100,blank=True,null=True)



    def __str__(self):
        return self.title



class Comment(models.Model):
    course=models.ForeignKey(MyCourse,related_name='comments',on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by= models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'comments'


class Quiz(models.Model):
    lesson=models.ForeignKey(Lesson,related_name='quizzes', on_delete=models.CASCADE)
    question= models.CharField(max_length=200,null=True)
    answer=models.CharField(max_length=200,null=True)
    op1=models.CharField(max_length=200,null=True)
    op2=models.CharField(max_length=200,null=True)
    op3=models.CharField(max_length=200,null=True)

    class Meta:
        verbose_name_plural = 'Quizzes'

    
