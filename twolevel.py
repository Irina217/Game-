import arcade
import random
import end

# Размер экрана и название
width = 1680
height = 800
title = "jng_alpha"

movespeed = 15
num_jump_frames = 1  # Количество кадров анимации прыжка
num_throw_frames = 2  # Количество кадров анимации броска

class MyHero(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()

        # Устанавливаем текстуры для стояния вправо и влево
        self.stand_right_textures = [arcade.load_texture("hero2/hero_stand.png")]
        self.stand_left_textures = [arcade.load_texture("hero2/hero_stand.png", mirrored=True)]
        # Устанавливаем текстуры для ходьбы вправо и влево
        self.walk_right_textures = [arcade.load_texture(f"hero2/hero_walk{i}.png") for i in range(2)]
        self.walk_left_textures = [arcade.load_texture(f"hero2/hero_walk{i}.png", mirrored=True) for i in range(2)]
        # Устанавливаем текстуры для прыжка вправо и влево
        self.jump_right_textures = [arcade.load_texture(f"hero2/hero_jump{i}.png") for i in range(1, num_jump_frames + 1)]
        self.jump_left_textures = [arcade.load_texture(f"hero2/hero_jump{i}.png", mirrored=True) for i in range(1, num_jump_frames + 1)]
        # Устанавливаем текстуры для броска вправо и влево
        self.throw_right_textures = [arcade.load_texture(f"hero2/hero_throw{i}.png") for i in range(1, num_throw_frames + 1)]
        self.throw_left_textures = [arcade.load_texture(f"hero2/hero_throw{i}.png", mirrored=True) for i in range(1, num_throw_frames + 1)]

        # Устанавливаем начальное положение и скорость движения героя
        self.jump_speed = 50
        self.is_jumping = False
        
        self.is_throwing = False
        self.jump_frames = 0  # Для управления анимацией прыжка
        self.throw_frames = 0  # Для управления анимацией броска


    def update_animation(self):
        if self.is_throwing:
            self.throw_frames += 1
            if self.throw_frames >= num_throw_frames:
                self.is_throwing = False
                self.throw_frames = 0
            else:
                if self.change_x < 0:
                    self.texture = self.throw_left_textures[self.throw_frames]
                else:
                    self.texture = self.throw_right_textures[self.throw_frames]
        elif self.is_jumping:
            if self.change_y > 0:  # Прыжок вверх
                self.jump_frames = (self.jump_frames + 1) % num_jump_frames
                if self.change_x < 0:
                    self.texture = self.jump_left_textures[self.jump_frames]
                else:
                    self.texture = self.jump_right_textures[self.jump_frames]
            else:  # Падение после прыжка
                self.texture = arcade.load_texture("hero2/hero_jump1.png")
        else:
            super().update_animation()
class MyGame(arcade.Window):
    def __init__(self, apple_count):
        super().__init__(width, height, title)
        self.apple_count = apple_count

        self.setup()
        self.move_right_enemy = True
        self.background_music = arcade.Sound("background.mp3", streaming=True)
        self.background_player = self.background_music.play(volume=0.5, loop=True)

    def setup(self):
        # Загрузка текстур и фоновое изображение
        self.final_texture = arcade.load_texture("allnothero2/final.png")
        self.Enemy_texture = arcade.load_texture("allnothero2/enemy.png")
        self.background_texture = arcade.load_texture("allnothero2/background_image.png")
        self.apple_texture = arcade.load_texture("allnothero2/apple.png")
        self.ground_texture = arcade.load_texture("allnothero2/ground.png")
        self.item_texture = arcade.load_texture("allnothero2/apple.png")

        # Анимация героя
        self.hero_animation = MyHero()
        self.hero_animation.center_x = 125  # Устанавливаем начальное положение героя
        self.hero_animation.center_y = 279
        self.jump_speed = 50
        self.is_jumping = False
        self.can_jump = True
        self.can_double_jump = True

        # Параметры врага
        self.moveXEnemy = 5
        self.moveYEnemy = 0

        # Враг 1
        self.Enemy_sprite = arcade.Sprite()
        self.Enemy_sprite.texture = self.Enemy_texture
        self.Enemy_sprite.center_x = random.randint(1200, 1290)
        self.Enemy_sprite.center_y = 176

        # Враг 2
        self.Enemy_sprite2 = arcade.Sprite()
        self.Enemy_sprite2.texture = self.Enemy_texture
        self.Enemy_sprite2.center_x = 800
        self.Enemy_sprite2.center_y = 176

        self.killcheck = True

        # Параметры яблока
        self.apple_sprite = arcade.Sprite()
        self.apple_sprite.texture = self.apple_texture
        self.apple_sprite.position = (random.randint(250, 730), random.randint(175, 325))
        self.apple2_sprite = arcade.Sprite()
        self.apple2_sprite.texture = self.apple_texture
        self.apple2_sprite.position = (random.randint(730, 1630), random.randint(175, 325))
        
        
        # Добавляем переменные для позиции и движения облака
        self.cloud_texture = arcade.load_texture("allnothero2/cloud.png")
        self.cloud_x = 100  # Начальная позиция X в центре экрана
        self.cloud_y = random.randint(325, 750)  # Начальная позиция Y в центре экрана
        self.cloud_speed = 1  # Можно настроить по желанию
        self.cloud_direction = 1  # 1 для движения вправо, -1 для движения влево

        self.cloud2_texture = arcade.load_texture("allnothero2/cloud2.png")
        self.cloud2_x = 200  # Начальная позиция X в центре экрана
        self.cloud2_y = random.randint(625, 790)  # Начальная позиция Y в центре экрана

        # Земля
        self.ground_sprites = arcade.SpriteList()

        ground3 = arcade.Sprite()
        ground3.texture = self.ground_texture
        ground3.center_x = 1240
        ground3.center_y = 45
        self.ground_sprites.append(ground3)

        ground4 = arcade.Sprite()
        ground4.texture = self.ground_texture
        ground4.center_x = 220
        ground4.center_y = 145
        self.ground_sprites.append(ground4)

        ground1 = arcade.Sprite()
        ground1.texture = self.ground_texture
        ground1.center_x = 140
        ground1.center_y = 45
        self.ground_sprites.append(ground1)
        ground2 = arcade.Sprite()
        ground2.texture = self.ground_texture
        ground2.center_x = 390
        ground2.center_y = 45
        self.ground_sprites.append(ground2)
        ground7 = arcade.Sprite()
        ground7.texture = self.ground_texture
        ground7.center_x = 790
        ground7.center_y = 45
        self.ground_sprites.append(ground7)
        ground8 = arcade.Sprite()
        ground8.texture = self.ground_texture
        ground8.center_x = 1590
        ground8.center_y = 45
        self.ground_sprites.append(ground8)

        # Трава и грибы
        self.grass1_texture = arcade.load_texture("allnothero2/grass1.png")
        self.grass2_texture = arcade.load_texture("allnothero2/grass2.png")
        self.grass3_texture = arcade.load_texture("allnothero2/grass3.png")
        self.grass4_texture = arcade.load_texture("allnothero2/grass4.png")
        self.mushroom_big_texture = arcade.load_texture("allnothero2/mushroombig.png")

        # Создание спрайтов травы
        self.grass1_sprite = arcade.Sprite()
        self.grass1_sprite.texture = self.grass1_texture
        self.grass1_sprite.center_x = 1230
        self.grass1_sprite.center_y = 180

        self.mushroom_big_sprite = arcade.Sprite()
        self.mushroom_big_sprite.texture = self.mushroom_big_texture
        self.mushroom_big_sprite.center_x = 1280
        self.mushroom_big_sprite.center_y = 230

        self.mushroom_big_sprite2 = arcade.Sprite()
        self.mushroom_big_sprite2.texture = arcade.load_texture("allnothero2/mushroombig.png", mirrored=True)
        self.mushroom_big_sprite2.center_x = 160
        self.mushroom_big_sprite2.center_y = 330

        # Счетчик яблок
        self.apple_count = 0
        self.applecheck = True
        self.applecheck2 = True

        # Список предметов
        self.items_list = arcade.SpriteList()

        # Параметры финальной текстуры
        self.final_sprite = arcade.Sprite()
        self.final_sprite.texture = self.final_texture
        self.final_sprite.center_x = 1640  # Устанавливаем координаты финальной текстуры
        self.final_sprite.center_y = 225

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, width, height, self.background_texture)
        
        # Отрисовка земли
        self.ground_sprites.draw()

        # Отрисовка облаков
        arcade.draw_lrwh_rectangle_textured(self.cloud_x, self.cloud_y, self.cloud_texture.width, self.cloud_texture.height, self.cloud_texture)
        arcade.draw_lrwh_rectangle_textured(self.cloud2_x, self.cloud2_y, self.cloud2_texture.width, self.cloud2_texture.height, self.cloud2_texture)

        # Отрисовка врагов
        self.Enemy_sprite.draw()
        self.Enemy_sprite2.draw()

        # Отрисовка героя
        self.hero_animation.draw()

        # Отрисовка предметов
        self.items_list.draw()

        # Отрисовка яблок
        self.apple_sprite.draw()
        self.apple2_sprite.draw()
        
        # Отрисовка финальной текстуры
        self.final_sprite.draw()

        # Отрисовка травы
        self.grass1_sprite.draw()

        # Отрисовка грибов
        self.mushroom_big_sprite.draw()
        self.mushroom_big_sprite2.draw()

        arcade.draw_text(f"Apples: {self.apple_count}", 10, 700, arcade.color.BLACK, 20)
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.hero_animation.change_x = -movespeed
        elif key == arcade.key.D:
            self.hero_animation.change_x = movespeed
        if key == arcade.key.SPACE:
            if not self.hero_animation.is_jumping:
                self.hero_animation.change_y = self.jump_speed
                self.hero_animation.is_jumping = True
                self.hero_animation.jump_frames = 0  # Сброс кадров прыжка
                self.can_double_jump = True  # Разрешаем двойной прыжок после первого прыжка
            elif self.can_double_jump:
                self.hero_animation.change_y = self.jump_speed
                self.hero_animation.is_jumping = True
                self.hero_animation.jump_frames = 0  # Сброс кадров прыжка
                self.can_double_jump = False  # Запрещаем двойной прыжок после второго
        elif key == arcade.key.E and not self.hero_animation.is_throwing:
            self.hero_animation.is_throwing = True
            self.throw_item()  # Исправлено: добавлен вызов функции броска предмета
        elif key == arcade.key.Q:
            self.background_music.stop(self.background_player)
            self.close()  # Закрыть окно и выйти из игры
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.hero_animation.change_x = 0
    def transition_to_next_level(self):
        twolevel.main(self.apple_count)

    def throw_item(self):
        item_sprite = arcade.Sprite()
        item_sprite.texture = self.item_texture
        item_sprite.center_x = self.hero_animation.center_x
        item_sprite.center_y = self.hero_animation.center_y
        item_sprite.change_x = 10 if self.hero_animation.change_x >= 0 else -10
        self.items_list.append(item_sprite)
    def remove_item():
        item_sprite.kill()
        self.items_list.remove(item_sprite)
        arcade.schedule(remove_item, 0.5)

    def update(self, delta_time):
        self.hero_animation.update_animation()
        self.hero_animation.update()
        self.items_list.update()

        self.cloud_x += self.cloud_speed * self.cloud_direction

        if self.cloud_x > width + self.cloud_texture.width // 2:
            self.cloud_x = -self.cloud_texture.width // 2

        if self.hero_animation.is_jumping:
            self.hero_animation.change_y -= 450 * delta_time
            
        if self.move_right_enemy:
            self.Enemy_sprite2.center_x += self.moveXEnemy
            if self.Enemy_sprite2.center_x >= 860:  # Переключаемся на движение влево при достижении определенной позиции
                self.move_right_enemy = False
        else:
            self.Enemy_sprite2.center_x -= self.moveXEnemy
            if self.Enemy_sprite2.center_x <= 700:  # Переключаемся на движение вправо при достижении определенной позиции
                self.move_right_enemy = True

        # Проверяем столкновения героя с землей
        ground_hit_list = arcade.check_for_collision_with_list(self.hero_animation, self.ground_sprites)
        if ground_hit_list:
            ground_hit = ground_hit_list[0]  # Получаем первый объект столкновения
            self.hero_animation.is_jumping = False
            self.hero_animation.change_y = 0
            self.hero_animation.center_y = ground_hit.center_y + ground_hit.height // 2 + self.hero_animation.height // 2
            self.can_jump = True
        else:
            self.hero_animation.is_jumping = True

        self.hero_animation.center_x += self.hero_animation.change_x * delta_time
        self.hero_animation.center_y += self.hero_animation.change_y * delta_time

        if self.hero_animation.is_throwing and self.hero_animation.throw_frames == 0:
            self.throw_item()

        # Проверяем столкновение с яблоками
        if self.apple_sprite and arcade.check_for_collision(self.hero_animation, self.apple_sprite):
            if self.applecheck:
                self.apple_sprite.kill()
                self.apple_count += 1
                self.applecheck = False
        if self.apple2_sprite and arcade.check_for_collision(self.hero_animation, self.apple2_sprite):
            if self.applecheck2:
                self.apple2_sprite.kill()
                self.apple_count += 1
                self.applecheck2 = False

        # Проверяем столкновение между предметами и врагом
        for item in self.items_list:
            if arcade.check_for_collision(item, self.Enemy_sprite):
                self.Enemy_sprite.kill()
                self.killcheck = False
                item.kill()

            if arcade.check_for_collision(item, self.Enemy_sprite2):
                self.Enemy_sprite2.kill()
                self.killcheck = False
                item.kill()
        # Проверяем столкновение героя с врагом
        if self.killcheck and arcade.check_for_collision(self.hero_animation, self.Enemy_sprite):
            self.setup()  # Перезапуск уровня
        if self.killcheck and arcade.check_for_collision(self.hero_animation, self.Enemy_sprite2):
            self.setup()

        # Проверяем, умер ли герой
        if self.hero_animation.center_y < 0:
            self.setup()  # Перезапуск уровня

        # Проверяем столкновение с финальной текстурой
        if arcade.check_for_collision(self.hero_animation, self.final_sprite):
            self.background_music.stop(self.background_player)
            self.close()
            end.main(self.apple_count)



def main(apple_count=0):
    apple_count = 0
    window = MyGame(apple_count)
    arcade.run()

if __name__ == "__main__":
    main()
