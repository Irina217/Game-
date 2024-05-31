# Import уровней
import onelevel
import twolevel
# Библиотеки
import arcade


# Menu settings
width = 600
height = 600
title = "Main menu"


class MenuView(arcade.View):
    def on_show(self):
        self.ground_texture = arcade.load_texture("allnothero/ground.png")
        arcade.set_background_color((248, 210, 223))
        self.ground_sprite = arcade.Sprite()
        self.ground_sprite.texture = self.ground_texture
        self.ground_sprite.center_x = 10
        self.ground_sprite.center_y = 5

        self.hero_texture = arcade.load_texture("hero/hero_stand.png")  # Загрузка текстуры героя из папки hero
        arcade.set_background_color((248, 210, 223))
        self.hero_sprite = arcade.Sprite()
        self.hero_sprite.texture = self.hero_texture
        self.hero_sprite.center_x = 20
        self.hero_sprite.center_y = 125


        self.grass1_texture = arcade.load_texture("allnothero/grass1.png")
        self.grass1_sprite = arcade.Sprite()
        self.grass1_sprite.texture = self.grass1_texture
        self.grass1_sprite.center_x = 59
        self.grass1_sprite.center_y = 130

        self.mushroom_big_texture = arcade.load_texture("allnothero/mushroombig.png")
        self.mushroom_big_sprite = arcade.Sprite()
        self.mushroom_big_sprite.texture = self.mushroom_big_texture
        self.mushroom_big_sprite.center_x = 499
        self.mushroom_big_sprite.center_y = 110

        self.cloud_texture = arcade.load_texture("allnothero/cloud.png")  # Загрузка текстуры облака
        self.cloud_sprite = arcade.Sprite()
        self.cloud_sprite.texture = self.cloud_texture
        self.cloud_sprite.center_x = 100
        self.cloud_sprite.center_y = 400
        self.cloud_speed = 1  # Скорость движения облака
        self.cloud_direction = 1  # Направление движения: 1 - вправо, -1 - влево

        

    def on_draw(self):
        arcade.start_render()  # Начало рендеринга
        self.mushroom_big_sprite.draw()
        self.cloud_sprite.draw()
        arcade.draw_text("Main Menu", width/2, height/2+170,  # Отображение текста "Main Menu" по центру экрана
                         arcade.color.WHITE, font_size=55, anchor_x="center")
        arcade.draw_text("Нажмите цифру уровня для старта", width/2, height/4 - 50,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("A,D движение пробел прыжок", width/2, height/2 -50,
                         arcade.color.BLACK, font_size=17, anchor_x="center")
 
        self.grass1_sprite.draw()        
        self.ground_sprite.draw()
        self.hero_sprite.draw()
    def update(self, delta_time):
        self.cloud_sprite.center_x += self.cloud_speed * self.cloud_direction  # Движение облака

        if self.cloud_sprite.center_x > width + self.cloud_texture.width // 2:  # Если облако уходит за правый край
            self.cloud_sprite.center_x = -self.cloud_texture.width // 2  # Перемещаем его на левый край


        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.KEY_1 or key == arcade.key.NUM_1:
            self.window.close()  
            onelevel.main()
        if key == arcade.key.KEY_2 or key == arcade.key.NUM_2:
            self.window.close()  
            twolevel.main()
            

# Класс, представляющий игровой экран


def main():
    window = arcade.Window(width, height, title)  # Создание игрового окна
    menu_view = MenuView()  # Создание экземпляра представления меню
    window.show_view(menu_view)  # Показать представление меню в игровом окне
    arcade.run()  # Запуск главного игрового цикла

if __name__ == "__main__":
    main()  # Запуск функции main(), если скрипт запускается напрямую
