'''
Import files so that their classes, functions,and fields
are available
'''
import media
import fresh_tomatoes

#creating a movie object stored as scarface
scarface = media.Movie("Scarface",
                       "After getting a green card in exchange for " +
                       "assassinating a Cuban government official, " +
                       "Tony Montana (Al Pacino) stakes a claim on " +
                       "the drug trade in Miami. Viciously murdering " +
                       "anyone who stands in his way, Tony eventually " +
                       "becomes the biggest drug lord in the state, " +
                       "controlling nearly all the cocaine that comes " +
                       "through Miami. But increased pressure from the " +
                       "police, wars with Colombian drug cartels and his " +
                       "own drug-fueled paranoia serve to fuel the flames " +
                       "of his eventual downfall.",
                       "https://upload.wikimedia.org/wikipedia/commons/2/28/" +
                       "Scarface_release_poster.jpg",
                       "https://www.youtube.com/watch?v=7pQQHnqBa2E")

#creating a movie object stored as american_gangster
american_gangster = media.Movie("American Gangster",
                                "Frank Lucas (Denzel Washington) earns " +
                                "his living as a chauffeur to one of " +
                                "Harlem's leading mobsters. After his " +
                                "boss dies, Frank uses his own ingenuity " +
                                "and strict business code to become one " +
                                "of the inner city's most powerful crime " +
                                "bosses. Meanwhile, veteran cop Richie " +
                                "Roberts (Russell Crowe) senses a change " +
                                "in the mob's power structure and looks " +
                                "for ways to bring his opponent to justice.",
                                "https://upload.wikimedia.org/wikipedia/" +
                                "commons/thumb/f/f9/Amgangty.jpg/256px-Amgangty.jpg",
                                "https://www.youtube.com/watch?v=BV_nssS6Zkg")

#creating a movie object stored as trainign_day
training_day = media.Movie("Training Day",
                           "Police drama about a veteran officer who " +
                           "escorts a rookie on his first day with the " +
                           "LAPD's tough inner-city narcotics unit. " +
                           "\"Training Day\" is a blistering action drama " +
                           "that asks the audience to decide what is " +
                           "necessary, what is heroic and what crosses " +
                           "the line in the harrowing gray zone of fighting " +
                           "urban crime. Does law-abiding law enforcement " +
                           "come at the expense of justice and public safety? " +
                           "If so, do we demand safe streets at any cost?",
                           "https://upload.wikimedia.org/wikipedia/commons/" +
                           "thumb/a/a4/Traing.jpg/512px-Traing.jpg",
                           "https://www.youtube.com/watch?v=DXPJqRtkDP0")

#creating a movie object stored as transporter
transporter = media.Movie("The Transporter",
                          "Ex-Special Forces operator Frank Martin " +
                          "(Jason Statham) lives what seems to be a " +
                          "quiet life along the French Mediterranean, " +
                          "hiring himself out as a mercenary transporter " +
                          "who moves goods - human or otherwise - from " +
                          "one place to another. No questions asked. " +
                          "Dangerous complications ensue when he is " +
                          "hired to kidnap the feisty daughter of a " +
                          "lethal Chinese crime lord who's smuggling " +
                          "his fellow countrymen into France.",
                          "https://upload.wikimedia.org/wikipedia/commons/d/d8/Tran15.jpg",
                          "https://www.youtube.com/watch?v=0poXFSvX0_4")

#creating a list of the movie objects
movies = [scarface, american_gangster, training_day, transporter]

'''
passing the list of movie objects to the open_movies_page function that's in
the fresh_tomatoes.py file
'''
fresh_tomatoes.open_movies_page(movies)

