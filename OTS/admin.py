from django.contrib import admin
from .models import Candidate,Question,Result
# Register your models here.

# Register candidate ,Question, result admin with admin .Also it will show as a table in ADMIN interface bcoz of Model Admin
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display=['username','name','password','test_attempted','points']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['qid','ques','a','b','c','d','ans']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display=['resultid','username','date','time','attempt','right','wrong','points']