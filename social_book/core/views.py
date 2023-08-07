from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth 
from django.contrib.auth import authenticate , login
from django.contrib import messages
from .models import Profile , Post,postliker ,Follow_user 
from django.contrib.auth.decorators import login_required
from itertools import chain
import random
# Create your views here.

@login_required(login_url='signin')
def index(request):
    user_obj = User.objects.get(username=request.user.username) 
    user_profile= Profile.objects.get(user=user_obj)
    # posts = Post.objects.all()
    
    following_list_user= []
    images= []

    following_user= Follow_user.objects.filter(follow= request.user.username)

    for users in following_user:
        following_list_user.append(users.user)

    for usernames in following_list_user:
        image_lists= Post.objects.filter(user=usernames)
        images.append(image_lists)

    image_list = list(chain(*images))
    
    users_all = User.objects.all()
    user_following_all= []

    for users in following_user:
        user_list= User.objects.get(username = users.user) 
        user_following_all.append(user_list)

    suggestions = [x for x in list(users_all) if (x not in list(user_following_all))]
    current = User.objects.filter(username= request.user.username)
    new_sugestions= [x for x in list(suggestions) if (x not in list(current))]
    random.shuffle(new_sugestions)
    profile_user= []
    profile_user_list=[]

    for users in new_sugestions:
        profile_user.append(users.id)

    for ids in profile_user:
        profiles= Profile.objects.filter(id_user=ids)
        profile_user_list.append(profiles)
    
    suggestions_users = list(chain(*profile_user_list))

    return render(request, 'index.html',{'user_profile' : user_profile,'post':image_list ,"suggestions_users":suggestions_users})
@login_required(login_url='signin')
def like_post(request):
    username= request.user.username
    post_id= request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    Like_f= postliker.objects.filter(post_id=post_id ,username=username).first()

    if Like_f == None:
        newlike= postliker.objects.create(post_id=post_id,username=username)
        newlike.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('index')

    else:
        Like_f.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('index')
def signup(request):

    if request.method == 'POST':
        username= request.POST['Username']
        email= request.POST['E_mail']
        password= request.POST['Password']
        password2= request.POST['Confirm Password']

        
        if password !=password2:
            messages.error(request, "Password didn't matched")
            return  redirect('signup')
        
        else:

            if User.objects.filter(email=email).exists():
                messages.info(request,'Email is already registered! Please try another one.')
                return redirect ('signup')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,"user is taken!")
                return redirect('signup')
            
            else:
                reg= User.objects.create_user(username= username, email= email,password= password)
                reg.save()
                messages.success(request,'Your Profile has been Created successfully , Now you can login here...')
                
                user_login= authenticate(request,username=username,password=password)
                login(request,user_login)


                user_model=User.objects.get(username=reg)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('setting')

    return render(request,'signup.html')
@login_required(login_url='signin')
def profile(request,sk):
    us_ob= User.objects.get(username=sk)
    us_profile_ob= Profile.objects.get(user=us_ob)
    us_post= Post.objects.filter(user=sk)
    length_post= len(us_post)

    follower = request.user.username
    user= sk

    if Follow_user.objects.filter(follow = follower , user=user).first():
        button= "Unfollow"
    
    else:
        button="Follow"

    follower_user = len(Follow_user.objects.filter(user=sk))
    following_user = len(Follow_user.objects.filter(follow=sk))

    data={
        'us_ob':us_ob,
        'us_profile_ob':us_profile_ob,
        'us_post':us_post,
        'length_post':length_post,
        'button': button,
        'follower_user':follower_user,
        'following_user' :following_user
    }
    
    return render(request,'profile.html',data)
@login_required(login_url='signin')
def settings(request):
    user_profile= Profile.objects.get(user=request.user)

    if request.method== "POST":
        if request.FILES.get("image") == None:
            image= user_profile.profileimg
            bio = request.POST['Bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location

            user_profile.save()

    if request.method =="POST":
        if request.FILES.get('image') != None:
            image= request.FILES['image']
            bio = request.POST['Bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location

            user_profile.save()
    

        return redirect('setting')


    return render(request,'setting.html',{"user_profile":user_profile})
@login_required(login_url='signin')
def search(request):
    user_obj= User.objects.get(username= request.user.username)
    profile_img= Profile.objects.get(user=user_obj)
    if request.method == 'POST':
        search= request.POST['search']
        user_objects= User.objects.filter(username__icontains=search)

        username_profile= []
        user_profile_list=[]

        for users in user_objects:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists= Profile.objects.filter(id_user= ids)
            user_profile_list.append(profile_lists)
        user_profile_list = list(chain(*user_profile_list))
    return render(request,'serach.html',{'user_profile_list':user_profile_list,'profile_img':profile_img})
@login_required(login_url='signin')
def upload(request):
    if request.method =='POST': 
        user= request.user.username
        image=request.FILES.get('image')    
        caption= request.POST.get('caption')

        new_post=Post.objects.create(user=user,image=image,caption=caption)
        new_post.save()

        return redirect('index')


    else:
        return redirect('index')
@login_required(login_url='signin')
def follow(request):
    if request.method =="POST":
        
        follow = request.POST['follower']
        user = request.POST['user']
        
        if Follow_user.objects.filter(follow=follow, user=user).first():
            print('hello')
            delete_follow= Follow_user.objects.get(follow=follow ,user=user)
            delete_follow.delete()

            return redirect ('/profile/'+ user)

        else:

            add_new_following  = Follow_user.objects.create(follow=follow,user=user)
            print('hii')
            add_new_following.save()
            return redirect ('/profile/'+ user)
        
    else:
        print("nothing")
        return redirect('index')
        
def signin(request):


    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['password']

        user= authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            messages.warning(request,"Invalid Username or Passowrd!! Try Again")
            return redirect("signin")
            
    return render (request,'signin.html')