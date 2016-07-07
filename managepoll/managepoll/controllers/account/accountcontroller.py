# -*- coding: utf-8 -*-
from tg import TGController 
from tg import expose, flash, require, url, lurl,validate 
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from tg.predicates import has_any_permission, in_any_group


from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from tgext.pyutilservice import Utility
import sys
from datetime import datetime ;


# import tw2.core
# import logging;
# from surveymodel.authuser import UserSocialNetwork
# from tgext.sendmailservice import SendMailService
# from pollandsurvey.controllers.service import RegisterService
# from surveyobject.languageobject import LanguageObject


# log = logging.getLogger(__name__);
# from tgext.pylogservice import LogDBHandler;
# __all__ = ['AccountController']

class AccountController(TGController):
    
    allow_only = in_any_group('voter', 'managers', msg=l_('Only for people with the "manage" permission'))   
    
    def __init__(self, models, session, config_type=None, translations=None):
        self.utility = Utility()
        self.model = models   
        
#         
#         self.registerService = RegisterService();
#         dh = LogDBHandler( config=config,request=request);        
#         log.addHandler(dh)
        
#         self.__getMasterData()   
#         
#     def __getMasterData(self):
#         self.serviceType = self.model.SocialType.getAll(1)     

    @expose('managepoll.templates.account.index')
    def index(self,**kw):
        user =  request.identity['user'];
        print user.user_id
                
        userService = self.model.UserService();
        if request.identity:
            user =  request.identity['user'];
            userService = self.model.UserService.getById(user.user_id);            
            if userService is None:
                userService= self.model.UserService();         
        
        listConutry = [];
        self.country = self.model.FixCountry.getAll("1");
        for lang in self.country:
            listConutry.append( lang.to_json());
        
        listGender = self.model.Gender.getAll(1)
        listLanguage = [];
        
        self.language = self.model.FixLanguage.getAll("1");
        for lang in self.language:
            listLanguage.append( lang.to_json());
            
        return dict(page='index', 
                    userService = userService, 
                    listConutry = listConutry, 
                    listGender = listGender, 
                    listLanguage = listLanguage, 
                    idproject = None)
    
       
    @expose('managepoll.templates.account.changepassword')    
    def changepass(self, *args, **kw):
        """Handle the front-page."""
        return dict(page='changepassword')
    
    @expose('managepoll.templates.account.socialmedia')    
    def socialmedia(self, *args, **kw):
        
        return dict(page='socialmedia')
    
    @expose('managepoll.templates.account.cancellation')  
    def cancellation(self, *args, **kw):
        """Handle the front-page."""
        return dict(page='cancellation')
    
    
    