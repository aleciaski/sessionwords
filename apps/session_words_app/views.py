from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
  # the index function is called when root is visited
def index(request):
	# response = "Hello, I am your first request!"
	# print("this is the index, yo!")
	if "response" not in request.session:
		request.session['response']=[]
	print(request.session['response'])
	return render(request,'session_words_app/index.html')

def process(request):
	print("We are in process")
	print(request.POST)
	word = request.POST['new_word']
	color= request.POST['color']
	size= request.POST['font']
	
	context={
			'word' : word,
			'color' : color,
			'size' : size,
			"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
			} 
	request.session['response'].append(context)
	request.session.modified = True
	print (request.session['response'])
	# temp_list = request.session['response']
	# # temp_list.append("hi")
	# # temp_list.append("bye")
	# # print (temp_list)
	# temp_list.append({"word": word, "color": color, "size": size})
	# request.session['word'] = temp_list
	return redirect('/')

def reset(request):
	request.session.clear()
	
	print("im in reset")
	return redirect('/')

