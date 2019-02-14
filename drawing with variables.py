import arcade


WIDTH = 640
HEIGHT = 480

radius = int(input("Please give radius: "))
x = int(input("please give x-location: "))
y = int(input("please give y-location: "))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.DARK_MOSS_GREEN)

arcade.start_render()
# Begin drawing
arcade.draw_circle_filled(x, y, radius, arcade.color.GREEN_YELLOW) #x, y, radius

# End drawing
arcade.finish_render()
arcade.run()