# Name: Nate McCain
# Date: 09/25/2014
# Class: CS142
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: Turtle Snow builds a snowman and a snowwoman based on the
#              inputs that are defined in the main function.
# Output: It tells the users where the snow people are standing and then
#         it draws the snow people.


import turtle

# Class 1- Shape
# This class sets the standard pencolor and pensize to be passed on to
# other classes through inheritance. It does not have a draw method
# because I took it from the sample.py provided to the class.

class Shape(object):
    """General shape class"""
    def __init__(self, pencolor = "black", pensize = 1):
        """ Creates a shape
            pencolor - color of the pen for outlining.
            pensize - size (width) of the outline.
        """
        self.pencolor = pencolor
        self.pensize = pensize

    def __str__(self):
        return "The pen is {} wide and its ink is {}.".format(self.pensize,self.pencolor)
    
# Class 1.5- Line
# This class creates the standard line with a starting point, and ending
# point, and it inherits pencolor and pensize from Shape.

class Line(Shape):
    """Line class"""
    def __init__(self, beg = (0.0,0.0), end = (0.0, 50.0),
                 pencolor = "black", pensize = 1):
        """ Creates a line
            beg - coordinates of the beginning point.
            end - coordinates of the end point.
            pencolor - color of the line.
            pensize - size (width) of the line.
        """
        Shape.__init__(self,pencolor,pensize)
        self.beg = beg
        self.end = end

    def __str__(self):
        return "Line(beg: {}, end: {})".format(self.beg, self.end)

    def draw(self, pen):
        """Draw the line using the provided pen"""
        pen.pensize(self.pensize)
        pen.pencolor(self.pencolor)
        pen.up()
        pen.goto(self.beg)
        pen.down()
        pen.goto(self.end)

# Class 2- Circle
# This class creates the Circle shape to be used throughout the program.
# This shape has a bottom starting position, radius, extent of rotation,
# and it inherits pencolor and pensize.

class Circle(Shape):
    """Creates a circle"""
    def __init__(self, pos = (0.0, 0.0), rad = 5,
                 extent = 360, pencolor = "black",
                 pensize = 1):
        """Creates a circle
           pos - starting coordinates of the circle.
           rad - radius of the circle.
           extent - how far the circle is drawn in degrees.
           pencolor - color of the circle's outline
           pensize - size (width) of the circle's outline.
        """
        Shape.__init__(self,pencolor,pensize)
        self.pos = pos
        self.rad = rad
        self.extent = extent
        
    def __str__(self):
        return "Circle starts at {} and has a radius of {}".format(self.pos,self.rad)
    def draw(self, pen):
        """Draw the circle using the provided pen."""
        pen.pensize(self.pensize)
        pen.pencolor(self.pencolor)
        pen.up()
        pen.goto(self.pos)
        pen.down()
        pen.circle(self.rad,self.extent)

# Class 3- Triangle
# This class creates the triangle shape to be used as the girl's hat.
# It takes in three vertices, and it inherits pencolor and pensize.

class Triangle(Shape):
    """Creates a triangle to be used as the girl's hat."""
    def __init__(self, vertexOne = (0.0, 0.0), vertexTwo = (5.0, 5.0),
                 vertexThree = (10.0, 0.0), pencolor = "black",
                 pensize = 1):
        """ Creates a triangle given:
            vertexOne - First vertex coordinates.
            vertexTwo - Second vertex coordinates.
            vertexThree- Third vertex coordinates.
            pencolor - color of the pen.
            pensize - size (width) of the outline.
        """
        Shape.__init__(self,pencolor,pensize)
        self.vertexOne = vertexOne
        self.vertexTwo = vertexTwo
        self.vertexThree = vertexThree

    def __str__(self):
        return "Vertex One is {}, Vertex Two is {}, and Vertex Three is {}.".format(self.vertexOne,self.vertexTwo,self.vertexThree)

    def draw(self, pen):
        """Draws the triangle with the provided pen"""
        pen.pensize(self.pensize)
        pen.pencolor(self.pencolor)
        pen.up()
        pen.goto(self.vertexOne)
        pen.down()
        pen.goto(self.vertexTwo)
        pen.goto(self.vertexThree)
        pen.goto(self.vertexOne)

# Class 4- Box
# This class creates a box type shape that is used to make the man's hat
# and his mustache. It takes in four corners, and it inherits pencolor
# and pensize.

class Box(Shape):
    """Creates a box to be used as a starting spot for the boy's hat."""
    def __init__(self, corner_1 = (0.0, 0.0), corner_2 = (5.0, 0.0),
                 corner_3 = (5.0, 5.0), corner_4 = (0.0, 5.0),
                 pencolor = "black", pensize = 1):
        """Creates a box given:
           corner_1 - Coordinates of the first corner.
           corner_2 - Coordinates of the Second corner.
           corner_3 - Coordinates of the Third corner.
           corner_4 - Coordinates of the Fourth corner.
           pencolor - Color of the pen used to draw.
           pensize - size (width) of the pen outlining the box.
        """
        Shape.__init__(self,pencolor,pensize)
        self.corner_1 = corner_1
        self.corner_2 = corner_2
        self.corner_3 = corner_3
        self.corner_4 = corner_4

    def __str__(self):
        return "Corner 1 is {}, corner 2 is {}, corner 3 is {}, and corner 4 is {}".format(self.corner_1,
                                                                                           self.corner_2,
                                                                                           self.corner_3,
                                                                                           self.corner_4)
    def draw(self, pen):
        """Draws the box with the provided pen."""
        pen.pensize(self.pensize)
        pen.pencolor(self.pencolor)
        pen.up()
        pen.goto(self.corner_1)
        pen.down()
        pen.goto(self.corner_2)
        pen.goto(self.corner_3)
        pen.goto(self.corner_4)
        pen.goto(self.corner_1)

# Class 5- Snow_Person
# This class creates a snow person out of the different shapes. The snow person
# has three circles for the body, three buttons, a mouth, two eyes, and two arms.

class Snow_Person(object):
    """Creates a generic snow person."""
    def __init__(self, pos = (0.0, 0.0)):
        """Creates a generic snow person given:
           pos - Bottom position of the snow person's bottom circle.
        """
        self.pos = pos
        x,y = pos
        self.body_bottom = [Circle((x,y),85,360,"black",4)]
        self.body_middle = [Circle((x,y+170),70,360,"black",4)]
        self.body_top = [Circle((x,y+310),60,360,"black",4)]
        self.eye_left = [Circle((x-20,y+375),10,360,"black",1)]
        self.eye_right = [Circle((x+20,y+375),10,360,"black",1)]
        self.mouth = [Line((x-30,y+337),(x+30,y+337),"black",5)]
        self.button_bottom = [Circle((x,y+185),10,360,"black",1)]
        self.button_middle = [Circle((x,y+230),10,360,"black",1)]
        self.button_top = [Circle((x,y+275),10,360,"black",1)]
        self.arm_left = [Line((x-70,y+240),(x-150,y+240),"black",7)]
        self.arm_right = [Line((x+70,y+240),(x+150,y+240),"black",7)]

    def __str__(self):
        return "Bottom position is: {}.".format(self.pos)

    def draw(self,pen):
        """Draws the generic snow person."""
        for bottom in self.body_bottom:
            bottom.draw(pen)
        for middle in self.body_middle:
            middle.draw(pen)
        for top in self.body_top:
            top.draw(pen)
        pen.color("blue")
        pen.begin_fill()
        for eye_Left in self.eye_left:
            eye_Left.draw(pen)
        pen.end_fill()
        pen.color("blue")
        pen.begin_fill()
        for eye_Right in self.eye_right:
            eye_Right.draw(pen)
        pen.end_fill()           
        for mouth in self.mouth:
            mouth.draw(pen)
        pen.color("blue")
        pen.begin_fill()
        for button_Bottom in self.button_bottom:
            button_Bottom.draw(pen)
        pen.end_fill()
        pen.color("white")
        pen.begin_fill()
        for button_Middle in self.button_middle:
            button_Middle.draw(pen)
        pen.end_fill()
        pen.color("red")
        pen.begin_fill()
        for button_Top in self.button_top:
            button_Top.draw(pen)
        pen.end_fill()           
        for arm_Left in self.arm_left:
            arm_Left.draw(pen)           
        for arm_Right in self.arm_right:
            arm_Right.draw(pen)

# Class 6- Snow_Woman
# This class takes the snow person and adds blonde hair, a pink hat,
# and some lipstick over the mouth.

class Snow_Woman(object):
    """This makes a lady by adding to the snow person."""
    def __init__(self, pos =(0.0, 0.0)):
        """Creates a snow woman just by building off of
           the snow person class.
           pos - Coordinates of the bottom circle of the snow woman.
        """
        self.pos = pos
        x,y = pos
        self.generic_form = [Snow_Person((x,y))]
        self.hair = [Line((x-30,y+430),(x-60,y+310),"yellow",8),
                     Line((x-35,y+430),(x-65,y+310),"yellow",8),
                     Line((x-40,y+430),(x-70,y+310),"yellow",8),
                     Line((x-45,y+430),(x-75,y+310),"yellow",8),
                     Line((x-50,y+430),(x-80,y+310),"yellow",8),
                     Line((x+30,y+430),(x+60,y+310),"yellow",8),
                     Line((x+35,y+430),(x+65,y+310),"yellow",8),
                     Line((x+40,y+430),(x+70,y+310),"yellow",8),
                     Line((x+45,y+430),(x+75,y+310),"yellow",8),
                     Line((x+50,y+430),(x+80,y+310),"yellow",8)]
        self.girly_hat = [Triangle((x-70,y+415),(x,y+485),(x+70,y+415),
                                   "pink",1)]
        self.girl_lips = [Line((x-30,y+337),(x+30,y+337),"pink",9)]

    def __str__(self):
        return "The lady is standing at: {}".format(self.pos)

    def draw(self, pen):
        """This actually draws the lady."""

        for generic_Form in self.generic_form:
            generic_Form.draw(pen)
        for hair_Girl in self.hair:
            hair_Girl.draw(pen)
        pen.color("pink")
        pen.begin_fill()
        for girly_Hat in self.girly_hat:
            girly_Hat.draw(pen)
        pen.end_fill()
        for girly_Lips in self.girl_lips:
            girly_Lips.draw(pen)

# Class 7- Snow_Man
# This class takes a snow person and adds an elegant top hat, a grey
# mustache, and a grey unibrow.

class Snow_Man(object):
    """This makes a snow man by adding to the snow person."""
    def __init__(self, pos = (0.0, 0.0)):
        """Creates a snow man just by building off of
           the snow person class.
           pos - Coordinates of the bottom circle of the snow man.
        """
        self.pos = pos
        x,y = pos
        self.generic_form = [Snow_Person((x,y))]
        self.generic_hat_brim = [Box((x-62,y+420),(x+62,y+420),(x+62,y+440),(x-62,y+440),
                                     "black",1)]
        self.hat_ribbon = [Box((x-52,y+440),(x+52,y+440),(x+52,y+445),(x-52,y+445),"red",1)]
        self.generic_hat_top = [Box((x-52,y+445),(x+52,y+445),(x+52,y+515),(x-52,y+515),
                                    "black",1)]
        self.mustache = [Box((x-35,y+342),(x+35,y+342),(x+27,y+350),(x-27,y+350),"grey",1)]
        self.brows = [Line((x-25,y+400),(x+25,y+400),"grey",7)]
        

    def __str__(self):
        return "The man is standing at: {}".format(self.pos)

    def draw(self, pen):
        """This actually draws the man."""
        for generic_Form in self.generic_form:
            generic_Form.draw(pen)
        pen.color("black")
        pen.begin_fill()
        for generic_Hat_Brim in self.generic_hat_brim:
            generic_Hat_Brim.draw(pen)
        pen.end_fill()
        pen.color("red")
        pen.begin_fill()
        for ribbon in self.hat_ribbon:
            ribbon.draw(pen)
        pen.end_fill()
        pen.color("black")
        pen.begin_fill()
        for generic_Hat_Top in self.generic_hat_top:
            generic_Hat_Top.draw(pen)
        pen.end_fill()
        pen.color("grey")
        pen.begin_fill()
        for facial_Hair in self.mustache:
            facial_Hair.draw(pen)
        pen.end_fill()
        for unibrow in self.brows:
            unibrow.draw(pen)

# Main Function- Creates an instance of a snowman and snowwoman,
# and it tells the user where they are standing. Then it will draw
# the snowman and the snowwoman using turtle. When the user clicks
# on the turtle screen, it will close.

def main():
    pen = turtle.Turtle()

    lady = Snow_Woman((180,-300))
    print(lady)
    lady.draw(pen)

    man = Snow_Man((-180,-300))
    print(man)
    man.draw(pen)

    pen.hideturtle()
    turtle.exitonclick()

main()
