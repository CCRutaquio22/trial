import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
 
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#Guestbbok Module

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

# [START greeting]
class Greeting(ndb.Model):
    """Models an individual Guestbook entry."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
# [END greeting]


class MainPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('Guestbook.html')
        self.response.write(template.render(template_values))

class Guestbook(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each Greeting
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/guestbook?' + urllib.urlencode(query_params))


#Module1 MemberOne Module

DEFAULT_MEMBERONE_NAME = 'memberone_comments'

def memberone_key(memberone_page=DEFAULT_MEMBERONE_NAME):
    """Constructs a Datastore key for a Comment entity with memberone_page."""
    return ndb.Key('MemberOnePageComment', memberone_page)

class Comment(ndb.Model): #this is a comment
    """Models an individual Comment entry with author, content, and date."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class MemberOnePage(webapp2.RequestHandler):

    def get(self):

        memberone_page =self.request.get('memberone_page',DEFAULT_MEMBERONE_NAME)
        comments_query = Comment.query(
            ancestor=memberone_key(memberone_page)).order(-Comment.date)
        comments = comments_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'comments': comments,
            'memberone_page': urllib.quote_plus(memberone_page),
            'url': url,
            'url_linktext': url_linktext,
        }
        template = JINJA_ENVIRONMENT.get_template('MemberOnePage.html')
        self.response.write(template.render(template_values))

class MemberOnePageComment(webapp2.RequestHandler):

    def post(self):

        memberone_page = self.request.get('memberone_page',DEFAULT_MEMBERONE_NAME)
        comment = Comment(parent=memberone_key(memberone_page))

        if users.get_current_user():
            comment.author = users.get_current_user()

        comment.content = self.request.get('content')
        comment.put()

        query_params = {'memberone_page': memberone_page}
        self.redirect('/module-1/1?' + urllib.urlencode(query_params))

# Member Two Module 1

DEFAULT_MEMBERTWO_NAME = 'membertwo_comments'

def membertwo_key(membertwo_page=DEFAULT_MEMBERTWO_NAME):
    """Constructs a Datastore key for a Comment entity with membertwo_page."""
    return ndb.Key('MemberTwoPageComment', membertwo_page)

class MemberTwoPage(webapp2.RequestHandler):
    
    def get(self):

        membertwo_page =self.request.get('membertwo_page',DEFAULT_MEMBERTWO_NAME)
        comments_query = Comment.query(
            ancestor=membertwo_key(membertwo_page)).order(-Comment.date)
        comments = comments_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'comments': comments,
            'membertwo_page': urllib.quote_plus(membertwo_page),
            'url': url,
            'url_linktext': url_linktext,
        }
        template = JINJA_ENVIRONMENT.get_template('MemberTwoPage.html')
        self.response.write(template.render(template_values))

class MemberTwoPageComment(webapp2.RequestHandler):

    def post(self):

        membertwo_page = self.request.get('membertwo_page',DEFAULT_MEMBERTWO_NAME)
        comment = Comment(parent=membertwo_key(membertwo_page))

        if users.get_current_user():
            comment.author = users.get_current_user()

        comment.content = self.request.get('content')
        comment.put()

        query_params = {'membertwo_page': membertwo_page}
        self.redirect('/module-1/2?' + urllib.urlencode(query_params))

# Student Module

class Student(ndb.Model):
    """Models an individual Guestbook entry with FirstName, LastName, EmailAddress and StudentNumber."""
    FirstName = ndb.StringProperty(indexed=False)
    LastName = ndb.StringProperty(indexed=False)
    EmailAddress = ndb.StringProperty(indexed=False)
    StudentNumber = ndb.StringProperty(indexed=False)
    Department = ndb.StringProperty(indexed=False)
    StudentStatus = ndb.StringProperty(indexed=False)

class StudentMainPage(webapp2.RequestHandler):
    def get(self):	
  
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
        }    
                    
        template = JINJA_ENVIRONMENT.get_template('StudentMainPage.html')
        self.response.write(template.render(template_values))

class StudentNewHandler(webapp2.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
        } 

        template = JINJA_ENVIRONMENT.get_template('StudentNew.html')
        self.response.write(template.render(template_values))

    def post(self):

    	student = Student()
        student.FirstName = self.request.get('FirstName')
        student.LastName = self.request.get('LastName')
        student.EmailAddress = self.request.get('EmailAddress')
        student.StudentNumber = self.request.get('StudentNumber')
        student.Department = self.request.get('Department')
        student.StudentStatus = self.request.get('StudentStatus')        
        student.put()
        self.redirect('/student/success')

class SuccessPageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('StudentSuccess.html')
        self.response.write(template.render())

class StudentList(webapp2.RequestHandler):
    def get(self):

        student = Student.query().fetch();
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
        	'student': student,            
        } 

        template = JINJA_ENVIRONMENT.get_template('StudentList.html')
        self.response.write(template.render(template_values))

class StudentView(webapp2.RequestHandler):
    def get(self, thesid):

        student = Student.query().fetch();

        template_values = {
        'student': student,
        'id'    : int(thesid)
        }

        template = JINJA_ENVIRONMENT.get_template('StudentView.html')
        self.response.write(template.render(template_values))

class StudentEditHandler(webapp2.RequestHandler):
    def get(self,thes_id):
       
        student = Student.query().fetch();

        template_values = {
        'student': student,
        'id'    : int(thes_id)
        }

        template = JINJA_ENVIRONMENT.get_template('StudentEdit.html')
        self.response.write(template.render(template_values))
 
 
    def post(self, thes_id):
        student_id = int(thes_id)
        student = Student.get_by_id(student_id)
        student.FirstName = self.request.get('FirstName')
        student.LastName = self.request.get('LastName')
        student.EmailAddress = self.request.get('EmailAddress')
        student.StudentNumber = self.request.get('StudentNumber')
        student.Department = self.request.get('Department')
        student.StudentStatus = self.request.get('StudentStatus')        
        student.put()
        self.redirect('/student/success')


# Adviser Module

class Adviser(ndb.Model):
    """Models an individual Guestbook entry with FirstName, LastName, EmailAddress and StudentNumber."""
    Department = ndb.StringProperty(indexed=False)
    TitleName = ndb.StringProperty(indexed=False)
    FirstName = ndb.StringProperty(indexed=False)
    LastName = ndb.StringProperty(indexed=False)
    EmailAddress = ndb.StringProperty(indexed=False)
    PhoneNumber = ndb.StringProperty(indexed=False)

class AdviserNew(webapp2.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
        } 

        template = JINJA_ENVIRONMENT.get_template('AdviserCreate.html')
        self.response.write(template.render(template_values))

    def post(self):

    	adviser = Adviser()
        adviser.Department = self.request.get('Department')
        adviser.TitleName = self.request.get('TitleName')
        adviser.FirstName = self.request.get('FirstName')
        adviser.LastName = self.request.get('LastName')
        adviser.EmailAddress = self.request.get('EmailAddress')
        adviser.PhoneNumber = self.request.get('PhoneNumber')
        adviser.put()
        self.redirect('/adviser/success')

class AdviserMainPage(webapp2.RequestHandler):
    def get(self):	

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
        }

        template = JINJA_ENVIRONMENT.get_template('AdviserMainPage.html')
        self.response.write(template.render(template_values))

class AdviserSuccess(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('AdviserSuccess.html')
        self.response.write(template.render())

    def post(self):

    	adviser = Adviser()
        adviser.Department = self.request.get('Department')
        adviser.TitleName = self.request.get('TitleName')
        adviser.FirstName = self.request.get('FirstName')
        adviser.LastName = self.request.get('LastName')
        adviser.EmailAddress = self.request.get('EmailAddress')
        adviser.PhoneNumber = self.request.get('PhoneNumber')
        adviser.put()
        self.redirect('/adviser/success')

class AdviserList(webapp2.RequestHandler):
    def get(self):

        adviser = Adviser.query().fetch();
       
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
	        'adviser': adviser,
        }

        template = JINJA_ENVIRONMENT.get_template('AdviserList.html')
        self.response.write(template.render(template_values))

class AdviserView(webapp2.RequestHandler):
    def get(self, thesid):

        adviser = Adviser.query().fetch();

        template_values = {
        'adviser': adviser,
        'id'    : int(thesid)
        }

        template = JINJA_ENVIRONMENT.get_template('AdviserView.html')
        self.response.write(template.render(template_values))

class AdviserEditHandler(webapp2.RequestHandler):
    def get(self, thesid):

        adviser = Adviser.query().fetch();

        template_values = {
        'adviser': adviser,
        'id'    : int(thesid)
        }

 
        template = JINJA_ENVIRONMENT.get_template('AdviserEdit.html')
        self.response.write(template.render(template_values))
 
 
    def post(self, thes_id):
        thes_id = int(thes_id)
        adviser = Adviser.get_by_id(thes_id)
        adviser.Department = self.request.get('Department')
        adviser.TitleName = self.request.get('TitleName')
        adviser.FirstName = self.request.get('FirstName')
        adviser.LastName = self.request.get('LastName')
        adviser.EmailAddress = self.request.get('EmailAddress')
        adviser.PhoneNumber = self.request.get('PhoneNumber')
        adviser.put()
        self.redirect('/adviser/success')

# Thesis Management Module

class Thesis(ndb.Model):
    """Models an individual Guestbook entry with FirstName, LastName, EmailAddress and StudentNumber."""
    TitleName = ndb.StringProperty(indexed=False)
    Description = ndb.StringProperty(indexed=False)
    SchoolYear = ndb.StringProperty(indexed=False)
    Status = ndb.StringProperty(indexed=False)


class ThesisNew(webapp2.RequestHandler):
    def get(self):

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
        } 

        template = JINJA_ENVIRONMENT.get_template('ThesisCreate.html')
        self.response.write(template.render(template_values))

    def post(self):

    	thesis = Thesis()
        thesis.TitleName = self.request.get('TitleName')
        thesis.Description = self.request.get('Description')
        thesis.SchoolYear = self.request.get('SchoolYear')
        thesis.Status = self.request.get('Status')
        thesis.put()
        self.redirect('/thesis/success')

class ThesisMainPage(webapp2.RequestHandler):
    def get(self):	
      
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
        }    

        template = JINJA_ENVIRONMENT.get_template('ThesisMainPage.html')
        self.response.write(template.render(template_values))

class ThesisSuccess(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('ThesisSuccess.html')
        self.response.write(template.render())

    def post(self):

    	thesis = Thesis()
        thesis.TitleName = self.request.get('TitleName')
        thesis.Description = self.request.get('Description')
        thesis.SchoolYear = self.request.get('SchoolYear')
        thesis.Status = self.request.get('Status')
        thesis.put()
        self.redirect('/thesis/success')

class ThesisList(webapp2.RequestHandler):
    def get(self):

        thesis = Thesis.query().fetch();

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)

        else:
            url = users.create_login_url(self.request.uri)
  
        template_values = {
            'url': url,
            'user': users.get_current_user(),
	        'thesis': thesis,
        }

        template = JINJA_ENVIRONMENT.get_template('ThesisList.html')
        self.response.write(template.render(template_values))

class ThesisView(webapp2.RequestHandler):
    def get(self, thesid):

        thesis = Thesis.query().fetch();

        template_values = {
        'thesis': thesis,
        'id'    : int(thesid)
        }

        template = JINJA_ENVIRONMENT.get_template('ThesisView.html')
        self.response.write(template.render(template_values))


class ThesisEditHandler(webapp2.RequestHandler):
    def get(self,thesis_id):
       
        thesisquery = Thesis.query().fetch()
        thesis_id = int(thesis_id)
 
        values = {
            'thesisquery': thesisquery,
            'id': thesis_id
        }
 
        template = JINJA_ENVIRONMENT.get_template('ThesisEdit.html')
        self.response.write(template.render(values))
 
 
    def post(self, thesis_id):
        thesis_id = int(thesis_id)
        thesis = Thesis.get_by_id(thesis_id)
        thesis.TitleName = self.request.get('TitleName')
        thesis.Description = self.request.get('Description')
        thesis.SchoolYear = self.request.get('SchoolYear')
        thesis.Status = self.request.get('Status')
        thesis.put()
        self.redirect('/thesis/success')

#Module Number Three Added Codes

class SignIn(webapp2.RequestHandler):
    def get(self):
        # Checks for active Google account session
 
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
            url_linkname = ':)'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Sign In'
            url_linkname = ':('
    
        template_values = {
            'url': url,
            'user': users.get_current_user(),
            'url_linktext': url_linktext,
            'url_linkname': url_linkname,
        }

        template = JINJA_ENVIRONMENT.get_template('MThreeMain.html')
        self.response.write(template.render(template_values))
 
application = webapp2.WSGIApplication([
	#ModuleThree
    ('/', SignIn),
    #Guestbook
    ('/guestbook',MainPage),
    ('/sign', Guestbook),
    #Module1
    ('/module-1/1',MemberOnePage),
    ('/module-1/1/sign',MemberOnePageComment),
    ('/module-1/2',MemberTwoPage),
    ('/module-1/2/sign',MemberTwoPageComment),
    #Student
    ('/student/new',StudentMainPage),
    ('/student/create',StudentNewHandler),
    ('/student/success',SuccessPageHandler),
    ('/student/list',StudentList),
    ('/student/view/(\d+)',StudentView),
   	('/student/edit/(\d+)', StudentEditHandler), 
    #Adviser
    ('/adviser/create',AdviserNew),
    ('/adviser/new',AdviserMainPage),
    ('/adviser/success',AdviserSuccess),
    ('/adviser/list',AdviserList),
    ('/adviser/view/(\d+)',AdviserView), 
    ('/adviser/edit/(\d+)', AdviserEditHandler),
    #Thesis    
    ('/thesis/create',ThesisNew),
    ('/thesis/new',ThesisMainPage),
    ('/thesis/success',ThesisSuccess),
    ('/thesis/list',ThesisList),
    ('/thesis/view/(\d+)',ThesisView),
    ('/thesis/edit/(\d+)', ThesisEditHandler),

], debug=True)