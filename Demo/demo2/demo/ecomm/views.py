from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
import string
from spell_corector import checkspell

def index(request):
	print 'here'
	return render(request,'index.html')

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
	# cos_distance_suggestions = checkspell_object.nearest_word(word)
	return render(request,'index.html',context=result)

@csrf_exempt
def cos(request):
	if request.method == 'GET':
		return render(request,'index.html')
	word = request.POST.get('word','bank')
	word = str(word)
	word = word.title()
	print word
	checkspell_object = checkspell(dict_name='en_US',max_dist=2)
	# suggestions = checkspell_object.checks(word)
	cos_distance_suggestions,cos_list = checkspell_object.nearest_word(word)
	print cos_distance_suggestions
	result = {'result':list(cos_distance_suggestions,cos_list)}
	return render(request,'index.html',context=result)

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

@csrf_exempt
def bays(request):
	if request.method == 'GET':
		return render(request,'index.html')
	print request.POST.get('word','bank')
	word = request.POST.get('word','bank')
	word = str(word)
	word = word.title()
	# print word
	bays_object = checkspell(dict_name='en_US',max_dist=2)
	# # suggestions = checkspell_object.checks(word)
	bays_result = bays_object.correct(word)
	print bays_result
	result = {'result':bays_result}
	return render(request,'index.html',context=result)