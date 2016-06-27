# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController 
from tg import expose, flash, require, url, lurl,validate 
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from tg.predicates import has_any_permission, in_any_group

from managepoll import model 





from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from tgext.pyutilservice import Utility
import sys
from datetime import date,datetime
#from surveyobject.voterobject import VoterObject
from .script import LoadDataControllers

from .project import ProjectController
from .invitation import InvitationController
from .publication import PublicationController
from .voter import VoterController


class RootController(TGController):
    

    allow_only = in_any_group('voter', 'managers', msg=l_('Only for people with the "manage" permission'))
    
    invitation = InvitationController(model, model.DBSession, config_type=TGAdminConfig)
    
    voter = VoterController(model, model.DBSession, config_type=TGAdminConfig)
    
    publication = PublicationController(model, model.DBSession, config_type=TGAdminConfig)
    project = ProjectController(model, model.DBSession, config_type=TGAdminConfig)
    script = LoadDataControllers(model, model.DBSession, config_type=TGAdminConfig)
    
    
    def __init__(self):
        
        
        self.utility = Utility()
        
        
        
        
    
    @expose('managepoll.templates.index')
    def index(self):
        flash(_("Hello World!"))
        return dict(page ='index',idproject = None)
    
    
    
    
    
 
    
    
 
    