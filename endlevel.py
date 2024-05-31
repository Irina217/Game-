import twolevel
import arcade

width = 600
height = 600
title = "End level"

class MenuView(arcade.View):
    def __init__(self, apple_count):
        super().__init__()
        self.apple_count = apple_count

    def on_show(self):
        arcade.set_background_color((248, 210, 223))
        
        self.ground_texture = arcade.load_texture("allnothero/ground.png", mirrored=True)
        self.ground_sprite = arcade.Sprite()
        self.ground_sprite.texture = self.ground_texture
        self.ground_sprite.center_x = 600
        self.ground_sprite.center_y = 5



        self.ground2_texture = arcade.load_texture("allnothero/ground.png")
        self.ground2_sprite = arcade.Sprite()
        self.ground2_sprite.texture = self.ground_texture
        self.ground2_sprite.center_x = 10
        self.ground2_sprite.center_y = 5




    def on_draw(self):
        arcade.start_render()


        arcade.draw_text("Вы прошли уровень", width/2, height/2+60, arcade.color.BLACK, font_size=35, anchor_x="center")
        arcade.draw_text("Нажмите Пробел чтобы продолжить", width/2, height/2 - 50, arcade.color.BLACK, font_size=20, anchor_x="center")
        self.ground_sprite.draw()
        self.ground2_sprite.draw()
        arcade.draw_text(f"Яблоки: {self.apple_count}", width/2, height/2, arcade.color.BLACK, 22, anchor_x="center")


    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.window.close()
            twolevel.main(self.apple_count)

def main(apple_count):
    window = arcade.Window(width, height, title)
    menu_view = MenuView(apple_count)
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main(apple_count=0) 
