#!/usr/bin/python

from gi.repository import Gtk, Gdk
import cairo


class MouseButtons:
    
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3
    
    
class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        
    def init_ui(self):    

        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_draw)
        self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        #self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        #self.darea.set_events(key_press_event)
        self.add(self.darea)
        
        #self.coords = []
        self.w = 520
        self.h = 200
        self.linePos = 4
        self.text = True
        self.grid = True
        self.printPng = False


        self.darea.connect("button-press-event", self.on_button_press)
        self.connect('key_press_event', self.on_key_press_event)
        self.set_title("Moving moires")
        self.resize(self.w, self.h)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
    def paintTransparentBackground(self, cr):
        cr.set_source_rgba(0.0, 0.0, 0.0, 0.0)
        cr.paint()



    def getGridSurface(self, nbLines, lineWidth, offsetX, originX):
        s = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.w, self.h)
        lcr = cairo.Context(s)
        self.paintTransparentBackground(lcr)
        lcr.set_source_rgba(0.0, 0.0, 0.0, 1.0)
        lcr.set_line_width(lineWidth)
        for i in range(nbLines):
            lx = (i * offsetX) + originX
            lcr.move_to(lx, 0)
            lcr.line_to(lx, self.h)
            lcr.stroke()
        return s
    
    def getTextSurface(self, text, x, y, fontFace, fontSize):
        s = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.w, self.h)
        lcr = cairo.Context(s)
        self.paintTransparentBackground(lcr)
        lcr.set_source_rgb(0.0, 0.0, 0.0)
        lcr.select_font_face(fontFace, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        lcr.set_font_size(fontSize)
        (x, y, width, height, dx, dy) = lcr.text_extents(text)
        lcr.move_to(self.w / 2 - width / 2, self.h / 2)
        lcr.show_text(text)
        
        return s

    def on_draw(self, wid, cr):
        imgSurface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.w, self.h)
        imgCr = cairo.Context(imgSurface)
        self.paintTransparentBackground(imgCr)
        textList = ['Save  the  Date', '' , 'Melissa & Joseph', '', '17  Mai  2014', '']
        
        originX = 10
        originY = 150
        
        #fontFace = 'Purisa'
        #fontFace = 'UnPilGi'
        fontFace = 'Comic Sans MS'
        fontSize = 60

        offsetX = 6
        nbLines = 150
        lineWidth = 1.0

        if (self.text):
            for i, text in enumerate(textList):
                localMove = lineWidth * i
                lx = originX + localMove # Move text by one linewidth
                imgCr.set_source_surface(self.getTextSurface(text, lx, originY, fontFace, fontSize), 0, 0)
                imgCr.mask_surface(self.getGridSurface(nbLines, lineWidth, offsetX, localMove), 0, 0)
        if self.grid:
            imgCr.set_source_surface(self.getGridSurface(nbLines, offsetX - lineWidth, offsetX, self.linePos))
            imgCr.paint()

        if (self.printPng):
            imgSurface.write_to_png("img.png")
            self.printPng = False
        cr.set_source_surface(imgSurface)
        cr.paint()
                                              
    def on_button_press(self, w, e):
        if e.type == Gdk.EventType.BUTTON_PRESS \
            and e.button == MouseButtons.LEFT_BUTTON:
            self.linePos += 0.5
            
        if e.type == Gdk.EventType.BUTTON_PRESS \
            and e.button == MouseButtons.RIGHT_BUTTON:
            self.linePos -= 0.5
        
        self.darea.queue_draw()

    def on_key_press_event(self, w, e):
        keyname = Gdk.keyval_name(e.keyval)
        if keyname == 't':
            self.text = not self.text
        if keyname == 'g':
            self.grid = not self.grid
        if keyname == 'p':
            self.printPng = True
        self.darea.queue_draw()

    
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()