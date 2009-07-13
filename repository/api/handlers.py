from piston.handler import AnonymousBaseHandler
from piston.handler import BaseHandler
from emitters import *
from django.http import Http404

import os
import os.path
import sys
sys.path.append('..')
from repository.winrepo.models import *

class AnonymousPackageHandler(AnonymousBaseHandler):
    model = Package
    fields = ('name', 'version', 'architecture', 'filename', 'short_description', 'long_description', 'creator', 'creator_email', 'publisher', 'publisher_email', 'maintainer', 'maintainer_email', 'rights_holder', 'rights_holder_email', 'release_date', 'changes', 'size', 'license', 'sha256', 'homepage', 'installed_size', 
('languages', ('language', ), ),
('section', ('title', ), ),
('supported', ('os_version', ), ),
('depends', ('name', 'version', ), ), 
('provides', ('name', 'version', ), ), 
('suggests', ('name', 'version', ), ),  
('replaces', ('name', 'version', ), ),
('pre_depends', ('name', 'version', ), ),
('recommends', ('name', 'version', ), ),
('conflicts', ('name', 'version', ), )
# Languages and supported are not yet implemented
)
#   allow_methods = {'GET',}


class PackageHandler(BaseHandler):
    anonymous = AnonymousPackageHandler
    model = Package
    fields = ('name', 'version', 'architecture', 'filename', 'short_description', 'long_description', 'creator', 'creator_email', 'publisher', 'publisher_email', 'maintainer', 'maintainer_email', 'rights_holder', 'rights_holder_email', 'release_date', 'changes', 'size', 'license', 'sha256', 'homepage', 'installed_size', 
('languages', ('language', ), ),
('section', ('title', ), ),
('supported', ('os_version', ), ),
('depends', ('name', 'version', ), ), 
('provides', ('name', 'version', ), ), 
('suggests', ('name', 'version', ), ),  
('replaces', ('name', 'version', ), ),
('pre_depends', ('name', 'version', ), ),
('recommends', ('name', 'version', ), ),
('conflicts', ('name', 'version', ), )
# Languages and supported are not yet implemented
)
#   allow_methods = {'GET',}


class PackageHandler(BaseHandler):
    anonymous = AnonymousPackageHandler
    model = Package
    fields = ('name', 'version', 'architecture', 'filename', 'short_description', 'long_description', 'creator', 'creator_email', 'publisher', 'publisher_email', 'maintainer', 'maintainer_email', 'rights_holder', 'rights_holder_email', 'release_date', 'changes', 'size', 'license', 'sha256', 'homepage', 'installed_size',  
('languages', ('language', ), ),
('section', ('title', ), ),
('supported', ('os_version', ), ),
('depends', ('name', 'version', ), ), 
('provides', ('name', 'version', ), ), 
('suggests', ('name', 'version', ), ),  
('replaces', ('name', 'version', ), ),
('pre_depends', ('name', 'version', ), ),
('recommends', ('name', 'version', ), ),
('conflicts', ('name', 'version', ), )
# Languages and supported are not yet implemented
)
#   allow_methods = {'GET',}

    def read(self, request, name=None, version=None, id=None, generalquery=None):
        base = Package.objects

        if name and version:
            try:
                return base.get(name=name, version=version)
            except:
                return None #This should be modified by a default error message

class AnonymousPackagesHandler(AnonymousBaseHandler):
    model = Package
    fields = ('name', 'version', 'architecture', 'filename', 'short_description', 'long_description', 'creator', 'creator_email', 'publisher', 'publisher_email', 'maintainer', 'maintainer_email', 'rights_holder', 'rights_holder_email', 'release_date', 'changes', 'size', 'license', 'sha256', 'homepage', 'installed_size',  
('languages', ('language', ), ),
('section', ('title', ), ),
('supported', ('os_version', ), ),
('depends', ('name', 'version', ), ), 
('provides', ('name', 'version', ), ), 
('suggests', ('name', 'version', ), ),  
('replaces', ('name', 'version', ), ),
('pre_depends', ('name', 'version', ), ),
('recommends', ('name', 'version', ), ),
('conflicts', ('name', 'version', ), )
# Languages and supported are not yet implemented
)
#   allow_methods = {'GET',}


class PackagesHandler(BaseHandler):
    model = Package
    anonymous = AnonymousPackagesHandler
    fields = ('name', 'version', 'architecture', 'filename', 'short_description', 'long_description', 'creator', 'creator_email', 'publisher', 'publisher_email', 'maintainer', 'maintainer_email', 'rights_holder', 'rights_holder_email', 'release_date', 'changes', 'size', 'license', 'sha256', 'homepage', 'installed_size',  
('languages', ('language', ), ),
('section', ('title', ), ),
('supported', ('os_version', ), ),
('depends', ('name', 'version', ), ), 
('provides', ('name', 'version', ), ), 
('suggests', ('name', 'version', ), ),  
('replaces', ('name', 'version', ), ),
('pre_depends', ('name', 'version', ), ),
('recommends', ('name', 'version', ), ),
('conflicts', ('name', 'version', ), )
# Languages and supported are not yet implemented
)
#   allow_methods = {'GET',}
    
    def read(self, request, date=None):
        base = Package.objects

        if date:
            list_date = date.split('-')
            date = {'day':int(list_date[0]), 'month': int(list_date[1]), 'year': int(list_date[2])}
            try:
                return base.filter(release_date__gte=(datetime.date(date['year'], date['month'],  date['day'])))
            except:
                return None
        else:
            try:
                return base.all()
            except:
                return None
