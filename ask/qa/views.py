#from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Question

def test(request, *args, **kwargs):
    try:
        return HttpResponse('OK')
    except:
        raise Http404

def one_question(request, question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, 'qa/one_question.html', {'question': question})

def popular(request):
    popular_question_list = Question.objects.order_by('-rating')
    limit=request.GET.get('limit', 10)
    page=request.GET.get('page', 1)
    paginator=Paginator(popular_question_list, limit)
    paginator.baseurl='/popular/?page='
    page=paginator.page(page)
    return render(request, 'qa/popular.html',{
            'popular_question_list': page.object_list,
            paginator: paginator, page: page,
    })


def index(request):
    latest_question_list=Question.objects.order_by('-added_at')
    limit=request.GET.get('limit', 10)
    page=request.GET.get('page', 1)
    paginator=Paginator(latest_question_list, limit)
    paginator.baseurl='/?page='
    page=paginator.page(page)
    return render(request, 'qa/index.html',{
            'latest_question_list': page.object_list,
            paginator: paginator, page: page,
    })
