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

from tgext.pyutilservice import Utility
import sys
from datetime import date,datetime



class RootController(TGController):
    @expose('managepoll.templates.index')
    def index(self):
        flash(_("Hello World!"))
        pass
    
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
        reload(sys).setdefaultencoding("utf-8");
        if('idproject' in kw):
            print kw['idproject']
            questionproject = model.QuestionProject.getId(kw['idproject'])
            self.emailtemplate = model.EmailTemplate.getTemplateBy(5);
        #print kw    
        return dict(page='invitation',questionproject = questionproject,emailtemplate = self.emailtemplate)
    
    @expose('managepoll.templates.invitationlist')
    def invitationlist(self,**kw):
        if('idproject' in kw):
            questionproject = model.QuestionProject.getId(kw['idproject'])
        return dict(page = 'invitationlist',questionproject = questionproject)
        

    @expose('json')
    def getdatainvittation(self,**kw):
        print "****************"
        print kw 
       
        values,total = model.Invitation.getByidProject(idProject=kw['id'],page=int(kw['current']), page_size=int(kw['rowCount']))
        return dict(current= kw['current'] ,rowCount= kw['rowCount'],total=total,rows = values)
        
    @expose()
    def saveinvitation(self,**kw):
        print kw
        o = model.Invitation(**kw)
        o.save()
        redirect('/managepoll/surfvey')
        
    
    @expose('mytemplate.templates.publicationlist')   
    def publicationlist(self,**kw):
        return dict(page = 'publicationlis',idproject = kw['idproject'] )
    
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
    