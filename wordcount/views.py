from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET.get('fulltext')
    wordlist = fulltext.split()
    worddict={}
    for word in wordlist:
        if word not in worddict:
            worddict[word]=1
        else:
            worddict[word]+=1
    sorted_words = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sorted_dict':sorted_words})

def about(request):
    return render(request,'about.html')
