
# tworzenie class (blueprint)
class User:
    # Contructor - tworzenie w nawiasie self oznacza że to jest odłwołanie do całej klasy, każda rzecz robiona z def musi mieć na starcie w () self
    # user_id/username to są atrybuty które przypisuje i później są wykorzystywane jako metody
    def __init__(self, user_id, username):
       self.id = user_id
       self.username = username
       self.followers = 0 # z defaultu wszyscy uzytkownicy beda mieć 0 followersów
       self.following = 0
    
    # Tworzenie metod class - tworzenie metody która dodaje followersów i follujących   
    def follow(self,user): 
        user.followers += 1 # tutaj dodanie że na swoim koncie ma 1 followersa
        self.following += 1

# stworzenie z class objectu
user_1 = User("001","jack")
user_2 = User("002","angela")

user_1.follow(user_2)

print('user1 followers', user_1.followers)
print('user1', user_1.following)

print('user2 followers', user_2.followers)
print('user2', user_2.following)


