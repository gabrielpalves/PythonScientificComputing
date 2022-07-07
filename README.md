# PythonScientificComputing
Projects of Scientific Computing with Python course from FreeCodeCamp.

A total of 5 projects were developed. Use 'main.py' to run each project.

## Project 1: Arithmetic Formatter
A function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side

## Project 2: Time Calculator
A function named add_time that takes in two required parameters and one optional parameter:

- a start time in the 12-hour clock format (ending in AM or PM)
- a duration time that indicates the number of hours and minutes
- (optional) a starting day of the week, case insensitive

The function adds the duration time to the start time and return the result. Ex:
```
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

## Project 3: Budget App
A class Category in budget.py that instantiates objects based on different budget categories like food, clothing, and entertainment.

When the budget object is printed it displays:

- A title line of 30 characters where the name of the category is centered in a line of * characters.
- A list of the items in the ledger. Each line shows the description and amount. The first 23 characters of the description are displayed, then the amount. The amount is right aligned, contains two decimal places, and displays a maximum of 7 characters.
- A line displaying the category total.

Here is an example of the output:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the Category class, a function called create_spend_chart takes a list of categories as an argument. It returns a string that is a bar chart.

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Project 4: Polygon Area Calculator
A rectangle and a square class that can return area, perimeter, diagonal, the amount of squares or rectangles inside a shape and a picture made with asterisk. The objects height and width (or side for the square) can be modified. See the example below:
```
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

That code returns:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

## Project 5: Probability Calculator
A program that determines the approximate probability of drawing certain balls randomly from a hat. Instead of using mathematics to calculate the probability, the project consisted in writing a program to perform a large number of experiments to estimate an approximate probability. Example:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```
Since this is based on random draws, the probability will be slightly different each time the code is run.
