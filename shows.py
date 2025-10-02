SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        # print(show.capitalize()) # Uppercase first letter of each word
        # print(show.title())  # Uppercase first letter of each word
        # print(show.strip())  # Remove leading/trailing whitespace
        # print(show.strip().title())  # Combine methods
        
        cleaned_shows.append(show.strip().title())
        
    print(', '.join(cleaned_shows))
        
main()