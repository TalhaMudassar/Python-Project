"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import os 
import json

FILENAME = 'movies.json'

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME,'r',encoding='utf-8')as file:
        return json.load(file)
    
def save_movies(movies):
    with open(FILENAME,'w',encoding='utf-8')as file:
        json.dump(movies,file,indent=2)  # json writing mode


def add_movie(movies):
    title = input("Plase enter the title of movie")
    if any(movie['title'].lower()==title for movie in movies): 
        print("Movie already exists")
        return
    genre = input("Genre: ".strip().lower())
    try:
        rating = float(input("Enter rating (o-10)"))
        if not (0 <= rating <= 10):
            raise ValueError("Please enter a valid number")
    except ValueError:
        print("please enter a valid number")
        return 
    
    new_movie = {"title": title, "genre": genre, "rating": rating}
    movies.append(new_movie)
    save_movies(movies)
    print(f" Movie '{title}' added successfully!")
    
    
def search_movies(movies):
    term = input("Enter the Title or genre ").strip().lower()
    results = []
    for movie in movies:
        if term in movie['title'].lower() or term in movie['genre'].lower():
            results.append(movie)

    if not results:
        print("Not matching result")
        return
    print(f"Found {len(results)} result(s)")
    
    for movie in results:
        print(f" {movie["title"]}  --  {movie["genre"]}  --  {movie["rating"]}")
        
    
def view_movie(movies):
    if not movies:
        print("No Movies in DB")
        return
    for movie in movies:
        print(f" {movie["title"]}  --  {movie["genre"]}  --  {movie["rating"]}")
        
    
    
            
def run_movie_db():
    movies = load_movies()
    
    while True:
        print("\n MOVIES-DB")
        print(" 1.Add a movie")
        print(" 2.View all movies")
        print(" 3.Search movies by title or genre")
        print(" 4.Exit the app")
        
        choice = input("PLEASE ENTER YOUR CHOICE")
        match choice:
            case "1": add_movie(movies)
            case "2": view_movie(movies)
            case "3": search_movies(movies)
            case "4": break
            case _: print("Enter Valid choice")
            
if __name__ == "__main__":
    run_movie_db()