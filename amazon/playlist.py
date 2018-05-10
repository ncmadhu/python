#Author: Madhu Chakravarthy
#Date: 09-08-2018
def playlist(songs, currentSong, nextSong):
    length = len(songs)

    movesDown = 0
    currSong = currentSong
    nxtSong = nextSong
    while currSong != nxtSong:
        currSong = (currSong + 1) % length
        movesDown += 1

    movesUp = 0
    while currentSong != nextSong:
        currentSong = (currentSong - 1) % length
        movesUp += 1

    return min(movesDown, movesUp)



if __name__ == "__main__":
    songs = ["money", "wishyouwerehere", "welcome", "time"]
    print playlist(songs, 2, 3)
    songs = ["money", "wishyouwerehere", "welcome", "time"]
    print playlist(songs, 2, 1)
    songs = ["money", "wishyouwerehere", "welcome", "time"]
    print playlist(songs, 3, 0)

