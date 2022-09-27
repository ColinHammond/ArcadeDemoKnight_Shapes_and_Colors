import arcade
#use this to open the window, width 800, Height 600
my_window = arcade.open_window(800,600, "First Window Demo")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
#everthing else goes here
arcade.draw_lrtb_rectangle_filled(50, 200, 200, 50, arcade.color.GENERIC_VIRIDIAN)
arcade.draw_lrtb_rectangle_outline(100, 300, 450, 100, arcade.color.JELLY_BEAN, 20)
arcade.draw_xywh_rectangle_outline(150, 250, 250, 150, arcade.color.LIME, 15)
arcade.draw_xywh_rectangle_filled(500, 150, 150, 250, arcade.color.QUARTZ)
arcade.draw_circle_filled(100, 500, 50, arcade.color.WINE)
arcade.draw_circle_outline(100, 500, 75, arcade.color.WINE, 10)
arcade.draw_triangle_filled(300, 400, 500, 600, 400, 300, arcade.color.NEW_CAR)
arcade.draw_triangle_outline(100, 200, 300, 500, 200, 100, arcade.color.ORCHID, 5)
arcade.draw_arc_filled(300, 500, 100, 100, arcade.color.GOLD, 60, 330)
arcade.draw_arc_outline(500, 600, 100, 100, arcade.color.WHITE_SMOKE, -180, 0, 10)
arcade.finish_render()

arcade.run()