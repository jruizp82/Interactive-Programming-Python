# Implementation of Subimage class


#################################################
# Student adds code where appropriate

# definition of Subimage class
class Subimage:
    
    def __init__(self, image, center, size, caption):
        self.image = image
        self.image_center = center
        self.image_size = size
        self.caption = caption
        self.modified = False
        
    def draw(self, canvas, target):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          target, self.image_size)
        canvas.draw_text(self.caption, [target[0] - self.image_size[0] * 0.25, target[1] + self.image_size[1] * 0.4], 18, "White")
    
    def get_caption(self):
        return self.caption
    
    def set_caption(self, new_caption):
        if not self.modified:
            self.caption = new_caption
            self.modified = True
        
    
    
###################################################
# Testing code

import simplegui

instructor_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/instructors.jpg")

# create a Subimage object
john_image = Subimage(instructor_image, [500, 150], [200, 200], "John")

def draw(canvas):
    john_image.draw(canvas, [100, 100])
    
    
frame = simplegui.create_frame("Subimage test", 200, 200)
frame.set_draw_handler(draw)
frame.start()

# test code for get_caption and set_caption
print john_image.get_caption()
john_image.set_caption("Greiner")
print john_image.get_caption()
john_image.set_caption("Rocks!")
print john_image.get_caption()



####################################################
# Output  - should see a picture of John with caption "Greiner"

#John
#Greiner
#Greiner


