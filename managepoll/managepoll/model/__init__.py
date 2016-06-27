# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from tgext.pluggable import PluggableSession

from surveymodel import *

DBSession = PluggableSession()
DeclarativeBase = declarative_base()



def init_model(app_session):
    print "call init_model in prlugproject"
    DBSession.configure(app_session)








"""
from tgext.pluggable import app_model
from sqlalchemy.ext.declarative import declarative_base
from tgext.pluggable import PluggableSession

DBSession = PluggableSession()
DeclarativeBase = declarative_base()


def init_model(app_session):
    print "init_model : ManagePoll"
    print app_session
    DBSession.configure(app_session)
"""

##from surveymodel import * 

