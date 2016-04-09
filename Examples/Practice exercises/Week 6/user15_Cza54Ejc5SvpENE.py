# Application of Subimage class


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
# Student adds code as necessary below

import simplegui

#load big image
instructor_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/instructors.jpg")

# create a Subimage objecta
joe_image = Subimage(instructor_image, [715, 150], [200, 200], "Joe")
scott_image = Subimage(instructor_image, [390, 225], [200, 200], "Scott")
john_image = Subimage(instructor_image, [500, 150], [200, 200], "John")
stephen_image = Subimage(instructor_image, [185, 250], [200, 200], "Stephen")

current_image = john_image


# define button handlers
def joe_button():
    global current_image
    current_image = joe_image

def scott_button():
    global current_image
    current_image = scott_image

def john_button():
    global current_image
    current_image = john_image

def stephen_button():
    global current_image
    current_image = stephen_image
   
def awesome_button():
    current_caption = current_image.get_caption()
    current_image.set_caption(current_caption + " is awesome!")

# draw handler
def draw(canvas):
    current_image.draw(canvas, [100, 100])
    
    
frame = simplegui.create_frame("Subimage application", 200, 200)
frame.add_button("Joe", joe_button, 100)
frame.add_button("Scott", scott_button, 100)
frame.add_button("John", john_button, 100)
frame.add_button("Stephen", stephen_button, 100)
frame.add_button("Make awesome", awesome_button, 200)

frame.set_draw_handler(draw)
frame.start()




