from django.shortcuts import render, get_object_or_404

from .models import Content, Issue, Bio

# Create your views here.
def index(request):
    return render(request, 'beholder/index.html')

def archive(request):
    issue_list = Issue.objects.all()
    return render(request, 'beholder/backissues.html', {'issue_list': issue_list})

def issue(request, issue_num):
    issue_details = get_object_or_404(Issue, issue_num=issue_num)
    return render(request, 'beholder/issue.html', {'issue_details': issue_details})

def content_detail(request, issue_num, slug):
    content_details = get_object_or_404(Content, slug=slug)
    css_class = content_details.get_content_class()
    if css_class == 'comic':
        return render(request, 'beholder/carousel.html', {'content_details': content_details})
    elif css_class == 'ednote':
        return render(request, 'beholder/ednote.html', {'content_details': content_details})
    else:
        return render(request, 'beholder/content.html', {'content_details': content_details})

def contributors(request):
    contributor_list = Bio.objects.all()
    return render(request, 'beholder/contributors.html', {'contributor_list': contributor_list})

def current(request):
    current_issue = Issue.objects.first()
    return issue(request, current_issue.issue_num)

def submit(request):
    return render(request, 'beholder/submit.html')