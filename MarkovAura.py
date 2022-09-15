from distutils.log import fatal
from turtle import Turtle
from turtle import Screen
import numpy as np

class MarkovAura:
    
    def __init__(self, transition_matrix):
        """
        Generates a visual aura that relies on a Markov Chain
        Args: transition_matrix (dict) = transition probabilities for the Markov Chain
        """
        self.transition_matrix = transition_matrix
        self.moods = list(transition_matrix.keys())
        

    def get_next_mood(self, current_mood):
        """
        Decides the next mood based on the current mood and weather
        Args: current_mood (int) = the current mood
        """
        return np.random.choice(self.moods, p = [self.transition_matrix[current_mood][next_mood] for next_mood in self.moods])

    def compose_aura(self, current_mood = "yellow", count = 30):
        """Generates a sequence of moods for aura visual.
        Args: current_mood (int) = current mood level
              count (int) = number of moods, or number of days in a month
        """
        aura_sequence = []
        aura_sequence.append(current_mood)
        while len(aura_sequence) < count:
            next_mood = self.get_next_mood(current_mood)
            aura_sequence.append(next_mood)
            current_mood = next_mood
        
        return aura_sequence

    def generate_visual(self, aura_sequence):
        #initialize turtle
        t = Turtle()
        t.speed('fastest')
        window = Screen()
        window.colormode(255)
        window.setup(700, 700)
        window.bgcolor("black")
        t.hideturtle()
        t.penup()
        factor = 10
        radius = factor
        index = 0
        last_mood = ""
        current_mood = ""
        for mood in aura_sequence:
            if index == 0:
                last_mood = mood
                index += 1
            else:
                current_mood = mood
                t.home()
                t.right(90) #Face south
                t.forward(radius) #increment radius
                t.right(270)
                t.pendown()
                self.draw(t, factor, radius, last_mood, current_mood)
                t.penup()
                last_mood = current_mood
                radius += factor
                index += 1
            
    def draw(self, t, factor, radius, color1, color2):
        print(color1, color2)
        
        colorCodes = {"yellow": [247, 247, 73],
                    "orange": [237, 139, 0],
                    "red": [237, 29, 36],
                    "purple": [128, 49, 167],
                    "blue": [46, 103, 248],
                    "green": [48, 183, 0],
                    "white": [242, 233, 234],
                    "gray": [190, 195, 198]}
        
        code1 = colorCodes[color1]
        code2 = colorCodes[color2]
        i = radius - factor;
        gradient = 1
        while i < radius:
            r = code1[0] + (code2[0]-code1[0])*gradient//factor
            g = code1[1] + (code2[1]-code1[1])*gradient//factor
            b = code1[2] + (code2[2]-code1[2])*gradient//factor
            t.color(r, g, b)
            t.right(90)
            t.forward(1)
            t.right(270)
            t.pensize(4)
            t.pendown()
            t.circle(i)
            t.penup()
            i += 1
            gradient += 1

        
def main():
    aura_maker = MarkovAura({
        "yellow": {"yellow": 0, "orange": 0.25, "red": 0.025, "purple": 0.25, "blue": 0.1, "green": 0.25, "white": 0.1, "gray": 0.025},
        "orange": {"yellow": 0.25, "orange": 0, "red": 0.025, "purple": 0.1, "blue": 0.25, "green": 0.25, "white": 0.1, "gray": 0.025},
        "red": {"yellow": 0.1, "orange": 0.1, "red": 0, "purple": 0.05, "blue": 0.15, "green": 0.25, "white": 0.15, "gray": 0.2},
        "purple": {"yellow": 0.2, "orange": 0.15, "red": 0.025, "purple": 0, "blue": 0.3, "green": 0.2, "white": 0.1, "gray": 0.025},
        "blue": {"yellow": 0.15, "orange": 0.1, "red": 0.025, "purple": 0.25, "blue": 0, "green": 0.2, "white": 0.25, "gray": 0.025},
        "green": {"yellow": 0.25, "orange": 0.2, "red": 0.04, "purple": 0.25, "blue": 0.15, "green": 0, "white": 0.1, "gray": 0.01},
        "white": {"yellow": 0.2, "orange": 0.15, "red": 0, "purple": 0.1, "blue": 0.25, "green": 0.3, "white": 0, "gray": 0},
        "gray": {"yellow": 0.05, "orange": 0.1, "red": 0.3, "purple": 0.1, "blue": 0.2, "green": 0.1, "white": 0.15, "gray": 0}
    })
    #run visual
    new_aura = aura_maker.compose_aura(current_mood="yellow", count=30)
    aura_maker.generate_visual(new_aura)

if __name__ == "__main__":
    main()

