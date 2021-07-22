import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Issue, Person, Bio, Content
from .views import *

# Model tests
class IssueTests(TestCase):
    def setUp(self):
        self.testIssue = Issue(issue_num = 3, 
                            release_date = datetime.date(2021, 6, 10), 
                            cover_img_url = "https://picsum.photos/200/300")
        self.testIssue2 = Issue(issue_num = 4, 
                            release_date = datetime.date(2022, 8, 10), 
                            cover_img_url = "https://picsum.photos/200/300")

    def test_issuetablename(self):
        self.assertEqual(str(Issue._meta.db_table), "issue")

    def test_issuestring(self):
        self.assertEqual(str(self.testIssue), "issue 3")

    def test_issue_published(self):
        self.assertTrue(self.testIssue.issue_published())
        self.assertFalse(self.testIssue2.issue_published())

class PersonTests(TestCase):
    def setUp(self):
        self.testAbby = Person(first_name = "Abby", 
                            last_name = "Normal", 
                            role = "Contributor")
        self.testLewis = Person(first_name = "Lewis",
                            role = "Publisher")

    def test_persontablename(self):
        self.assertEqual(str(Person._meta.db_table), "person")

    def test_personstring(self):
        self.assertEqual(str(self.testAbby), "Abby Normal")
        self.assertEqual(str(self.testLewis), "Lewis ")


class BioTests(TestCase):
    def setUp(self):
        self.testAbby = Person(first_name = "Abby", 
                            last_name = "Normal", 
                            role = "Contributor")
        self.testAbbyBio = Bio(person = self.testAbby,
                            pronouns = "she/her",
                            social_url = "https://www.instagram.com/",
                            bio_text = "Not abnormal at all",
                            bio_img_url = "https://picsum.photos/200/300")

    def test_biotablename(self):
        self.assertEqual(str(Bio._meta.db_table), "bio")

    def test_biostring(self):
        self.assertEqual(str(self.testAbbyBio), "Abby Normal's bio")

class ContentTests(TestCase):
    def setUp(self):
        self.testIssue = Issue.objects.create(issue_num = 3, 
                            release_date = datetime.date(2021, 8, 10), 
                            cover_img_url = "https://picsum.photos/200/300")
        self.testAbby = Person.objects.create(first_name = "Abby", 
                            last_name = "Normal", 
                            role = "Contributor")
        self.testPoem = Content.objects.create(title = "Raven",
                            issue = self.testIssue,
                            slug = "raven",
                            pub_date = datetime.date(2021, 6, 10),
                            page = 2,
                            css_class = 'poem',
                            body = "poem goes here")
        self.testStory = Content.objects.create(title = "Fragile Things",
                            issue = self.testIssue,
                            slug = "fragile-things",
                            pub_date = datetime.date(2022, 1, 11),
                            page = 3,
                            css_class = 'short',
                            body = "book here")
        self.testAbby.appears_in.set([self.testIssue])
        self.testPoem.creator.set([self.testAbby])
        self.testStory.creator.set([self.testAbby])
        
    def test_contenttablename(self):
        self.assertEqual(str(Content._meta.db_table), "content")
    
    def test_contentstring(self):
        self.assertEqual(str(self.testPoem), "Raven")

    def test_css_class(self):
        self.assertEqual(self.testPoem.get_content_class(), 'poem')   

    def test_set_author(self):
        self.assertEqual(self.testPoem.creator.count(), 1)
        self.assertEqual(str(self.testPoem.creator.get()), "Abby Normal")

    def test_set_appearsin(self):
        self.assertEqual(str(self.testAbby.appears_in.get()), "issue 3")
        self.assertNotEqual(str(self.testAbby.appears_in.get()), "issue 2")

    def test_abs_url(self):
        self.assertEqual(self.testPoem.get_absolute_url(), '/beholder/issue3/raven')

    def test_content_published(self):
        self.assertTrue(self.testPoem.issue.issue_published())
        self.assertFalse(self.testStory.issue.issue_published())

# View tests

# Auth tests