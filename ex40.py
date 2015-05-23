class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

chanson = ["C est une chanson de test qui",
            "chie des bulles"]


happy_bday = Song(["Happy birthday to you",
                    "I dont want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

chanson_pipo = Song(["Je change une chanson pipo",
                    "pour faire un exercice"])

chanson_de_test = Song(chanson)




happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

chanson_pipo.sing_me_a_song()

chanson_de_test.sing_me_a_song()
