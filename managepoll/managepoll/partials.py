from tg import expose

@expose('managepoll.templates.little_partial')
def something(name):
    return dict(name=name)