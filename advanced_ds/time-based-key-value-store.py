from collections import defaultdict

class TimeMap:

    def __init__(self):
        # with what i understand we're using a dict
        # maybe the question isn't descriptive
        self.map = defaultdict(lambda: ([], []))
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if not key:
        #     continue
        times, values = self.map[key]
        times.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str:

        if not key in self.map:
            return ""
        
        # array = self.map[key]

        times, values = self.map[key]


        position = bisect_right(times, timestamp)

        if position == 0:
            return ""

        return values[position - 1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)