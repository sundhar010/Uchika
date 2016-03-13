#
                     #######
                ##################
            #########################
                ##################
                    ########
                       #

def slider(field,value):
    response.files.append(URL("static","css/slider_need.css"))
    response.files.append(URL("static","js/slider_need.js"))
    response.files.append(URL("static","js/slider_need2.js"))
    wraper = DIV(_style = "flote:left;width:300px;")
    #print SQLFORM.widgets.string.widget(field,value, _display=None)
    a=INPUT(_name = field.name,
                       _id = "posts_Time_range",
                       _type = "text",
                       _style = "border:0; color:#f6931f; font-weight:bold;",
                       _value = value,_readonly=True)
    wraper.append(a)
    wraper.append(DIV(_id="slider-range"))
    s=SCRIPT("""   $(function() {
    $( '#slider-range' ).slider({
      range: true,
      min: 0,
      max: 24,
      values: [ 0, 24 ],
      slide: function( event, ui ) {
        $( '#posts_Time_range' ).val( ui.values[ 0 ] + ":00" + " - " + ui.values[ 1 ] + ":00" );
      }
    });
    $( '#posts_Time_range' ).val(($( "#slider-range" ).slider( "values", 0 ) + ":00"+
      " - " + $( "#slider-range" ).slider( "values", 1 ) + ":00") );
  });""" )
    wraper.components.extend([s])
    return wraper
                        #
                     #######
                ##################
            #########################
                ##################
                    ########
                       #
