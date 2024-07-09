# Game intro
print('''
                                    /\\
                                   /  \\
                                  |    |
                                --:''\':'':--
                                  :'_' :
                                  _:"":\\___
                   ' '      ____.' :::     '._
                  . *=====<<=)           \\    :
                   .  '      '-'-'\\_      /'._.'
                                    \\====:_ ""
                                   .'     \\\\
                                  :       :
                                 /   :    \\
                                :   .      '.
                ,. _            :  : :      :
             '-'    ).          :__:-:__.;--'
           (        '  )        '-'   '-'
        ( -   .00.   - _
       (    .'  _ )     )
       '-  ()_.\\,\\,   -
''')

print("\nTHE MAGICAL MYSTERY OF HOGWARTS\n")

print(
    "You're a brave young witch or wizard, who's discovered an ancient secret hidden within the castle walls."
)
print(
    "Your mission is to make important choices, to save Hogwarts from an impending disaster.\n"
)

# Game start
print("GAME STARTS\n")
print(
    "You find yourself in the Hogwarts library, late at night, when you stumble upon"
)
print(
    "an old, dusty book that mentions a hidden room filled with powerful artifacts.\n"
)

print("""
What do you do?
1. Investigate the hidden room alone.
2. Ask Hermione for help.
3. Inform Professor McGonagall.
""")

choice1 = input("What do you choose? Type only 1, 2 or 3: ")

if (choice1 == "1"):
    print("""
You decide to brave the adventure on your own.
You follow the book's clues, which lead you to
a mysterious, dark corridor.
  """)
    print("""
What do you do?
1. Light your wand with Lumos.
2. Proceed without light, trusting your instincts.
  """)
    choice2 = input("What do you choose? Type only 1 or 2: ")
    if (choice2 == "1"):
        print("""
There is a corridor filled with cobwebs.
At the end is a door. You open it.
Inside you find the Mirror of Erised.
In the mirror you see yourself as Quidditch Captain, holding a trophy.
""")
        print("GAME OVER!")
    else:
        print("\nYou don't see the hole and fall into it. You die.\n")
        print("GAME OVER!")
elif (choice1 == "2"):
    print("""
Hermione uses a spell on the book that reveals a hidden map of Hogwarts with a marked location.
You and Hermione decide to follow it to the marked location.
When you get to the location, there are 2 doors.
  """)
    print("""
Which do you enter?
1. The door on the left.
2. The door on the right.
  """)
    choice3 = input("Which door do you choose: Type only enter 1 or 2: ")
    if (choice3 == "1"):
        print("""
You enter the left door where you are surprised by Fluffy! You die.
  """)
        print("GAME OVER!")
    else:
        print("""
You enter the door on the right.
It's pitch black inside.
Suddenly there is a roar of celebration.
All your friends arranged a surprise birthday party for you.
There were no artifacts, but you feel lucky to have such wonderful friends!
  """)
else:
    print("""
You decide to inform Professor McGonagall.
She takes the book and sends you to bed.
You were in the library after curfew.
5 Points deducted from Griffindor.\n
GAME OVER!
  """)
