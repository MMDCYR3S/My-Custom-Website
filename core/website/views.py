from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from accounts.models import User, Profile
from .models import WorkSamples

# Index page
def index_view(request):
    """ Main page that contains contact form and other stuff. """
    samples = WorkSamples.objects.filter(status=True).order_by("created_date")[:3]
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد.")
        else:
            messages.error(request, ("پیام شما ارسال نشد!"))
    
    form = ContactForm()
    context = {
        "form": form,
        "samples": samples,
        
        'meta_title': 'صفحه اصلی | تواین دیزاین',
        'meta_description': 'تیم تواین دیزاین، طراحی وبسایت‌های تخصصی شما را به عهده می‌گیرد',
        'meta_keywords': 'django, website, صفحه اصلی, SEO, تواین دیزاین, طراحی سایت, جنگو, twinvibedesign',
        }
    return render(request, "website/index.html", context)

# About page
def about_view(request):
    """ Showing developer's information from database. """
    mamad = User.objects.get(email=("amingholami06@gmail.com"))
    arashk = User.objects.get(email=("arashkzolghadr993@gmail.com"))
    m_profile = Profile.objects.get(user=mamad)
    a_profile = Profile.objects.get(user=arashk)
    context = {
        "m_profile" : m_profile,
        "a_profile" : a_profile,
        'meta_title': 'درباره ما | تواین دیزاین',
        'meta_description': 'تیم تواین دیزاین، طراحی وبسایت‌های تخصصی شما را به عهده می‌گیرد',
        'meta_keywords': 'django, website, درباره ما, SEO, تواین دیزاین, طراحی سایت, جنگو, twinvibedesign',
        }
    return render(request, "website/about.html", context)

# Contact page
def contact_view(request):
    """ Show contact page and make ContactForm work in page. """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد.")
        else:
            messages.error(request, ("پیام شما ارسال نشد!"))
    
    mamad = User.objects.get(email=("amingholami06@gmail.com"))
    arashk = User.objects.get(email=("arashkzolghadr993@gmail.com"))
    m_profile = Profile.objects.get(user=mamad)
    a_profile = Profile.objects.get(user=arashk)
    
    form = ContactForm()
    context = {
        'meta_title': 'ارتباط با ما | تواین دیزاین',
        'meta_description': 'شما می‌توانید از طریق ایمیل یا شماره تماس با ما در ارتباط باشید',
        'meta_keywords': 'django, website, ارتباط با ما, SEO, تواین دیزاین, طراحی سایت, جنگو, twinvibedesign',
        "form": form,
        "m_profile" : m_profile,
        "a_profile" : a_profile,
        }
    return render(request, "website/contact.html", context)

# Resume View
def resume_view(request):
    """ Show more information about work samples in website. """
    samples = WorkSamples.objects.filter(status=True)
    context = {
        "samples" : samples,
    }
    return render(request, "website/resume.html", context)
