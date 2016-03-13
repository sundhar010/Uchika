#127.0.0.1:8000/uchika/default/index ------> for home page
#127.0.0.1:8000/uchika/default/take ------> for taking a ride
#127.0.0.1:8000/uchika/default/posts/(page no)?from_=*****&on_=*****&to_=****  ------> shows all posts
#127.0.0.1:8000/uchika/default/show/(arg as id) ---------> shows the post with id
#127.0.0.1:8000/uchika/default/show_his_posts/(auth id)/(page no)   -------> shows all the posts posted bu the auth with id 
#127.0.0.1:8000/uchika/default/offer ------>requirs auth if(auth) form to offer
#127.0.0.1:8000/uchika/default/myposts/<page no.> ------> requirs auth if(auth) shows all recent posts


POSTS_PER_PAGE = 4
def index():
    rows = db(db.posts.On_ >= datetime.datetime.today()).select(orderby=db.posts.created_on)
    return locals()
def take():
    get = SQLFORM.factory(Field('From','string',widget = SQLFORM.widgets.autocomplete(request, db.city.name, limitby=(0,3),min_length=1),
                                requires = [IS_NOT_EMPTY(),IS_LOWER()]),
                          Field('To','string',widget = SQLFORM.widgets.autocomplete(request, db.city.name, limitby=(0,3), min_length=1),
                                requires = [IS_NOT_EMPTY(),IS_LOWER()]),
                          Field('On','date',requires = IS_DATE_IN_RANGE(format=T('%Y-%m-%d'),
                                                               minimum=datetime.date.today(),
                                                               maximum=None,
                                                               error_message='Enter a valid date')),
                         Field('Time_range',widget=slider))
    x = get.element('input',_id = 'no_table_From')
    y = get.element('input',_id = 'no_table_To')
    x['_class']='form-control string'
    y['_class']='form-control string'
    p = get.element('div',_id="_autocomplete_city_name_div")
    p['_style']='z-index:1'
    q = get.element('input',_id = 'no_table_To')
    q['_style']='z-index:-1'
    get.process()
    if get.accepted:
        Time_range = get.vars.Time_range
        print type(get.vars.On)
        redirect(URL('posts',vars = {'from_':get.vars.From,'to_':get.vars.To,'on_' : get.vars.On,'time_':Time_range}))
    else:
        x = get.element('input',_id = 'no_table_From')
        y = get.element('input',_id = 'no_table_To')
        x['_class']='form-control string'
        y['_class']='form-control string'
        p = get.element('div',_id="_autocomplete_city_name_div")
        p['_style']='z-index:1'
        q = get.element('input',_id = 'no_table_To')
        q['_style']='z-index:-1'
    return locals()


def posts():
    page = request.args(0,cast=int,default = 0)
    start = page*POSTS_PER_PAGE
    stop = start + POSTS_PER_PAGE
    From = request.vars.from_
    to = request.vars.to_
    query = (db.posts.From_==request.vars.from_) & (db.posts.To_==request.vars.to_) & (db.posts.On_ ==request.vars.on_ )
    rows = db(query).select(orderby=~db.posts.created_on )
    count = db((db.posts.From_==request.vars.from_) & (db.posts.To_==request.vars.to_) & (db.posts.On_==request.vars.on_ )).count()
    s = request.vars.on_
    l = s.split("-")
    today = request.vars.on_
    nextday = datetime.date(int(l[0]),int(l[1]),int(l[2]))
    previousday = datetime.date(int(l[0]),int(l[1]),int(l[2]))
    nextday+=datetime.timedelta(days=1)
    previousday+=datetime.timedelta(days=-1)
    print nextday,previousday
    return locals()


def show():
    q=request.args(0)
    show = db.posts[q]
    count = db(db.posts.created_by == show.created_by).count()
    get = SQLFORM.factory(Field('From')).process()
    return locals()
def profile():
    q = request.args(0)
    first = db.auth_user(q).first_name
    second = db.auth_user(q).last_name
    gender = db.auth_user(q).Gender
    email = db.auth_user(q).email
    return locals()
def show_his_posts():
    user_id = request.args(0)
    page = request.args(1,cast=int,default = 0)
    start = page*POSTS_PER_PAGE
    stop = start + POSTS_PER_PAGE
    name = db.auth_user(user_id).first_name
    rows = db(db.posts.created_by == user_id).select(orderby=~db.posts.created_on )
    get = SQLFORM.factory(Field('From')).process()
    return locals()

@auth.requires_login()
def myposts():
    page = request.args(0,cast=int,default = 0)
    start = page*POSTS_PER_PAGE
    stop = start + POSTS_PER_PAGE
    rows = db(db.posts.created_by == auth.user.id).select(orderby=~db.posts.created_on)
    return locals()


@auth.requires_login()
def offer():
    form = SQLFORM(db.posts).process()
    x = form.element('input',_id = 'posts_From_')
    y = form.element('input',_id = 'posts_To_')
    x['_class']='form-control string'
    y['_class']='form-control string'
    p = form.element('div',_id="_autocomplete_city_name_div")
    p['_style']='z-index:1'
    if form.accepted:
        #db.posts.insert(Time_range=request.vars.Time_range)
        redirect(URL('index'))
    return locals()

@auth.requires_login()
def book():
    book = SQLFORM.factory(Field('number','integer',requires = IS_NOT_EMPTY())).process()
    n=book.vars.number
    user_id = request.args(0,cast = int)
    if book.accepted:
        redirect(URL('email',vars = {'no_':n,'user_id_':user_id}))
    email = db.auth_user(user_id).email
    return locals()

@auth.requires_login()
def inf():
    no = request.vars.no_
    print auth.user.first_name
    user_id = request.vars.user_id_
    inf = SQLFORM.factory(Field('name','string',requires = IS_NOT_EMPTY()),
                          Field('age','integer',requires = IS_NOT_EMPTY()),
                          Field('gender',requires=IS_IN_SET(['MALE','FEMALE']),widget=SQLFORM.widgets.radio.widget)).process()
    if inf.accepted:
        redirect(URL('email',vars = {'user_id_':user_id,'name_':inf.vars.name,'age_':inf.vars.age,'gender_':inf.vars.gender}))
    return locals()

@auth.requires_login()
def email():
    user_id = request.vars.user_id_
    name = auth.user.first_name
    gender = auth.user.Gender
    print gender
    no = request.vars.no_
    email1=auth.user.email
    email=db.auth_user(user_id).email
    k=mail.send(to=[email],
             subject='Uchika',
             reply_to='sandeepvarma531@gmail.com',
             message='This is from Uchika  Name: '+name+'  wants to book '+ no + ' seats in your ride so please contact him if you like to offer a ride to '+name+' contact to Email id : '+email1+' .')
    return locals()



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
def via():
    print request.args[0]
