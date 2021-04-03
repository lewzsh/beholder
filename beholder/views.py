from django.shortcuts import render, get_object_or_404

from .models import Content, Issue, Bio

# Create your views here.
def index(request):
    return render(request, 'beholder/index.html')

def archive(request):
    issue_list = Issue.objects.all()
    return render(request, 'beholder/backissues.html', {'issue_list': issue_list})

def issue(request, id):
    issue_details = get_object_or_404(Issue, pk=id)
    table_of_contents = issue_details.contents.all()
    return render(request, 'beholder/issue.html', {'issue_details': issue_details, 'toc': table_of_contents})

def content_detail(request, id):
    content_details = get_object_or_404(Content, pk=id)
    return render(request, 'beholder/content.html', {'content_details': content_details})

def contributors(request):
    contributor_list = Bio.objects.all()
    return render(request, 'beholder/contributors.html', {'contributor_list': contributor_list})