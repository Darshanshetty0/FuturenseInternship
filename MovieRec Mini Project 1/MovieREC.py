#MovieREC
import random
class MovieRecommendationSystem:
    def __init__(self):
        self.movies = []

    def add(self, title, genre):
        rating =random.randint(0,11)
        movie = {'title': title, 'genre': genre, 'rating': rating}
        self.movies.append(movie)
        print(f"Movie '{title}' added successfully!")

    def search_by_title(self, title):
        results = [movie for movie in self.movies if title.lower() in movie['title'].lower()]
        return results

    def search_by_genre(self, genre):
        results = [movie for movie in self.movies if genre.lower() in movie['genre'].lower()]
        return results

    def recommend(self, n):
        result = []
        for i in range (0,len(self.movies)):
            movie = self.movies[i]
            if(int(movie["rating"])>=int(n)):
                result.append(movie)
        return result

    def delete(self, title):
        self.movies = [movie for movie in self.movies if movie['title'].lower() != title.lower()]
        print(f"Movie '{title}' deleted successfully!")


def algo():
    answer = input("\nChoose an option:\n1.Add Movie\n2.Delete Movie\n3.Recommend Movie by rating\n4.Search Movie\n5.Exit\n:")
    
    match answer:
        case "1":
            title = input("Title: ")
            genre = input("Genre: ")
            system.add(title, genre)
            algo()
                
        case "2":
            title = input("Title: ")
            system.delete(title)
            algo()
             
        case "3":
            rating  = input("Rating: ")
            results = system.recommend(rating)
            print(results)
            algo()
                
        case "4":
            answer = input("\nChoose an option to Search:\n1.Search by Title\n2.Search by Genre\n:")
            
            match answer:
                case "1":
                    title = input("Title: ")
                    print(system.search_by_title(title))
                
                case "2":
                    genre = input("Genre: ")
                    print(system.search_by_genre(genre))
            
            algo()  
              
        case "5":
            print("-----Thank You-----")
# Example usage:
if __name__ == "__main__":
    system = MovieRecommendationSystem()
    system.add("Transformer","Sci-fi")
    system.add("Transporter","Action")
    system.add("The Bee Movie","Animation")
    system.add("Cars 3","Animation")
    system.add("IT","Horror")
    system.add("tT","Horror")
    
    algo()

