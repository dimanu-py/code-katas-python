MINIMUM_DEUCE_POINTS = 4
POINT = 1


class TennisGame1:

    def __init__(self, player_one_name: str, player_two_name: str) -> None:
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_score = 0
        self.player_two_score = 0

    def won_point(self, player_name: str) -> None:
        if player_name == self.player_one_name:
            self.player_one_score += POINT
        else:
            self.player_two_score += POINT

    def score(self) -> str:
        score = ""

        if self.player_one_score == self.player_two_score:
            score = self.get_tied_score()
        elif self.player_one_score >= MINIMUM_DEUCE_POINTS or self.player_two_score >= MINIMUM_DEUCE_POINTS:
            score = self.get_break_point_score(score)
        else:
            for i in range(1,3):
                if i == 1:
                    temp_score = self.player_one_score
                else:
                    score+="-"
                    temp_score = self.player_two_score
                score += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[temp_score]
        return score

    def get_break_point_score(self, score: str) -> str:
        score_difference = self.player_one_score - self.player_two_score
        if score_difference == 1:
            score = f"Advantage {self.player_one_name}"
        elif score_difference == -1:
            score = f"Advantage {self.player_two_name}"
        elif score_difference >= 2:
            score = f"Win for {self.player_one_name}"
        else:
            score = f"Win for {self.player_two_name}"
        return score

    def get_tied_score(self) -> str:

        score = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }

        return score.get(self.player_one_score, "Deuce")