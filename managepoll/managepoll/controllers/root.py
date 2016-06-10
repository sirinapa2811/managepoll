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



class RootController(TGController):
    def __init__(self):
        self.utility = Utility()
    
   
    @expose('managepoll.templates.index')
    def index(self):
        flash(_("Hello World!"))
        return dict(page ='index')
    
    @require(predicates.in_any_group('creator','managers', msg=l_('Only for creator')))
    @expose('managepoll.templates.surfvey')
    def surfvey(self,**kw):
               
        p = model.QuestionProjectType.getAll(act = 1)
        return dict(page ='surfvey',projecttype = p)
    
   
    @expose('json')
    def getdataproject(self,**kw):
        print kw
        
        user =  request.identity['user'];        
        values,total = model.QuestionProject.getAllByUser(userid=user.user_id,page=int(kw['current']), page_size=int(kw['rowCount']))
        
        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = values)
    
    @expose('managepoll.templates.managesurfvey')
    def managesurfvey(self,**kw):
        print '......................'
        print kw
        
        questionproject = model.QuestionProject()
        
        if('idproject' in kw):
            print kw['idproject']
            questionproject = model.QuestionProject.getId(kw['idproject'])
        else :
            print "don't have kw"    
        #g = model.QuestionProjectType.getAll(act = 1)
        questionType = model.QuestionType.getAll(act = 1)
        return dict(page ='managesurfvey', questionproject = questionproject,questionType = questionType)
    
    @expose('managepoll.templates.invitation')
    def invitation(self,**kw):
        questionproject = model.QuestionProject.getId(kw['idproject'])
        print kw 
        
        
        reload(sys).setdefaultencoding("utf-8");
        invitation = model.Invitation()
        self.emailtemplate = model.EmailTemplate()
        if('idinvitation' in kw):
            print kw['idinvitation']            
            #           
            invitation = model.Invitation.getId(kw['idinvitation'])  
            
            
        else:
            self.emailtemplate = model.EmailTemplate.getTemplateBy(5); 
            
            invitation.name_content  = self.emailtemplate.sender
            invitation.from_name =  self.emailtemplate.sender
            invitation.subject =  self.emailtemplate.subject
            invitation.content =  self.emailtemplate.content_template
         
        return dict(page='invitation', invitation = invitation, questionproject=questionproject)
    
    @expose('managepoll.templates.invitationlist')
    def invitationlist(self,**kw):
        if('idproject' in kw):
            questionproject = model.QuestionProject.getId(kw['idproject'])
            
            
        return dict(page = 'invitationlist',questionproject = questionproject)
        

    @expose('json')
    def getdatainvittation(self,**kw):
        print "****************"
        print kw 
       
        values,total = model.Invitation.getByidProject(idProject=kw['id'],page=int(int(kw['current'])-1), page_size=int(kw['rowCount']))

        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = values)
        
    @expose()
    def saveinvitation(self,**kw):
        reload(sys).setdefaultencoding('utf8') 
        
        o = model.Invitation(**kw)
        
        o.id_question_invitation = self.utility.setIfEmpty(o.id_question_invitation)
        
        print o.name_content
        print o.subject
        print o.from_name
        print o.content
   
        
        if self.utility.isEmpty(o.id_question_invitation) : 
            o.save()
        else :
            o.updateall()
      
        #o.save()

        redirect('/managepoll/invitationlist',params={'idproject':o.id_question_project})
    
        
    
    @expose('managepoll.templates.publicationlist')   
    def publicationlist(self,**kw):
        return dict(page = 'publicationlis',idproject = kw['idproject'] )
    
    @expose()
    def deletepublication(self,**kw): 
        print kw
        
        status, message = model.QuestionOption.deleteById(kw['idoption'])
        
        print status
        print message

        redirect('/managepoll/publicationlist',params={'idproject':kw['idproject']})
    
    @expose('managepoll.templates.publication')
    def publication(self,**kw):
        
        reload(sys).setdefaultencoding('utf8')      #set ค่า เป็น utf8 สำหรับฟังชั่นนี้
        
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
        emailtemplate, total = model.Invitation.getByidProject(kw['idproject'])
        
        return dict(page='publication',
                    questionoption = questionoption,
                    emailtemplate = emailtemplate, 
                    randomtype=randomtype, 
                    closetype=closetype, 
                    questionthem=questionthem)
 
    @expose()
    def savepublication(self,**kw):
        print kw
        reload(sys).setdefaultencoding('utf8')    
          
        o = model.QuestionOption(**kw)
         
        print o.show_navigator  
        print o.show_score 
        print o.random_answer
        
        o.activate_date = self.utility.startDate(o.activate_date)
        o.expire_date = self.utility.finishDate(o.expire_date)
        o.show_score = self.utility.convertToBit(o.show_score)  
        o.show_navigator = self.utility.convertToBit(o.show_navigator)  
        o.id_question_option = self.utility.setIfEmpty(o.id_question_option)
        o.random_answer = self.utility.convertToBit(o.random_answer)
  
        print "show_navigator : %s" %o.show_navigator  
        print "show_score : %s" %o.show_score 
        print "random_answer : %s" %o.random_answer
        
        if self.utility.isEmpty(o.id_question_option) : 
            o.save()
        else :
            o.updateall()
       
        redirect('/managepoll/publicationlist',params={'idproject':o.id_question_project})
        
    @expose('json')
    def getdatapublication(self,**kw):   
        values,total = model.QuestionOption.getByProject(idProject=kw['id'],page=(int(kw['current'])-1), page_size=int(kw['rowCount']))        
        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = values)
    

    @expose()
    def deletesurfvey(self,**kw):
        print 'Delete : Project ID :', kw['idproject']
        model.QuestionProject.deleteById(kw['idproject'])
        redirect('/surfvey')
        
    @expose()
    def savesurfver(self,**kw):
        user =  request.identity['user'];
        values = model.QuestionProject.getAllByUser(userid=user.user_id)
     
       
        print user.user_id #user_id --login
      
        s = model.QuestionProject()
        
        s.name = kw['p_name']
        s.description  = kw['p_description']
        s.id_question_project_type = kw['p_type']
        s.user_id = user.user_id
        s.save()
      
        #model.DBSession.add(s)
  
        redirect('/managepoll/surfvey')
    