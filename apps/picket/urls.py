"""
Copyright 2008 Serge Matveenko

This file is part of Picket.

Picket is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Picket is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Picket.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.conf.urls.defaults  import *

"""
TODO: project view with project summary not administration
"""
urlpatterns = patterns('apps.picket.views',
    (r'^$', 'index', {},
        'picket-index',),
    (r'^filebug/$', 'filebug', {},
        'picket-filebug',),
    (r'^bugs/$', 'bugs', {},
        'picket-bugs',),
    (r'^project(?P<project_id>\d+)/$', 'project', {},
        'picket-project',),
    (r'^bugs/c(?P<category_id>\d+)/$', 'bugs', {},
        'picket-category',),
    (r'^bug/(?P<bug_id>\d+)/$', 'bug', {},
        'picket-bug',),
    (r'^p\d+/c\d+/b(?P<bug_id>\d+)/annotate/$', 'annotate', {},
        'picket-annotate',),
    (r'^choose_project/next/(?P<view_name>[\w-]+)/$', 'choose_project', {},
        'picket-choose-project-gonext'),
    (r'^choose_project/$', 'choose_project', {},
        'picket-choose-project'),
    (r'^set_project/next/(?P<view_name>[\w-]+)/$', 'set_project', {},
        'picket-set-project-gonext'),
    (r'^set_project/$', 'set_project', {},
        'picket-set-project'),
    (r'^jump/$', 'jump_to_bug', {},
        'picket-jump-to-bug'),
    (r'^my/$', 'my', {},
        'picket-my-view',),
    (r'^changelog/$', 'changelog', {},
        'picket-changelog'),
    (r'^roadmap/$', 'roadmap', {},
        'picket-roadmap'),
    
    ## picket administration
    (r'^admin/', include('apps.picket.admin.urls')),
)