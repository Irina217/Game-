import arcade

width = 600
height = 600
title = "End"

class MenuView(arcade.View):
    def __init__(self, apple_count):
        super().__init__()
        self.apple_count = apple_count

    def on_show(self):
        arcade.set_background_color((248, 180, 193))
        self.ground_texture = arcade.load_texture("allnothero/ground.png", mirrored=True)
        self.ground_sprite = arcade.Sprite()
        self.ground_sprite.texture = self.ground_texture
        self.ground_sprite.center_x = 600
        self.ground_sprite.center_y = 5

        self.hero_texture = arcade.load_texture("hero/hero_stand.png", mirrored=True)
        self.hero_sprite = arcade.Sprite()
        self.hero_sprite.texture = self.hero_texture
        self.hero_sprite.center_x = 570
        self.hero_sprite.center_y = 125

        self.mushroom_big_texture = arcade.load_texture("allnothero/mushroom2.png", mirrored=True)
        self.mushroom_sprites = arcade.SpriteList()

        self.cloud_texture = arcade.load_texture("allnothero/cloud.png")
        self.cloud_sprite = arcade.Sprite()
        self.cloud_sprite.texture = self.cloud_texture
        self.cloud_sprite.center_x = 100
        self.cloud_sprite.center_y = 400
        self.cloud_speed = 1
        self.cloud_direction = 1

        self.cloud2_texture = arcade.load_texture("allnothero/cloud2.png")
        self.cloud2_sprite = arcade.Sprite()
        self.cloud2_sprite.texture = self.cloud2_texture
        self.cloud2_sprite.center_x = 350
        self.cloud2_sprite.center_y = 560
        self.cloud2_speed = 1
        self.cloud2_direction = 1

    def on_draw(self):
        arcade.start_render()
        self.cloud_sprite.draw()
        self.cloud2_sprite.draw()
        arcade.draw_text("Final!", width/2, height/2+170, arcade.color.WHITE, font_size=55, anchor_x="center")
        arcade.draw_text("Нажмите Q чтобы закрыть окно", width/2, height/2 - 50, arcade.color.BLACK, font_size=20, anchor_x="center")
        self.ground_sprite.draw()
        self.hero_sprite.draw()
        arcade.draw_text(f"Яблоки: {self.apple_count}", width/2, height/2, arcade.color.BLACK, 22, anchor_x="center")

    def update(self, delta_time):
        self.cloud_sprite.center_x += self.cloud_speed * self.cloud_direction
        self.cloud2_sprite.center_x += self.cloud2_speed * self.cloud2_direction

        if self.cloud_sprite.center_x > width + self.cloud_texture.width // 2:
            self.cloud_sprite.center_x = -self.cloud_texture.width // 2

        if self.cloud2_sprite.center_x > width + self.cloud2_texture.width // 2:
            self.cloud2_sprite.center_x = -self.cloud2_texture.width // 2

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            self.window.close()


def main(apple_count):
    window = arcade.Window(width, height, title)
    menu_view = MenuView(apple_count)
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main(apple_count=0) 
