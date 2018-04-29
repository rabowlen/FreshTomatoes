import fresh_tomatoes
import media

# Create various instances of Movies to display on the site.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://ia.media-imdb.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",  # noqa
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

its_a_wonderful_life = media.Movie("It's a Wonderful Life",
                        "A man gets a second chance at life",
                        "https://ia.media-imdb.com/images/M/MV5BZjc4NDZhZWMtNGEzYS00ZWU2LThlM2ItNTA0YzQ0OTExMTE2XkEyXkFqcGdeQXVyNjUwMzI2NzU@._V1_SY1000_CR0,0,687,1000_AL_.jpg",  # noqa
                        "https://youtu.be/cR7p-IB6INM")

avengers_aou = media.Movie("Avengers: Age of Ultron",
                        "The Avengers Faceoff Against a New Threat",
                        "https://ia.media-imdb.com/images/M/MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_SY1000_SX675_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=tmeOjFno6Do")

the_wedding_singer = media.Movie("The Wedding Singer",
                        "A Wedding Singer Learns to Appreciate the Small" +
                        "Things in Life.jpg",
                        "https://ia.media-imdb.com/images/M/MV5BYjM5YTQ0ZGYtMWExZi00MTFmLTg0YjUtZDcyMGNiYzE5MmNmL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # noqa
                        "https://youtu.be/_bhU3NsCIDs")

avengers_iw = media.Movie("Avengers: Infinity War",
                        "The Avengers Faceoff Against Thanos",
                        "https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

movies = [toy_story, avatar, its_a_wonderful_life, avengers_aou,
          the_wedding_singer, avengers_iw]
fresh_tomatoes.open_movies_page(movies)

