import sys
class TempTracker:
    def __init__(self):
        self.tempratures = []
        print(sys.maxsize)
        print(-sys.maxsize-1)
        self.max = -sys.maxsize - 1
        self.min = sys.maxsize
        self.mean = None
        self.mode = None
        self.sum = 0
        self.count = 0
        self.occurences = {}
        self.max_occurrences = 0

    def insert(self, temprature):
        self.tempratures.append(temprature)
        self.sum += temprature
        self.count += 1
        self.mean = self.sum / self.count
        if temprature > self.max:
            self.max = temprature

        if temprature < self.min:
            self.min = temprature

        self.occurences[temprature] = self.occurences.get(temprature,0) + 1
        if self.occurences[temprature] > self.max_occurrences:
            self.max_occurrences = self.occurences[temprature]
            self.mode = temprature

    def get_max(self):
        return self.max

    def get_mean(self):
        return self.mean

    def get_min(self):
        return self.min

    def get_mode(self):
        return self.mode

if __name__ == "__main__":
    tempTracker = TempTracker()
    print(tempTracker.insert(5))