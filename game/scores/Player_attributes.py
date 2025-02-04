class Player_attributes:
    def __init__(self, player, difficulty):
        """
            initialize all current player attribute for the game's course
        """
        self.player = player
        self.multiplicator = difficulty
        self.score = 0
        self.combo = 0
        self.played_key = ''
        self.last_key = ''
        self.strike = 0
        self.frozen_delay = 0
        self.slashed = 0
        self.invicibility = 0
    
    def life_down(self, life, mistake, frame=0):
        """
            lower the player's life based on events
        """
        if mistake == 'dropped':
            if frame - self.invicibility > self.multiplicator*20:
                self.strike += 1
                self.invicibility = frame
        elif mistake == 'bomb':
            self.strike = life
    
    def is_alive(self, life):
        """
            return a boolean to check the player's life state
        """
        life_count = life - self.strike
        if life_count > 0:
            return True
        else:
            return False
    
    def add_score(self):
        """
            add score to the player's based on their current combo
        """
        if self.played_key == self.last_key:
            if self.combo <= 2:
                self.score += 2 * self.multiplicator
                self.combo += 1
            elif self.combo <= 5:
                self.score += round(self.combo*0.8) * self.multiplicator
                self.combo +=1
            else:
                self.score += 3 * self.multiplicator
                self.combo +=1
        else :
            self.score += 1 * self.multiplicator
            self.combo = 0
        self.slashed += 1
        self.last_key = self.played_key

    def frozen_up(self):
        """
            update the player's frozen delay up or down based on events
        """
        if self.is_frozen():
            self.frozen_delay -=1
        else:
            self.frozen_delay = 180
    
    def is_frozen(self):
        """
            return a boolean based on the player's frozen state
        """
        if self.frozen_delay > 0:
            return True
        else:
            return False