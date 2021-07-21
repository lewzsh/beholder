import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Content, Issue, Bio

def index(request):
    latest_issues = Issue.objects.filter(release_date__lte=datetime.date.today())[:4]
    return render(request, 'beholder/index.html', {'latest_issues': latest_issues})

def archive(request):
    issue_list = Issue.objects.filter(release_date__lte=datetime.date.today())
    return render(request, 'beholder/archive.html', {'issue_list': issue_list})

def issue(request, issue_num):
    issue_details = get_object_or_404(Issue, issue_num=issue_num)
    if (issue_details.issue_published()):
        first_page = get_object_or_404(issue_details.contents, page=1)
        return render(request, 'beholder/issue.html', {'issue_details': issue_details, 'first_page': first_page})
    else:
        return HttpResponse("That issue is not published yet")

def content_detail(request, issue_num, slug):
    content_details = get_object_or_404(Content, slug=slug)
    if (content_details.content_published()):
        css_class = content_details.get_content_class()
        if css_class in ['comic', 'gallery']:
            content_details.create_list()
        next = content_details.next()
        previous = content_details.previous()
        page = './page/' + css_class + '.html'
        return render(request, 'beholder/page/' + css_class + '.html', {'content_details': content_details, 'next': next, 'previous': previous, 'page': page})
    else:
        return HttpResponse("That content is not published yet")

def contributors(request):
    contributor_list = Bio.objects.all()
    return render(request, 'beholder/contributors.html', {'contributor_list': contributor_list})

def current(request):
    current_issue = Issue.objects.filter(release_date__lte=datetime.date.today()).first()
    return issue(request, current_issue.issue_num)

def submit(request):
    return render(request, 'beholder/submit.html')
