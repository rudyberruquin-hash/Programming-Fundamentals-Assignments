"""
Author: Rudy Berruquin
Date September 24, 2026
Assignment: Personal Expense Tracker (Week 4)
Tier level: Base Level
Description: This is a Movie Collection Manager. The program stores, displays and analyzes a personal library of movies.

Test Cases:
1. Display pre-loaded collection: 
    All 5 movies displayed with genres joined by "/"
2. Add movie "Toy Story" with geners: 
    Successfully added and displayed
3. Sorted by year:
    Movies appear in chronological order, oldest at the top
4. Retrieved highest rated movies:
    Using find_top_rated(movies, 3) returned 3 highest rated movies in descending order
5. Retrieve average rating:
    Using get_average_rating() calculate average
"""

# First function: Create a movie dictionary
def create_movie(title, year, generes, rating):
    """
    This function will create and return a movie dictionary with the specified attributes.

    Parameters:
        title (str): The movie title
        year (int): The release year
        generes (list): List of genres
        rating (float): The movie rating

    Returns:
        dict: Dictionary containing movie data
    """
    return {
        "title": title,
        "year": year,
        "genres": generes,
        "rating": rating,
    }

# Second function: Display all movies in a table
def display_movies(movies, heading):

    """
    Parameters:
    movies(list): List of movies in dictionary
    heading(str): The heading title displayed above table
    """
    print(f"\n{heading}")
    print("="*70)

    # If list is empty print
    if len(movies) == 0:
        print("No movies in this collection.")
        return

    # Loop through each movie and give information
    for movie in movies:
        # Join genres list into a single str with "/" seperator
        genres_string = "/".join(movie["genres"])

        # Print formatted movie information using f-string
        print(f"{movie['title']:<30}{movie['year']:<6}{genres_string:<25}{movie['rating']}")

# Third function: Find the top rated movie
def find_top_rated(movies, n):
    """
    Returns a new list containing the top movies by rating

    Parameters:
        movies(list): List of movie dictionaries
        n(int): Number of the top movies to return

    Returns:
        list: A new list with the top rated movies
    """
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return sorted_movies[:n]

# Forth function: Calculate average rating
def get_average_rating(movies):

    """
    Calculates the averagee rating across all movies.

    Parameters:
        movies(list): List of movie dictionary

    Retruns:
        The average rating as a float (returns 0.0 if list is empty)
    """
    # If the list is empty
    if len(movies) == 0:
        return 0.0
    # Use a for loop and accumulator variables to sum ratings
    total_rating = 0.0
    for movie in movies:
        total_rating += movie["rating"]
    # Calculate average to two decimal places
    average = total_rating/len(movies)

    return average

# Main program
def main():
    """
    Main program that manages the movie collection
    """
    # Step 1: define the five-movie starter list
    movies = [
        {
                    "title": "Resident Evil",
                    "year": 2026,
                    "genres": ["Horror", "Sci-Fi"],
                    "rating": 7.7,
                },
                {
                    "title": "Hereditary",
                    "year": 2018,
                    "genres": ["Horror", "Thriller"],
                    "rating": 8.1,
                },
                {
                    "title": "Klaus",
                    "year": 2019,
                    "genres": ["Comedy", "Family"],
                    "rating": 7.5,
                },
                {
                    "title": "The Pursuit of Happyness",
                    "year": 2006,
                    "genres": ["Drama"],
                    "rating": 8.3,
                },
                {
                    "title": "Eight Crazy Nights",
                    "year": 2002,
                    "genres": ["Comedy", "Musical"],
                    "rating": 6.2,
                },
    ]

    # Step 2: Display the collection as loaded
    display_movies(movies, "Movie library")

    # Step 3: Ask user to add a new movie
    print("\n" + "="*70)
    print("Add a new movie")
    print("="*70)

    # Get movie title
    new_title = input("Enter the movies title: ").strip()

    # Get movie release year(converted to interger)
    new_year = int(input("Enter the release year: ").strip())

    # Get genere
    genres_input = input("Enter genres (seperate with commas: ").strip()

    # Split by comma and strip from each genre
    new_genres = [genre.strip() for genre in genres_input.split(",")]

    # Get rating (converted to float)
    new_rating = float(input("Enter the rating: ").strip())

    #Create the new movie anddictionary and append to the list
    new_movie = create_movie(new_title, new_year, new_genres, new_rating)
    movies.append(new_movie)

    print(f"\n'{new_title}' had ben added to you collection!")

    # Step 4: Sort movies by year and display
    movies.sort(key=lambda movie: movie["year"])
    display_movies(movies, "All movies sorted by year")

    # Step 5: Display top 3 rated movies
    top_three = find_top_rated(movies, 3)
    display_movies(top_three, "Top 3 rated movies")

    # Step 6: Calculate and display average rating
    average_rating = get_average_rating(movies)
    print(f"\nCollection average rating:{average_rating:.2f}")

    print("\n"+"="*60)
    print("Thank you for using the Movie Collection Manager!")
    print("="*60)

# Run the main program
if __name__ == "__main__":
    main()