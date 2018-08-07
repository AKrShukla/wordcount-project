from django.shortcuts import render
import operator
def homepage(request) :
    return render(request,'home.html')
def count(request) :
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    a={}
    for word in wordlist :
        if word in a :
            a[word]+=1
        else :
            a[word]=1
    z=sorted(a.items() , key=operator.itemgetter(1) , reverse=True)
    s={'fulltext' : fulltext , 'count' : len(wordlist) , 'worddictionary' : z}
    return render(request,'count.html',s)
def about(request) :
    return render(request,'about.html')
