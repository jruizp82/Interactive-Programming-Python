# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
CANVAS_SIZE = [800,600]
score = 0
lives = 3
time = 0.5
angle_vel_const = 0.1 # radian
acceleration = 0.5
friction = -0.02
missile_vel = 6.0
rocks = []
missiles = []
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 60)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust == False:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, [self.image_center[0]+self.image_size[0], self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
            
    def update(self):
        global ship_thrust_sound
        self.angle += self.angle_vel
        acc_vector = angle_to_vector(self.angle)
        if self.thrust == True:
            for i in range(2):
                self.vel[i] += acc_vector[i] * acceleration
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
        for i in range(2):
            self.vel[i] *= (1 + friction)
            self.pos[i] = (self.pos[i] + self.vel[i]) % CANVAS_SIZE[i]
            
    def shoot(self):
        global missile_sound, missile_image, missile_info, missiles
        shoot_vector = angle_to_vector(self.angle)
        missiles.append(Sprite([self.pos[0], self.pos[1]], [self.vel[0] + missile_vel * shoot_vector[0], self.vel[1] + missile_vel * shoot_vector[1]], 0, 0, missile_image, missile_info, missile_sound))
        missile_sound.rewind()
        missile_sound.play()
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.life = self.lifespan
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        for i in range(2):
            self.pos[i] = (self.pos[i] + self.vel[i]) % CANVAS_SIZE[i]

           
def draw(canvas):
    global time, rocks
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [CANVAS_SIZE[0] / 2, CANVAS_SIZE[1] / 2], [CANVAS_SIZE[0], CANVAS_SIZE[1]])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [CANVAS_SIZE[0] / 2 + 1.25 * wtime, CANVAS_SIZE[1] / 2], [CANVAS_SIZE[0] - 2.5 * wtime, CANVAS_SIZE[1]])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, CANVAS_SIZE[1] / 2], [2.5 * wtime, CANVAS_SIZE[1]])
    canvas.draw_text("LIVES : " + str(lives), (50, 50), 36, "Red")
    canvas.draw_text("SCORE : " + str(score), (550,50), 36, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    for i in range(len(rocks)):
        rocks[i].draw(canvas)
    for i in range(len(missiles)):
        missiles[i].draw(canvas)
    # update ship and sprites
    my_ship.update()
    for i in range(len(rocks)):
        rocks[i].update()
    expired_missile = -99  # we expect there is only 1 expired missile each time we update the canvas
    for i in range(len(missiles)):
        missiles[i].update()
        missiles[i].life -= 1
        if missiles[i].life <= 0:
            expired_missile = i
    if expired_missile != -99:
        missiles.remove(missiles[expired_missile]) 
        
def keydown(key):
    global my_ship, missile_sound
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel -= angle_vel_const
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel += angle_vel_const
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
    
def keyup(key):
    global my_ship
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel += angle_vel_const
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel -= angle_vel_const
    elif key == simplegui.KEY_MAP["space"]:
        pass
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = False

# timer handler that spawns a rock    
def rock_spawner():
    global rocks
    x = random.random()
    if x > 0.5:
        rocks.append(Sprite([CANVAS_SIZE[0] * random.random(), CANVAS_SIZE[1] * random.random()], [(random.random()-0.5)*5, (random.random()-0.5)*5], 0, (random.random() - 0.5)/10, asteroid_image, asteroid_info))
    
# initialize frame
frame = simplegui.create_frame("Asteroids", CANVAS_SIZE[0], CANVAS_SIZE[1])

# initialize ship and two sprites
my_ship = Ship([CANVAS_SIZE[0] / 2, CANVAS_SIZE[1] / 2], [0, 0], 0, ship_image, ship_info)
rocks.append(Sprite([CANVAS_SIZE[0] * random.random(), CANVAS_SIZE[1] * random.random()], [(random.random()-0.5)*5, (random.random()-0.5)*5], 0, (random.random() - 0.5)/10, asteroid_image, asteroid_info))

# register handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
