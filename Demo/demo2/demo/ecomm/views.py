from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
import string
from spell_corector import checkspell

# function to render first page
def index(request):
	print 'here'
	return render(request,'index.html')
# function to return Meaning 
@csrf_exempt
def calculate(request):
	if request.method == 'GET':
		return render(request,'index.html')
	word = request.POST.get('word','bank')
	word = str(word)
	word = word.title()
	print word
	checkspell_object = checkspell(dict_name='en_US',max_dist=2)
	suggestions = checkspell_object.checks(word)
	result = {'result':suggestions}
	return render(request,'index.html',context=result)
# function to return Cosine distance
@csrf_exempt
def cos(request):
	if request.method == 'GET':
		return render(request,'index.html')
	word = request.POST.get('word','bank')
	word = str(word)
	word = word.title()
	print word
	checkspell_object = checkspell(dict_name='en_US',max_dist=2)
	cos_distance_suggestions,cos_list = checkspell_object.nearest_word(word)
	result = {'result':list(cos_list)}
	return render(request,'index.html',context=result)
# function to add words
@csrf_exempt
def add(request):
	if request.method == 'GET':
		return render(request,'index.html')
	word = request.POST.get('word','bank')
	word = str(word)
	word = word.title()
	checkspell_object = checkspell(dict_name='en_US',max_dist=2)
	result = checkspell_object.add(word)
	result = {'result':result}
	return render(request,'index.html',context=result)
# function to do bayseian probability spelling check
@csrf_exempt
def bays(request):
	if request.method == 'GET':
		return render(request,'index.html')
	print request.POST.get('word','bank')
	word = request.POST.get('word','bank')
	word = str(word)
	word = word.title()
	bays_object = checkspell(dict_name='en_US',max_dist=2)
	bays_result = bays_object.correct(word)
	print bays_result
	result = {'result':bays_result}
	return render(request,'index.html',context=result)