# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#Function that takes a single movie and returns True if its IMDB score is above 5.5
def imdbsingle(movies):
    for x in movies:
        if x["imdb"] > 5.5:
            print(x["name"], ":",True)
        else:
            print(x["name"], ":",False)

#imdbsingle(movies)

#Function that returns a sublist of movies with an IMDB score above 5.5.

def subimdb(movies):
    imdbmovies = []
    for x in movies:
        if x["imdb"] > 5.5:
            imdbmovies.append(x["name"])
    print(imdbmovies)

#subimdb(movies)

#Write a function that takes a category name and returns just those movies under that category.

def categories(category_name):
    for x in movies:
        if(x["category"] == category_name):
            print(x["name"])
#category_name = str(input("Ask for category(Thriller, Action, Adventure, Drama, Romance, Crime, War, Comedy, Suspense): "))

#categories(category_name)

#Write a function that takes a list of movies and computes the average IMDB score.

def averimdb(movies):
    sumofimdb = 0
    for i in movies:
        sumofimdb += i["imdb"]
    return sumofimdb / len(movies)

#print(averimdb(movies))

#Write a function that takes a category and computes the average IMDB score.


def categories2(category_name):
    films = []
    sumofimdb = 0
    for x in movies:
        if(x["category"] == category_name):
            films.append(x["name"])
            sumofimdb += x["imdb"]
    return sumofimdb / len(films)

#category_name = str(input("Ask for category(Thriller, Action, Adventure, Drama, Romance, Crime, War, Comedy, Suspense): "))
#print(categories2(category_name))

