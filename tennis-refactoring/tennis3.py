POINTS_NAME = ["Love", "Fifteen", "Thirty", "Forty"]


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
            score = POINTS_NAME[self.points_player_one]
            return f"{score}-All" if self.is_deuce() else f"{score}-{POINTS_NAME[self.points_player_two]}"
        elif self.is_deuce():
            return "Deuce"
        else:
            return self.break_point()

    def is_deuce(self) -> bool:
        return self.points_player_one == self.points_player_two

    def break_point(self) -> str:
        headed_player = self.player_one_name if self.points_player_one > self.points_player_two else self.player_two_name
        return "Advantage " + headed_player if self.is_advantage() else "Win for " + headed_player

    def is_advantage(self) -> bool:
        return abs(self.points_player_one - self.points_player_two) == 1