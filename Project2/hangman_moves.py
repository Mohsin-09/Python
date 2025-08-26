class HangmanMoves:
    def __init__(self):
        self.stages = [
            """
              -----
              |   |
                  |
                  |
                  |
                  |
                  ______|______
            """,
            """
              -----
              |   |
              O   |
                  |
                  |
                  |
                  ______|______
            """,
            """
              -----
              |   |
              O   |
              |   |
                  |
                  |
                  ______|______
            """,
            """
              -----
              |   |
              O   |
             /|   |
                  |
                  |
                  ______|______
            """,
            """
              -----
              |   |
              O   |
             /|\  |
                  |
                  |
                  ______|______
            """,
            """
              -----
              |   |
              O   |
             /|\  |
             /    |
                  |
                  ______|______
            """,
            """
              -----
              |   |
              O   |
             /|\  |
             / \  |
                  |
                  ______|______
            """
        ]

    def get_stage(self, incorrect_guesses):
        return self.stages[min(incorrect_guesses, len(self.stages) - 1)]
