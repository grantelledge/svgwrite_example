import textwrap as tw
import svgwrite as svg
    
# initialize the drawing and background
dwg = svg.Drawing('output.svg')
bg_color = svg.rgb(25, 25, 25)
dwg.add(dwg.rect((0, 0), (1200, 1800), fill = bg_color))

# add some shapes
dwg.add(dwg.rect((50, 50), (1100, 700), stroke = svg.rgb(50, 50, 50, '%'), fill = bg_color, stroke_width = 3)) # top left, size, border color, fill color, border width
dwg.add(dwg.rect((50, 800), (1100, 950), stroke = svg.rgb(50, 50, 50, '%'), fill = bg_color, stroke_width = 3))

line_y_coord = [75, 725, 775, 825, 1725]
for y in line_y_coord:
    dwg.add(dwg.line((75, y), (1125, y), stroke = svg.rgb(50, 50, 50, '%'), stroke_width = 3)) # start, end, line color, stroke width

# option 1: import font data from the local file system
dwg.embed_font(name = "Nabla", filename = 'nabla.ttf')
dwg.add_stylesheet('font_classes.css', 'External CSS')

# add title
my_title = 'This is a book title <4 lines'
my_title_wrapped = tw.wrap(''.join(my_title), 10)
g = dwg.g(class_='nabla')

for i, line in enumerate(my_title_wrapped):
    g.add(dwg.text(line, insert=(100, 290 + i*200), class_='nabla'))
dwg.add(g)

# option 2: font data accessed through Google fonts
dwg.embed_google_web_font(name = "Montserrat", uri = 'https://fonts.googleapis.com/css?family=Montserrat')
dwg.add_stylesheet('font_classes.css', 'External CSS')

# add cover text
my_text = 'This is the content that goes on the front of the book, perhaps a really long subtitle or a description of the book. You can fit more than enough text at this scale. And author names can go here, too.'
my_text_wrapped = tw.wrap(''.join(my_text), 39)
g = dwg.g(class_='montserrat')

for i, line in enumerate(my_text_wrapped):
    g.add(dwg.text(line, insert=(100, 890 + i*60), class_='montserrat'))
dwg.add(g)

# and an image, for good measure
dwg.add(svg.image.Image('https://assets-cdn.kathmandupost.com/uploads/source/news/2019/lifestyle/shutterstock_1501191593.jpg', size = (600, 900), insert = (100, 1000)))

# and the module requires a save after all of the drawing is done
dwg.save(pretty = True)
