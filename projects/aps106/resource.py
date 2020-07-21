# Backgrounds
WHITE = "#FFFFFF"
SELECT = "#EBEFC9"
CONF = "#F98B8B"

BLACK = "#000000"
NUMS = "#0A3095"  # Permanent cell numbers
BACK = "#3F3F49"

FONTS = {
    55: ("Helvetica", "55", "bold"),
    30: ("Helvetica", "30", "bold"),
    25: ("Helvetica", "25", "bold"),
    20: ("Helvetica", "20", "bold"),
}


WIDTH = 1024
HEIGHT = 768


# Cell colors
RED = "#CB4335"
GREEN = "#229954"
BLUE = "#21618C"
YELLOW = "#F7DC6F"

HELP_TEXT = """

Welcome to this shitty game made by James Trew.

INSTRUCTIONS:

    A grid of cells colored red, blue, green, yellow is presented upon play.

    When a colored cell is selected, the selected cell and all neighboring cells sharing the same color are eliminated. The surrounding cells collapse down to remove the created gap. If an entire column have been eliminated, the immediate right column shifts in to fill the empty column. To eliminate cells, the selected cell must have at least one neighboring cell sharing the same color.

    The square of the number of cells remove adds to the total score.

    Once no more moves are possible, the game is over.

    For interactive play, simply left click the cell you'd like to eliminate.

    For computer play, press the spacebar to see the next move. The computer will play the move which will result in the highest score possible per move.

"""
