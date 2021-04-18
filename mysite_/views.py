# i have created this file -arpit
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     with open("1.txt", "r") as f:
#         x=f.read()
#         return HttpResponse(x)

# khud bnaya hai, diye hue name pr click krne se site khulegi
# def index(request):
#   s = '''<h1>Arpit</h1> <a href="https://www.youtube.com/c/CodeWithHarry"> <h1>Django Codewotharpit</h1></a>
#           <a href="https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwidp6-LzIPwAhXizzgGHR-oAy4QPAgI"> <h1>GOogle</h1> </a><br>
#           <a href="https://www.facebook.com/"> <h1>Facebook</h1></a><br>
#           <a href="https://www.linkedin.com/feed/"> <h1>LInkedin</h1></a><br>
#           <a href="https://www.netflix.com/in/"> <h1>Netflix</h1> </a>'''
#   return HttpResponse(s)
def index(request):
    return render(request, 'index.html')

def analyze(request): 
    #get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!"#$%&'()*+, -.:;<=>?@[]/^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'removed punctuations', 'analyzed_text': analyzed}
        #analyze the text
        djtext = analyzed
    if (fullcaps=="on"):
        analyzed = djtext.upper()
        params = {'purpose' : 'changed to uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
    if (newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text':analyzed}
        djtext = analyzed
    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]== " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text':analyzed}
        djtext =analyzed
    if (charcount=="on"):
        analyzed = 0
        for char in djtext:
            if char != "/n":
                analyzed = analyzed+1
        params = {'purpose': 'Remove New Line', 'analyzed_text':analyzed}
    if (removepunc != 'on'and newlineremover != 'on'and extraspaceremover != 'on' and charcount != 'on'and fullcaps != 'on' ):
        return HttpResponse(djtext)           
    #return render(request, 'analyze.html', params)
    #else:
        #return HttpResponse("aaaaa")
   
    return render(request, 'analyze.html', params)
def about(request):
    return render(request, 'about.html')

