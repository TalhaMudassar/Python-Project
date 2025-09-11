"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

import textwrap


name = input("Enter your name ").strip()
profession = input("Enter your profession ").strip() 
passion = input("Enter your passion ").strip()
emoji = input("Enter emoji ").strip()
website = input("Enter your webiste ").strip()

print("\n Choose your style")
print("1.Simple lines ")
print("2.Vertical Flares")
print("3.Emoji sandwich")


while True:
    style = input("Enter 1, 2 or 3: ").strip()
    if style in ["1", "2", "3"]:
        print(f"You selected: {style}")
        break   # exit loop if input is valid
    else:
        print("Invalid choice! Please enter only 1, 2, or 3.")



def generater_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n💡 {passion}\n {website}"
    elif style == "2":
        return f"{emoji} {name}\n {profession}🔥\n {passion} \n {website}🔥"
    elif style == "3":
        return f"{emoji*3}\n {name} - {profession}\n {passion}\n {website} \n {emoji*3}"


bio = generater_bio(style)


print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)


option = input("YOU WANT TO SAVE YOU BIO IN TEXT FILE (y/n)").lower().strip()

if option == 'y':
    file_name = f"{name.lower().replace(' ','_')}_bio.txt"
    with open(file_name,'w',encoding="utf8") as f:
        f.write(bio)
    print("file saved")
        
else:
    print("CODE COMPLETED .... Thanks🙂")
