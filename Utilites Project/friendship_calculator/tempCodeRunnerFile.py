"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0

    
    shared_letters = set(name1) & set(name2)
    vowels = set("aeiou")

    score += len(shared_letters) * 8
    score += len(shared_letters & vowels) * 15

    
    if name1[0] == name2[0]:
        score += 20

    # Bonus based on length similarity (closer lengths = higher score)
    length_diff = abs(len(name1) - len(name2))
    score += max(0, 20 - length_diff * 2)  # max 20 points

    # Keep in range 0–100
    return min(score, 100)



def run_friendship_calculator():
    print("💫 Friendship Compatibility Calculator 💫")
    
 
    name1 = input("Enter first friend's name: ")
    name2 = input("Enter second friend's name: ")

    score = friendship_score(name1, name2)
    

    print(f"\nYour Friendship Score: {score}% 🎯")
    
    if score <= 30:
        print("😬 You two might clash a lot. Opposites can be fun, but it’ll take effort!")
    elif 31 <= score <= 50:
        print("🙂 There’s some common ground. A little patience can strengthen your bond.")
    elif 51 <= score <= 75:
        print("🤝 You share a solid connection. Keep supporting each other—it works!")
    else:  # 76–100
        print("🌟 You’re like chai and samosa—absolutely made for each other!")



run_friendship_calculator()
