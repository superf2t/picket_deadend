"""
Copyright 2008-2010 Serge Matveenko

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

from django.conf.urls.defaults import *


urlpatterns = patterns('%s.views' % __package__,
    (r'^admin/', include('%s.admin.urls' % __package__)),
    (r'^$', 'index', {}, 'picket-index'),
    (r'^new/$', 'new_bug', {}, 'picket-bugs-new'),
    (r'^(?P<bug_id>\d+)/$', 'bug', {}, 'picket-bug'),
)
