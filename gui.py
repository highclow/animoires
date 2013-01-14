from gi.repository import Gtk, Gdk

class MouseButtons:
    
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3


class Window(Gtk.Window):

    def __init__(self):
        super(Window, self).__init__()
        
        self.init_ui()
        
        
    def init_ui(self):

        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_draw)
        self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)        
        self.add(self.darea)                   
        self.darea.connect("button-press-event", self.on_button_press)

        self.set_title("Moires")
        self.resize(600, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)

        self.show_all()

    def initAnimation(self, animation):
        self.animation = animation
        self.animation.run()

    def on_draw(self, wid, cr):
        self.animation.draw(cr)

    def on_button_press(self, w, e):
        if e.type == Gdk.EventType.BUTTON_PRESS \
            and e.button == MouseButtons.LEFT_BUTTON:
            
            if (not self.animation.stop):
                self.animation.stop = True
            else:
                self.animation.stop = False
                self.animation.run()

        '''    
        if e.type == Gdk.EventType.BUTTON_PRESS \
            and e.button == MouseButtons.RIGHT_BUTTON:
            
            self.stop = True
        '''
