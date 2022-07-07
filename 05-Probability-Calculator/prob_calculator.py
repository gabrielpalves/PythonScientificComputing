import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, number):
        old_list = self.contents
        deleted = []
        
        if number > len(old_list):
            deleted = old_list
            old_list = []
        else:
            deleted = random.sample(old_list,number)
            for i in deleted:
                old_list.remove(i)

        self.contents = old_list
        return deleted


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    if num_balls_drawn >= len(hat.contents):
        balls = hat.contents
        M = num_experiments
        for i in expected_balls:
            if balls.count(i) < expected_balls[i]:
                M = 0
                break
    else:
        for _ in range(num_experiments):
            balls = random.sample(hat.contents, num_balls_drawn)

            M = M + 1
            for i in expected_balls:
                if balls.count(i) < expected_balls[i]:
                    M = M - 1
                    break
    
    return M/num_experiments