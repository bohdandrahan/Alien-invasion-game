class GameStats():
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = False
        self.hi_score = 0

    def reset_stats(self):
        self.ships_left = self.game_settings.get_ship_limit()

        self.score = 0

    def lost_life(self):
        self.ships_left -= 1

    def get_ships_left(self):
        return self.ships_left
    
    def activate_game(self):
        self.game_active = True
    
    def disactive_game(self):
        self.game_active = False

    def get_score(self):
        return self.score

    def get_hi_score(self):
        return self.hi_score

    def add_points(self, points):
        self.score += points

    def check_and_update_hi_score(self):
        if self.get_score() > self.get_hi_score():
            self.hi_score = int(self.score)
        

        