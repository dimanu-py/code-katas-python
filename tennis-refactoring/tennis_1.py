MINIMUM_DEUCE_POINTS = 4
POINT = 1


class TennisGame1:

    STANDARD_SCORE = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    TIED_SCORE = {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
    }

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

        if self.is_deuce():
            return self.get_tied_score()
        elif self.is_advantage():
            return self.get_break_point_score()
        return self.get_score_during_game()

    def is_advantage(self) -> bool:
        return self.player_one_score >= MINIMUM_DEUCE_POINTS or self.player_two_score >= MINIMUM_DEUCE_POINTS

    def is_deuce(self) -> bool:
        return self.player_one_score == self.player_two_score

    def get_score_during_game(self) -> str:

        score_player_one = self.score_to_string(self.player_one_score)
        score_player_two = self.score_to_string(self.player_two_score)
        return f"{score_player_one}-{score_player_two}"

    def score_to_string(self, temp_score: int) -> str:
        return self.STANDARD_SCORE[temp_score]

    def get_break_point_score(self) -> str:

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
        return self.TIED_SCORE.get(self.player_one_score, "Deuce")