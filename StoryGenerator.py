import random
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a type of food: ")
name = input("Enter a person's name: ")
story1 = f"""
Once upon a time, {name} went to {place}.
It was a very {adj} day. Suddenly, a {animal} 
appeared and {verb} right over a giant bowl of {food}.
The {noun} was never the same again.
"""
story2 = f"""
In the middle of {place}, {name} found a {adj} {noun}.
Without thinking, {name} {verb} as fast as possible.
A hungry {animal} watched while eating {food}.
It was truly a sight to behold.
"""
story3 = f"""
{name} always dreamed of visiting {place}.
When they finally arrived, they saw a {adj} {animal}.
The animal {verb} and then offered {name} some {food}.
"Keep the {noun}," the animal whispered.
"""
story4 = f"""
The legend of the {adj} {noun} started in {place}.
{name} was the only one brave enough to carry a {food}.
An ancient {animal} {verb} loudly to signal their arrival.
Everyone cheered for {name}!
"""
story5 = f"""
"Look at that {adj} {animal}!" yelled {name}.
They were standing in the center of {place}.
The {animal} {verb} and dropped a piece of {food}.
{name} picked it up and realized it was actually a {noun}.
"""
stories = [story1, story2, story3, story4, story5]
selected_story = random.choice(stories)
print("\n" + "="*25)
print(selected_story)
print("="*25)