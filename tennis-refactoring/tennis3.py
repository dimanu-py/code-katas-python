

class TennisGame:

    def __init__(self, player_one_name: str, player_two_name: str) -> None:
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.points_player_one = 0
        self.points_player_two = 0

    def won_point(self, name: str) -> None:
        if name == self.player_one_name:
            self.points_player_one += 1
        else:
            self.points_player_two += 1

    def score(self) -> str:
        if (self.points_player_one < 4 and self.points_player_two < 4) and (self.points_player_one + self.points_player_two < 6):
            points_name = ["Love", "Fifteen", "Thirty", "Forty"]
            score = points_name[self.points_player_one]
            return score + "-All" if (self.points_player_one == self.points_player_two) else score + "-" + points_name[self.points_player_two]
        elif self.points_player_one == self.points_player_two:
            return "Deuce"
        else:
            score = self.player_one_name if self.points_player_one > self.points_player_two else self.player_two_name
            return "Advantage " + score if ((self.points_player_one - self.points_player_two) * (self.points_player_one - self.points_player_two) == 1) else "Win for " + score