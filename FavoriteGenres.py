from collections import defaultdict


class solution:
    def __init__(self,genres):
        self.dict = defaultdict(str)
        for genre,songs in genres.items():
            for song in songs:
                self.dict[song] = genre
        #print(self.dict)


    def FindFavorite(self,userSongs):
        res = {}
        for user,songs in userSongs.items():
            genreCount = defaultdict(int)
            for song in songs:
                genreCount[self.dict[song]] += 1
            highest = max(genreCount.values())
            res[user] = [genre for genre,num in genreCount.items() if num == highest]
        return res

userSongs = {
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
}
songGenres = {}

sol = solution(songGenres)
print(sol.FindFavorite(userSongs))

