BurgerNumber = sprites.create(img("""
        . . . . c c c b b b b b . . . . 
            . . c c b 4 4 4 4 4 4 b b b . . 
            . c c 4 4 4 4 4 5 4 4 4 4 b c . 
            . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
            e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
            e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
            e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
            . e b 4 4 4 4 4 5 4 4 4 4 b e . 
            8 7 e e b 4 4 4 4 4 4 b e e 6 8 
            8 7 2 e e e e e e e e e e 2 7 8 
            e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
            e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
            e b e 8 8 c c 8 8 c c c 8 e b e 
            e e b e c c e e e e e c e b e e 
            . e e b b 4 4 4 4 4 4 4 4 e e . 
            . . . c c c c c e e e e e . . .
    """),
    SpriteKind.player)
game.splash("Enter any number", "between 1 and 100")
number = game.ask_for_number("Your number:", 100)
if number >= 1 and number <= 100:
    if number % 3 == number % 5:
        BurgerNumber.say_text("FizzBuzz")
    elif number % 3 == 0:
        BurgerNumber.say_text("Fizz")
    elif number % 5 == 0:
        BurgerNumber.say_text("Buzz")
    else:
        BurgerNumber.say_text(number)
else:
    game.splash("Number not between 1 and 100")