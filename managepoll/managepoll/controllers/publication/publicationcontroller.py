# -*- coding: utf-8 -*-
from tg import TGController 
from tg import expose, flash, require, url, lurl,validate 
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from tg.predicates import has_any_permission

from managepoll import model 
from managepoll.model import DBSession

from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from tgext.pyutilservice import Utility
import sys
from datetime import date,datetime



class PublicationController(TGController):
    
    allow_only = has_any_permission('manage','creator',
                                msg=l_('Only for people with the "manage" permission'))
     
    def __init__(self):
        self.utility = Utility()
    
    
    @expose('managepoll.templates.publication.index')   
    def index(self,**kw):
        print kw
        return dict(page = 'index',idproject = kw['idproject'] )
    
    
    @expose()
    def deletepublication(self,**kw): 
        print kw
        
        status, message = model.QuestionOption.deleteById(kw['idoption'])
        
        print status
        print message

        redirect('/managepoll/publication/index',params={'idproject':kw['idproject']})
    
    @expose('managepoll.templates.publication.publication')
    def publication(self,**kw):
        
        
        reload(sys).setdefaultencoding('utf8')      #set ค่า เป็น utf8 สำหรับฟังชั่นนี้
        user =  request.identity['user'];    

        
        questionoption = model.QuestionOption()
        questionoption.id_question_project = kw['idproject']
        
        questionoption.activate_date = datetime.today() #today for add option
        questionoption.expire_date = self.utility.plusDate(datetime.today(),30) #plusDate30day for add option
       
        emailtemplate = model.Invitation()
        randomtype = model.RandomType()
        closetype = model.CloseType()
        questionthem = model.QuestionTheme()
        
        if('idoption' in kw):
            print "Edit option"
            questionoption = model.QuestionOption.getId(kw['idoption'])
            
        questionthem = model.QuestionTheme.getAll(act = 1)    
        closetype = model.CloseType.getAll(active = 1)
        randomtype = model.RandomType.getAll(active = 1)
        emailtemplate, total = model.Invitation.getByUser(user.user_id)
        
        return dict(page='publication',
                    questionoption = questionoption,
                    emailtemplate = emailtemplate, 
                    randomtype=randomtype, 
                    closetype=closetype, 
                    questionthem=questionthem,
                    idproject = kw['idproject']
                     )
 
    @expose()
    def savepublication(self,**kw):
        print kw
        reload(sys).setdefaultencoding('utf8')    
          
        questionoption = model.QuestionOption(**kw)
         
        print questionoption.show_navigator  
        print questionoption.show_score 
        print questionoption.random_answer
        
        questionoption.activate_date = self.utility.startDate(questionoption.activate_date)
        questionoption.expire_date = self.utility.finishDate(questionoption.expire_date)
        questionoption.show_score = self.utility.convertToBit(questionoption.show_score)  
        questionoption.show_navigator = self.utility.convertToBit(questionoption.show_navigator)  
        questionoption.id_question_option = self.utility.setIfEmpty(questionoption.id_question_option)
        questionoption.random_answer = self.utility.convertToBit(questionoption.random_answer)
  
        print "show_navigator : %s" %questionoption.show_navigator  
        print "show_score : %s" %questionoption.show_score 
        print "random_answer : %s" %questionoption.random_answer
        
        if self.utility.isEmpty(questionoption.id_question_option) : 
            questionoption.save()
        else :
            questionoption.updateall()
       
        redirect('/managepoll/publication/index',params={'idproject':questionoption.id_question_project})
        
    

    