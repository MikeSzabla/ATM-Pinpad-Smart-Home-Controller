from app.ui.Elements import Element, TextElement, Cursor, x_center
from app.display.display import display

# CREATE ELEMENTS
text_title = TextElement("ROOMS", x_center(5), 0, False)
text_dining_room = TextElement("Dining Room", x_center(11), 15, True)
element_bedroom = TextElement("Bedroom", x_center(7), 30, True)
element_hallway = TextElement("Hallway", x_center(7), 45, True)

text_title.draw(display)
text_dining_room.draw(display)
element_bedroom.draw(display)
element_hallway.draw(display)
display.show()


# CREATE CURSOR
cursor = Cursor(display, text_dining_room)

# RENDER ALL ELEMENTS
