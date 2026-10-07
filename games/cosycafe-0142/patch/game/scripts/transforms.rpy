init:
    if renpy.variant('pc'):
        default persistent.ui_speed_multiplier = 1.0
        default persistent.ui_delay_multiplier = 1.0
    else:
        default persistent.ui_speed_multiplier = .0
        default persistent.ui_delay_multiplier = .0
        
    default persistent.temp_ui_speed_multiplier = 1.0 - persistent.ui_speed_multiplier
    default persistent.temp_ui_delay_multiplier = 1.0 - persistent.ui_delay_multiplier

    default persistent.border_thickness = 3.0
    default persistent.border_colour    = "#161616"   

transform BAPR():

    easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0

transform BDPR():

    easein_quint (.5 * persistent.ui_speed_multiplier) alpha .0

transform BNT():

    alpha .0
    
transform BDPRT():

    easein_quint (.5 * persistent.ui_speed_multiplier) alpha .8

transform BNTT():

    alpha .8

transform button_text_enlarge():

    subpixel True
    zoom     1.0

    on idle:
        easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.0
    on hover:
        easein_quint (.5 * persistent.ui_speed_multiplier) zoom 1.05

transform button_enter_mm(wait = 0):

    subpixel True
    xzoom   .0
    yzoom   .0
    alpha   .0
    blur     5
    xoffset -250

    pause   (wait * persistent.ui_delay_multiplier)

    easein_quint (1.5 * persistent.ui_speed_multiplier) xoffset 0 alpha 1.0 blur .0 xzoom 1.0 yzoom 1.0

transform button_hover_mm():

    subpixel True

    on hover:

        easein_quint (.5 * persistent.ui_speed_multiplier) xoffset 5 yoffset -5 xzoom 1.1 yzoom 1.1

    on idle:

        easein_quint (.5 * persistent.ui_speed_multiplier) xoffset 0 yoffset 0 xzoom 1.0 yzoom 1.0

transform button_image_mm():

    subpixel   True

    zoom 1.0
    blur 0

    on idle:

        easein_quint (.5 * persistent.ui_speed_multiplier) blur 0 zoom 1.0

    on hover:

        easein_quint (.5 * persistent.ui_speed_multiplier) blur 5 zoom 1.05

transform button_image_fg():

    subpixel True

    xycenter (.5, .5)
    align    (.5, .5)
    blur       0

    on idle:

        easein_quint (.5 * persistent.ui_speed_multiplier) blur 0 xzoom 1.0 yzoom 1.0

    on hover:

        easein_quint (.5 * persistent.ui_speed_multiplier) blur 5 xzoom 1.05 yzoom 1.05

transform button_cascade(wait = 0):

    xycenter (.5, .5)
    blur       5
    alpha     .0
    zoom      .0
    xoffset   -250

    pause     (wait * persistent.ui_delay_multiplier)

    easein_quint (1.0 * persistent.ui_speed_multiplier) blur 0 xoffset 0 alpha 1.0 zoom 1.0

transform button_cascade_bottom(wait = 0):

    xycenter (.5, .5)
    blur       5
    alpha     .0
    zoom      .0
    yoffset    1080

    pause     (wait * persistent.ui_delay_multiplier)

    easein_quint (1.0 * persistent.ui_speed_multiplier) blur 0 yoffset 0 alpha 1.0 zoom 1.0

transform fade_in(wait = 0):

    blur   5
    alpha .0

    pause (wait * persistent.ui_delay_multiplier)

    easein_quint (1.0 * persistent.ui_speed_multiplier) alpha 1.0 blur 0

transform item_in(wait = 0):

    subpixel   True

    xycenter (.5, .5)
    xzoom     .0
    yzoom     .0
    alpha     .0
    xoffset   -50

    pause      (wait * persistent.ui_delay_multiplier)

    easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 xoffset 0 xzoom 1.0 yzoom 1.0

transform shrink():

    subpixel True

    on hover:

        easein_quint 0.3 xzoom .99 yzoom .99

    on idle:

        easein_quint 0.3 xzoom 1.0 yzoom 1.0

transform bios_draw(wait = 0):

    subpixel   True

    xycenter (.5, .5)
    xzoom     .0
    yzoom     .0
    alpha     .0
    yoffset   -500

    pause      (wait * persistent.ui_delay_multiplier)

    easein_quint (.75 * persistent.ui_speed_multiplier) alpha 1.0 yoffset 0 xzoom 1.0 yzoom 1.0

transform cascade_info(wait = 0):

    subpixel   True

    xycenter (.5, .5)
    zoom      .0
    alpha     .0
    blur       5
    yoffset   -250

    pause      (wait * persistent.ui_delay_multiplier)

    easein_quint (.5 * persistent.ui_speed_multiplier) yoffset 0 alpha 1.0 blur 0 zoom 1.0

transform cascade_image_gallery_char(wait = 0):

    subpixel   True

    xycenter (.5, .5)
    zoom      .0
    alpha     .0
    blur       5
    yoffset   -250

    pause      (wait * persistent.ui_delay_multiplier)

    easein_quint (.5 * persistent.ui_speed_multiplier) yoffset 0 alpha 1.0 blur 0 zoom 1.0

    on idle:

        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.0)

    on hover:

        easein_quint (.5 * persistent.ui_speed_multiplier) matrixcolor BrightnessMatrix(.125)

transform cascade_image_gallery_char_h(wait = 0):

    subpixel   True

    xycenter (.5, .5)
    zoom      .0
    alpha     .0
    blur       5
    xoffset   -250

    pause      (wait * persistent.ui_delay_multiplier)

    easein_quint (.5 * persistent.ui_speed_multiplier) xoffset 0 alpha 1.0 blur 0 zoom 1.0

transform bg_in():

    subpixel   True

    xycenter (.5, .5)
    alpha     .0
    zoom       1.25

    ease_quint (1.0 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0

transform bios_bg_in():

    subpixel   True

    xycenter (.5, .5)
    alpha     .0
    zoom       1.25
    blur       25

    easein_quint (.75 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0 blur 0

transform blur_in():

    subpixel True

    blur     0

    ease_quint (.5 * persistent.ui_speed_multiplier) blur 6

transform bios_char_slide_in():

    subpixel True

    zoom    .5
    blur     25
    xoffset -1280
    
    easein_quint (.75 * persistent.ui_speed_multiplier) xoffset -640 blur 0

transform bar_in():

    yoffset 250
    alpha  .0

    easein_quint (.75 * persistent.ui_speed_multiplier) alpha 1.0 yoffset 0

transform bios_text_in():

    alpha   .0
    zoom    .0
    xoffset -250

    easein_quint (.75 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0 xoffset 0

transform plate_in():
    
    subpixel   True

    xycenter (.5, .5)
    zoom      .0

    easein_quint (1.0 * persistent.ui_speed_multiplier) zoom 1.0

transform photo_gallery_general_in():

    subpixel True

    alpha   .0
    blur     5
    xoffset -250

    easein_quint (1.0 * persistent.ui_speed_multiplier) alpha 1.0 xoffset 0 blur 0

transform cascade_navigation(wait = 0):

    alpha   .0
    zoom    .0
    offset (-50, -50)
    
    pause (wait * persistent.ui_delay_multiplier)
    
    easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0 offset (.0, .0)

transform cascade_options(wait = 0):

    alpha  .0
    zoom   .0
    offset (0, -100)

    pause (wait * persistent.ui_delay_multiplier)

    easein_quint (.5 * persistent.ui_speed_multiplier) alpha 1.0 zoom 1.0 offset (0, 0) 

transform socials():

    subpixel   True

    xycenter (.5, .5)
    align    (.5, .5)
    blur       0

    on idle:

        easein_quint (.5 * persistent.ui_speed_multiplier) blur 0 xzoom 1.0 yzoom 1.0

    on hover:

        easein_quint (.5 * persistent.ui_speed_multiplier) blur 2 xzoom 1.05 yzoom 1.05

transform temp_gallery():

    zoom .5
    blur 0
    matrixcolor BrightnessMatrix(0)
    easein_quint (.75 * persistent.ui_speed_multiplier) blur 2 matrixcolor BrightnessMatrix(-.2)