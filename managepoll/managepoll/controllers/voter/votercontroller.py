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
from datetime import date,datetime
from surveyobject import *


class VoterController(TGController):
    
    allow_only = in_any_group('voter', 'managers', msg=l_('Only for people with the "manage" permission'))
    #has_any_permission('manage','creator', msg=l_('Only for people with the "manage" permission'))
    
    def __init__(self, models, session, config_type=None, translations=None):
        print "call VoterController(managepoll)"
        
        self.utility = Utility()           
        self.model = models       
        
        
    @expose('managepoll.templates.voter.index')
    def index(self):    
        return dict(page = 'index',idproject=None)
    
    
    @expose('managepoll.templates.voter.voter')
    def voters(self,*args,**kw):
        reload(sys).setdefaultencoding('utf8')   
        
        voterObject = VoterObject()        
        print kw
        
        if('idvoter' in kw):
            print kw
            print "Edit voter"
            voter = self.model.Voter.getId(kw['idvoter'])
            voterObject.setVoter(voter)
            #employment = model.EmploymentDetail.getId(kw['idvoter'])
            
        print "voters : lang"
        
        self.lang = self.model.Languages.getAll()
        print self.lang
        self.marriageStatus = self.model.MarriageStatus.getAll(act=1)
        self.gender = self.model.Gender.getAll(act=1)
        self.tel = self.model.TelephoneType.getAll(act=1)
        self.religion = self.model.ReligionType.getAll(act=1)
        self.national = self.model.NationalityType.getAll(act=1)
        self.race = self.model.RaceType.getAll(act=1)
        self.condition = self.model.LivingConditionType.getAll(act=1)
        self.employmentstatus = self.model.EmploymentType.getAll(act=1)
        self.listConutry = self.model.FixCountry.getAll(active=1)
        self.telephone = self.model.TelephoneType.getAll(act=1)
        self.education = self.model.EducationType.getAll(act=1)
        self.addresstype = self.model.AddressType.getAll(act=1)
            
        
        return dict(page = 'voters',
                    lang = self.lang,
                    marriageStatus = self.marriageStatus,
                    gender = self.gender,
                    tel = self.tel,
                    religion = self.religion,
                    national = self.national,
                    race = self.race,
                    condition = self.condition,
                    employmentstatus = self.employmentstatus,
                    listConutry = self.listConutry,
                    telephone = self.telephone,
                    education = self.education,
                    addresstype = self.addresstype,
                    
                    voter = voterObject,
                    idproject=None)
        
     
    @expose()   
    def savevoter(self,**kw):
       
        user =  request.identity['user'];
        print "********************"
        print kw['id_voter']
        print kw['id_voter_map_type']
        print kw['id_telephone']
        print kw['id_address']
        print kw['id_employment']
        print "********************"   
        
        voter = self.model.Voter.getId(kw['id_voter'])
        
        if voter is None : 
            print "voter is none"
            voter = self.model.Voter()
                        
        
        voter.email = kw['email']
        voter.prefix = kw['prefix']
        voter.firstname = kw['firstname']
        voter.lastname = kw['lastname']          
       
        voter.id_marriage_status  = kw['id_marriage_status']
        voter.birthdate = kw['birthdate']
        voter.id_gender = kw['id_gender']
           
        voter.id_living_condition = kw['id_living_condition']                                                        
        voter.size_family = kw['size_family']  
        voter.id_language = kw['id_language']
        voter.id_religion = kw['id_religion']
        voter.id_nationality = kw['id_nationality']
        voter.id_race = kw['id_race']
        voter.salary = kw['salary']
        voter.id_education = kw['id_education']
        voter.user_id_owner = user.user_id
        
        print "va %s" % (str( len(kw['id_voter'])))
        if (len(kw['id_voter']) == 0) :            
            voter.save()
         
         
        print "Voter id : %s" %voter.id_voter

        votermaptype =  self.model.VoterMapType.getId(kw['id_voter_map_type'])
        if votermaptype is None : 
            votermaptype = self.model.VoterMapType()
        
        votermaptype.id_voter = voter.id_voter
        votermaptype.id_voter_type = 5
                
        if (len(kw['id_voter_map_type'] ) == 0):
            votermaptype.save() 
        
        print "voter map type id : %s" %votermaptype.id_voter_map_type
        
        votertelephone = self.model.Telephone.getId(kw['id_telephone'])
        if votertelephone is None:
            votertelephone = self.model.Telephone()
        
         
        votertelephone.id_telephone_type = kw['id_telephone_type']
        votertelephone.description = kw['telephone']
        votertelephone.id_voter = voter.id_voter
        
        
        if (len(kw['id_telephone'] ) == 0):
            votertelephone.save()
        
        print "telephone : %s" %votertelephone.id_telephone
        
        voteraddress = self.model.Address.getId(kw['id_address'])
        if voteraddress is None:
            voteraddress = self.model.Address()
        
        voteraddress.id_address_type = kw['id_address_type']
        voteraddress.id_voter = voter.id_voter
        voteraddress.country = kw['id_country']
        voteraddress.province = kw['province']
        voteraddress.city = kw['city']
        voteraddress.county = kw['county']
        
        if (len(kw['id_address'] ) == 0):
            voteraddress.save()
        
          
        voteremployment = self.model.EmploymentDetail.getId(kw['id_employment'])
        if voteremployment is None:
            voteremployment = self.model.EmploymentDetail()
         
        
        voteremployment.id_voter = voter.id_voter
        voteremployment.id_employment_status_type = kw['id_employment_status_type']
        voteremployment.intructry_type = kw['intructry_type']
        voteremployment.job_catagory = kw['job_catagory']
         
        if (len(kw['id_employment'] ) == 0):
            voteremployment.save()
    
             
        redirect('/managepoll/voter')
        
    @expose('managepoll.templates.voter.indextest')
    def indextest(self):    
        return dict(page = 'voter',idproject=None)
    
    
    @expose('managepoll.templates.voter.votertest')
    def voterstest(self,*args,**kw):
        reload(sys).setdefaultencoding('utf8')   
        
        voterObject = VoterObject()        
        print kw
        
        if('idvoter' in kw):
            print kw
            print "Edit voter"
            voter = self.model.Voter.getId(kw['idvoter'])
            voterObject.setVoter(voter)
            #employment = model.EmploymentDetail.getId(kw['idvoter'])
            
        print "voters : lang"
        
        self.lang = self.model.Languages.getAll()
        print self.lang
        self.marriageStatus = self.model.MarriageStatus.getAll(act=1)
        self.gender = self.model.Gender.getAll(act=1)
        self.tel = self.model.TelephoneType.getAll(act=1)
        self.religion = self.model.ReligionType.getAll(act=1)
        self.national = self.model.NationalityType.getAll(act=1)
        self.race = self.model.RaceType.getAll(act=1)
        self.condition = self.model.LivingConditionType.getAll(act=1)
        self.employmentstatus = self.model.EmploymentType.getAll(act=1)
        self.listConutry = self.model.FixCountry.getAll(active=1)
        self.telephone = self.model.TelephoneType.getAll(act=1)
        self.education = self.model.EducationType.getAll(act=1)
        self.addresstype = self.model.AddressType.getAll(act=1)
            
        
        return dict(page = 'votertest',
                    lang = self.lang,
                    marriageStatus = self.marriageStatus,
                    gender = self.gender,
                    tel = self.tel,
                    religion = self.religion,
                    national = self.national,
                    race = self.race,
                    condition = self.condition,
                    employmentstatus = self.employmentstatus,
                    listConutry = self.listConutry,
                    telephone = self.telephone,
                    education = self.education,
                    addresstype = self.addresstype,
                    
                    voter = voterObject,
                    idproject=None)

    
    

    
    
    