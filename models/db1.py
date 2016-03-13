#
                     #######
                ##################
            #########################
                ##################
                    ########
                       #

import datetime
                        #
                     #######
                ##################
            #########################
                ##################
                    ########
                       #




db.define_table('city',Field('name','string',requires = IS_NOT_EMPTY()))

db.define_table('posts',
                Field('From_','string',widget = SQLFORM.widgets.autocomplete(request, db.city.name, limitby=(0,3), min_length=1),
                      requires = (IS_LOWER(), IS_NOT_EMPTY())),
                Field('To_','string',widget = SQLFORM.widgets.autocomplete(request, db.city.name, limitby=(0,3), min_length=1),
                      requires = (IS_NOT_EMPTY(),IS_LOWER())),
                Field('On_','date',requires = (IS_DATE_IN_RANGE(format=T('%Y-%m-%d'),
                                                               minimum=datetime.date(2015,10,22),
                                                               maximum=None,
                                                               error_message='Enter a valid date'),IS_NOT_EMPTY())),
                Field('Cost_','integer',requires = IS_NOT_EMPTY()),
                Field('Time_range','string',widget = slider,requires = [IS_NOT_EMPTY()]),
                Field('Seats_','integer',requires = IS_NOT_EMPTY()),
                Field('Description_','text'),
                Field('Smoking_',requires=IS_IN_SET(['YES','NO']),widget=SQLFORM.widgets.radio.widget),
                Field('Music_',requires=IS_IN_SET(['YES','NO']),widget=SQLFORM.widgets.radio.widget),
                Field('Pets_',requires=IS_IN_SET(['YES','NO']),widget=SQLFORM.widgets.radio.widget),
                Field('Driving_Licence_','upload',uploadfield='picture_file',requires = IS_IMAGE()),
                Field('picture_file','blob'),
                auth.signature)
                        #
                     #######
                ##################
            #########################
                ##################
                    ########
                       #


from gluon.tools import Mail
mail = Mail()
mail.settings.server = 'smtp.gmail.com:465'
mail.settings.sender = 'sandeepvarma531@gmail.com'
mail.settings.login = 'sandeepvarma531@gmail.com:joccfzxoyfbqqenv'
mail.settings.ssl = True
mail.settings.tls = True
