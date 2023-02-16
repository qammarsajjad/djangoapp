from django.shortcuts import render

posts =[
    {
        'author':'Qammarsajjad',
        'title':'Django-Post',
        'content':'Blog-Post1',
        'date_posted':'23 August 2022'
    },

      {
        'author':'Arham Javed',
        'title':'Javascript-Post',
        'content':'Blog-Post2',
        'date_posted':'23 August 2022'
    }
]



def Home(request):
    context  = {'posts':posts}
    return render(request,'blog/home.html',context)

def About(request):
   return render(request,'blog/about.html',{'title':'About'})
