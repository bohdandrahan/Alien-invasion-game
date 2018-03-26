class Settings():

    def  __init__(self):
        self.screen_width = 1200
        self.screen_hight = 800
        self.background = (101,155, 43)

        self.ship_speed_factor = 1.5

        self.ufo_speed_factor = 1
        self.ufo_speed_factor_drop = 10
        self.fleet_direction = 1
        
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 43, 75)
        self.bullets_max_num = 5

        self.star_speed_factor = 1.5
        self.star_prob = 0.5
        
    def get_screen_size(self):
        return (self.screen_width, self.screen_hight)

    def get_background(self):
        return self.background

    def get_ship_speed(self):
        return self.ship_speed_factor

    def get_ufo_speed(self):
        return self.ufo_speed_factor

    def get_ufo_speed_drop(self):
        return self.ufo_speed_factor_drop

    def get_fleet_direction(self):
        return self.fleet_direction

    def change_fleet_direction(self):
        self.fleet_direction *= -1

    def get_bullet_speed(self):
        return self.bullet_speed_factor

    def get_bullet_size(self):
        return (self.bullet_width, self.bullet_height)

    def get_bullet_color(self):
        return self.bullet_color

    def get_max_num_bullets(self):
        return self.bullets_max_num
    
    def get_star_speed(self):
        return self.star_speed_factor

    def get_star_prob(self):
        return self.star_prob

    
