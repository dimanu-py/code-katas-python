

class TennisGame:

    def __init__(self, player_one_name: str, player_two_name: str) -> None:
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.points_player_one = 0
        self.points_player_two = 0

    def won_point(self, n):
        if n == "player1":
            self.points_player_one += 1
        else:
            self.points_player_two += 1

    def score(self):
        if (self.points_player_one < 4 and self.points_player_two < 4) and (self.points_player_one + self.points_player_two < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.points_player_one]
            return s + "-All" if (self.points_player_one == self.points_player_two) else s + "-" + p[self.points_player_two]
        else:
            if (self.points_player_one == self.points_player_two):
                return "Deuce"
            s = self.player_one_name if self.points_player_one > self.points_player_two else self.player_two_name
            return "Advantage " + s if ((self.points_player_one - self.points_player_two) * (self.points_player_one - self.points_player_two) == 1) else "Win for " + s