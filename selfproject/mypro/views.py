from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone #시간변수 생성할 때 필요


def index(request):
    question_list = Question.objects.order_by('create_date')
    context = {'question_list':question_list}

    return render(request,'mypro/question_list.html',context)

def detail(request,question_id):
    question =get_object_or_404(Question,pk=question_id)
    context={'question':question}
    return render(request,'mypro/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #answer모델이 foreign 키로 question 모델을 참조하고 있기 때문에 위와같이 쓸 수 있음
    #위의 content는 form태그 내의 어떤 내용을 가져올 지 id로 지정한것
    return redirect('mypro:detail', question_id=question.id)