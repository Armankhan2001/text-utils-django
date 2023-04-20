from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse ("<h1>Hello</h1> <a href=https://www.youtube.com/results?search_query=django+code+with+harry > Django playlist </a>")
    # params={'name':'harry','place':'mars'}
    # return render(request,'index.html' ,params)
    # return render(request,'index.html')
    return render(request,'index.html')

def analyze(request):
# def removepunc(request):
    #Get the text
    djtext=request.POST.get('text','default')
    #checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    # print(removepunc)
    # print(djtext)

    #check with checkbox is on
    if removepunc=="on":
        # return HttpResponse("remove punc")  
        #Analyze the text
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        print('params',params)
        djtext=analyzed
        # return render(request,'analyzed.html',params)
    if (fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Capitalized text','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyzed.html',params)
    
    if (newlineremover == "on"):
        analyzed=""
        for char in djtext:
                if char!="\n" and char!="\r":
                    analyzed+=char

        params={'purpose':'Removed new line','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyzed.html',params)
    
    if (extraspaceremover == "on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char
        params={'purpose':'Extra spaces removed','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyzed.html',params)
    
    if (charcount == "on"):
        analyzed=""
        c=''
        for char in djtext:
            if char !=" ":
                c+=char
                analyzed=len(c)
        params={'purpose':'Character Counts','analyzed_text':analyzed}
       
        return render(request,'analyzed.html',params)
    if (removepunc!="on" and newlineremover != "on"and extraspaceremover!= "on" and charcount != "on"):
        return HttpResponse ("Error, Please select any operation")

    # else:
        # return HttpResponse("Error")
    return render(request,'analyzed.html',params)



















# def capfirst(request):
#     return HttpResponse("capitaize first")

# def newlineremover(request):
#     return HttpResponse("new line remove first")

# def spaceremove(request):
#     return HttpResponse("space remove <br> <br><button><a  href='/'> back </a></button>")

# def charcount(request):
#     return HttpResponse ("charcount")

# def index(request): 
#     file = open("1s.txt",'r+')
#     return HttpResponse(file.read())