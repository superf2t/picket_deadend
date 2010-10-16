"""
Copyright 2010 Serge Matveenko

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

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from mongoengine import URLField

from documents import Scope, Project, Category, Group


def choices(queryset):
    """
    @todo: DocumentChoiceField, DocumentMultipleChoiceField
    """
    return [(None, '',)] + map(lambda item: (item.id, item.name,), queryset)


class ProjectForm(forms.Form):
    name = forms.CharField()
    status = forms.CharField(required=False)
    enabled = forms.BooleanField(required=False, initial=True)
    scope = forms.ChoiceField(choices=choices(Scope.sort))
    url = forms.RegexField(required=False, regex=URLField.URL_REGEX)
    description = forms.CharField(required=False)
    parent = forms.ChoiceField(required=False, choices=choices(Project.sort))
    categories = forms.MultipleChoiceField(required=False,
        choices=choices(Category.sort))
    """ @todo: attachments handling """


class ScopeForm(forms.Form):
    name = forms.CharField()
    read_access = forms.MultipleChoiceField(required=False,
        choices=choices(Group.sort))
    write_access = forms.MultipleChoiceField(required=False,
        choices=choices(Group.sort))
    anonymous_access = forms.BooleanField(required=False, initial=False)


class AuthForm(AuthenticationForm):
    i_am_auth_form = forms.BooleanField(initial=True, widget=forms.HiddenInput)
