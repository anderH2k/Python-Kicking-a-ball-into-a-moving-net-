from graphics import *


class Game:
    def __init__(self, width, height):
        # Initializing the game window
        self.width = width
        self.height = height
        self.win = GraphWin("My Game", self.width, self.height)
        self.field = Image(Point(self.width / 2, self.height / 2), "football_field_1.png")
        self.field.draw(self.win)
        self.direction = 1
        self.ball_move = 0
        self.goal = 0
        self.life = 5
        self.highest_score = 0

        # Creating and displaying the score text
        self.score_text = Text(Point(self.width / 2, self.height / 2 + 100), "Your Score:" + str(self.goal))
        self.score_text.setTextColor("blue")
        self.score_text.setSize(30)
        self.score_text.setFace("times roman")
        self.score_text.setStyle("bold")
        self.score_text.draw(self.win)

        # Creating and displaying the highest score text
        self.highest_score_text = Text(Point(self.width / 2, self.height / 2 + 200), "Your Highest Score:" + str(self.highest_score))
        self.highest_score_text.setTextColor("blue")
        self.highest_score_text.setSize(30)
        self.highest_score_text.setFace("times roman")
        self.highest_score_text.setStyle("bold")
        self.highest_score_text.draw(self.win)

        # Creating and displaying the life text
        self.life_text = Text(Point(self.width / 2, self.height / 3), "Your Life:" + str(self.life))
        self.life_text.setTextColor("yellow")
        self.life_text.setSize(30)
        self.life_text.setFace("times roman")
        self.life_text.setStyle("bold")
        self.life_text.draw(self.win)

        # Creating the "GAME OVER!" text but don't display it yet until the life was gone
        self.game_over_text = Text(Point(self.width / 2, self.height / 2), "GAME OVER! ")
        self.game_over_text.setTextColor("red")
        self.game_over_text.setSize(35)
        self.game_over_text.setFace("times roman")
        self.game_over_text.setStyle("bold")

    def create_circle(self, x1, y1):
        # Creating and displaying the circle (ball)
        self.original_x = x1
        self.original_y = y1
        self.ball = Image(Point(x1, y1), 'football_1-removebg-preview.png')
        self.ball.draw(self.win)

    def create_net(self):
        # Creating and displaying the net
        self.net = Image(Point(self.width / 2, 60), 'net_1.png')
        self.net.draw(self.win)

    def move_net(self):
        # Moving the net back and forth
        if int(self.net.getAnchor().getX() + self.net.getWidth() / 2) == self.width:
            self.direction = -1

        if int(self.net.getAnchor().getX() - self.net.getWidth() / 2) == 0:
            self.direction = 1

        self.net.move(0.1 * self.direction, 0)

    def check_input(self):
        # If the "Up" key is pressed, the ball will move in the -y direction
        temp = self.win.checkKey()
        if temp == "Up":
            self.ball_move = -0.2

    def check_goal(self):
        # Checking if the ball enters the net
        if int(self.ball.getAnchor().getY()) == int(self.net.getAnchor().getY()):
            if int(self.ball.getAnchor().getX() >= self.net.getAnchor().getX() - self.net.getWidth() / 2) and int(
                    self.ball.getAnchor().getX() <= self.net.getAnchor().getX() + self.net.getWidth() / 2):
                # Increasing the goal count if the ball enters the net and reseting the ball's position
                self.goal += 1
                self.ball_move = 0
                self.score_text.setText(" Your Score: " + str(self.goal))
                self.ball.undraw()
                self.create_circle(self.original_x, self.original_y)
                if self.goal >= self.highest_score:
                    self.highest_score = self.goal
                    self.highest_score_text.setText(" Your Highest Score: " + str(self.highest_score))

        if self.ball.getAnchor().getY() <= 0:
            # Decreasing life count if the ball was not entered the net or out of the window and reseting the ball's position
            self.life -= 1
            self.goal = 0
            self.score_text.setText(" Your Score: " + str(self.goal))
            self.ball_move = 0
            self.life_text.setText("Your Life: " + str(self.life))
            self.ball.undraw()
            self.create_circle(self.original_x, self.original_y)

    def check_game_over(self):
        # Checking if the game is over (no more lives!!)
        if self.life == 0:
            self.game_over_text.draw(self.win)
            return True

    def move_circle(self):
        # Moving the ball vertically along the y direction
        self.ball.move(0, self.ball_move)

    def play(self):
        # Starting the game
        self.create_net()
        self.create_circle(self.width / 2, 580)

        while True:
            self.check_input()
            self.move_net()
            self.move_circle()
            self.check_goal()
            if self.check_game_over():
                break

        # Pressing the key "c" to close the window
        if self.win.getKey() == 'c':
            self.win.close()

if __name__ == "__main__":
    game = Game(550, 650)
    game.play()