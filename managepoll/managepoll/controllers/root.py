# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController 
from tg import expose, flash, require, url, lurl,validate 
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates


from managepoll import model 
from managepoll.model import DBSession

from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from tgext.pyutilservice import Utility
import sys
from datetime import date,datetime
#from surveyobject.voterobject import VoterObject
from .script import LoadDataControllers
from .project import SurveyController
from .invitation import InvitationController
from .publication import PublicationController
from .voter import VoterController


class RootController(TGController):
    

   
    
    def __init__(self):
        
        
        self.utility = Utility()
        
        self.project = SurveyController()
        self.invitation = InvitationController()
        self.publication = PublicationController()
        
        self.script = LoadDataControllers()
    
    
        print "call RootController(managepoll)"
        self.lang = model.Languages.getAll()
        self.voter = VoterController(model, DBSession, config_type=TGAdminConfig)
        
    
    @expose('managepoll.templates.index')
    def index(self):
        flash(_("Hello World!"))
        return dict(page ='index',idproject = None)
    
    
    
    
    
 
    
    
 
    