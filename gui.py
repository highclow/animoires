from gi.repository import Gtk, Gdk
import gobject


class MouseButtons:

    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3


class Window(Gtk.Window):

    def __init__(self, animation):
        super(Window, self).__init__()
        self.frame = 0
        self.time = 0.0
        self.playing = False
        self.animation = animation
        self.init_ui()

    def init_ui(self):
        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_draw)
        self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.add(self.darea)
        self.darea.connect("button-press-event", self.on_button_press)

        self.set_title("Moires")
        self.resize(self.animation.width, self.animation.height)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)

        self.show_all()

    def on_draw(self, wid, cr):
        self.animation.draw(cr, self.time)

    def on_button_press(self, w, e):
        if e.type == Gdk.EventType.BUTTON_PRESS \
            and e.button == MouseButtons.LEFT_BUTTON:
            if (self.playing):
                self.stopPlaying()
            else:
                self.startPlaying()

        '''
        if e.type == Gdk.EventType.BUTTON_PRESS \
            and e.button == MouseButtons.RIGHT_BUTTON:
            self.stop = True
        '''

    def incFrame(self):
        self.frame = self.frame + 1
        self.time = float(self.frame) / self.animation.frameRate
        if (self.time > self.animation.duration):
            self.time = 0
            self.frame = 0
            self.stopPlaying()
        else:
            self.darea.queue_draw()
        return self.playing

    def startPlaying(self):
        self.playing = True
        gobject.timeout_add(1000 / self.animation.frameRate, self.incFrame)

    def stopPlaying(self):
        self.playing = False
