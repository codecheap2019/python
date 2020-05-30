from django.shortcuts import get_object_or_404,render

# Create your views here.

from django.http import HttpResponse


from django.template import loader 

from .models import Question 

from .models import Users

from .forms import RegistrationForm

def register(request):
		form = RegistrationForm()
		context = { 'myregistrationform': form, }
		return render(request, 'polls/register.html',context)
		
def users(request):
		users = Users.objects.order_by('-email')[:5]
		context = { 'users': users }
		return render(request, 'polls/user.html',context)
		
def index(request): 
		latest_question_list = Question.objects.order_by('-pub_date')[:5] 
		template = loader.get_template('polls/index.html') 
		context = { 'latest_question_list': latest_question_list, } 
		return HttpResponse(template.render(context, request))
		
def detail(request, question_id): 
		question = get_object_or_404(Question, pk=question_id) 
		return render(request, 'polls/details.html', {'question': question})		

def test(request):
		return render(request, 'polls/test.html')
		
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)