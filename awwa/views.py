from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Project,Profile,Rating
from .forms import awwaLetterForm,NewProjectForm,ProfileUploadForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# # Create your views here.
# def welcome(request):
#     return render('Welcome to Awwards')
@login_required(login_url='/accounts/login/')
def awwa_today(request):
    date = dt.date.today()
    # all_images = .all_images()
    images= Project.objects.all()
    print(images)
    # image = Image.today-photos()
    if request.method == 'POST':
        form = awwasLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipient = awwasLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('awwas_today')
    else:
        form = awwaLetterForm()
        form = NewProjectForm()
    return render(request, 'all-awwa/today-awwa.html', {"date": date,"letterForm":form, "ImageForm":form,'images':images})


def past_days_awwa(request, past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(awwas_today)

    awwa_today = Project.past_days_awwa(date)
    return render(request, 'all-awwa/past-awwa.html',{"date": date,"awwa":awwa})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_images = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-awwa/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awwa/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-awwa/image.html", {"image":image})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    title = 'New image'
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('AwwaToday')

    else:
        form = NewProjectForm()
    return render(request, 'new_image.html', {"form": form,"current_user":current_user,"title":title})

@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['image']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(image = form.cleaned_data['image'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})

def votes(request,id):
    current_user = request.user
    post = Project.objects.get(id=id)
    votes = Votes.objects.filter(project=post)
  
    if request.method == 'POST':
            vote = VotesForm(request.POST)
            if vote.is_valid():
                design = vote.cleaned_data['design']
                usability = vote.cleaned_data['usability']
                content = vote.cleaned_data['content']
                rating = Votes(design=design,usability=usability,content=content,user=request.user,project=post)
                rating.save()
                return redirect(index)      
    else:
        form = VotesForm()
        return render(request, 'new-vote.html', {"form":form,'post':post,'user':current_user,'votes':votes})

