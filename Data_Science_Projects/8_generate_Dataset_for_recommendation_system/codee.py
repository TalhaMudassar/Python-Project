import pandas as pd


data = [
    {
        "title": "The Silent Forest",
        "author": "Jane Hill",
        "genre": "Mystery",
        "description": "A detective uncovers secrets hidden deep in the woods while chasing a serial killer."
    },
    {
        "title": "Spacebound",
        "author": "Rico Vega",
        "genre": "Science Fiction",
        "description": "An astronaut embarks on a mission to Mars but discovers an ancient alien presence."
    },
    {
        "title": "Dark Code",
        "author": "Nick Cipher",
        "genre": "Thriller",
        "description": "A cybersecurity expert is drawn into a global web of espionage and hidden messages."
    },
    {
        "title": "Fog Over London",
        "author": "Claire Black",
        "genre": "Mystery",
        "description": "Set in Victorian London, a private investigator unravels political conspiracies amid murders."
    },
    {
        "title": "Beneath the Waves",
        "author": "Diana Coast",
        "genre": "Adventure",
        "description": "An underwater archaeologist discovers an ancient city lost in the ocean."
    },
    {
        "title": "Love in Paris",
        "author": "Emily Rose",
        "genre": "Romance",
        "description": "A love story between a local baker and a traveler unfolds in the heart of Paris."
    },
    {
        "title": "The Glass Citadel",
        "author": "Arthur Stone",
        "genre": "Fantasy",
        "description": "A young sorceress must unite seven warring kingdoms before an ice age consumes the world."
    },
    {
        "title": "Echoes of the Past",
        "author": "Sarah Kline",
        "genre": "Historical Fiction",
        "description": "A family secret from World War II resurfaces, forcing a modern woman to confront her grandfather's hidden life."
    },
    {
        "title": "Zero Hour Protocol",
        "author": "Mark Delta",
        "genre": "Science Fiction",
        "description": "A team of scientists race against time to prevent a black hole from swallowing Earth's moon."
    },
    {
        "title": "Whispers in the Library",
        "author": "Eliza Reed",
        "genre": "Mystery",
        "description": "When a rare manuscript vanishes, a book restorer finds herself investigating a closed-circle of eccentric scholars."
    },
    {
        "title": "The Serpent's Heart",
        "author": "Liam Vance",
        "genre": "Adventure",
        "description": "Following an old map, a treasure hunter navigates the dense Amazon jungle in search of a mythical artifact."
    },
    {
        "title": "A Taste of Freedom",
        "author": "Julia Chen",
        "genre": "Contemporary",
        "description": "A chef leaves her high-stress restaurant job to open a small bakery, finding unexpected love and peace."
    },
    {
        "title": "Crimson Tide",
        "author": "Victor Hale",
        "genre": "Thriller",
        "description": "A political journalist uncovers a massive corporate conspiracy tied to a catastrophic oil spill."
    },
    {
        "title": "Beyond the Veil",
        "author": "Nadia Frost",
        "genre": "Paranormal",
        "description": "A skeptic is forced to believe in ghosts when a mischievous spirit attaches itself to her antique shop."
    },
    {
        "title": "Starship Nomad",
        "author": "Owen Kade",
        "genre": "Science Fiction",
        "description": "The last human alive pilots a battered starship across the galaxy, searching for a legendary new home."
    },
    {
        "title": "The Duke's Deception",
        "author": "Penelope Light",
        "genre": "Historical Romance",
        "description": "In 19th-century England, a governess discovers her employer, the Duke, is leading a double life."
    },
    {
        "title": "Mountain of Fire",
        "author": "Gael Cruz",
        "genre": "Adventure",
        "description": "An unlikely team of explorers must climb an active volcano to retrieve a sample vital to saving the planet."
    },
    {
        "title": "The Memory Thief",
        "author": "Alex Shaw",
        "genre": "Psychological Thriller",
        "description": "After a traumatic event, a man realizes someone is systematically stealing and altering his memories."
    },
    {
        "title": "Clockwork Dreams",
        "author": "Maxine Gears",
        "genre": "Steampunk",
        "description": "A brilliant but reclusive inventor builds an automaton to impersonate him, only for the machine to develop its own sentience."
    },
    {
        "title": "Summer by the Coast",
        "author": "Tessa Blue",
        "genre": "Romance",
        "description": "A woman returns to her childhood beach town to sell her family home and falls for the town's charming lighthouse keeper."
    }
]


df = pd.DataFrame(data)
df.to_csv("book_csv",index=False)
print("Book dataset created")
