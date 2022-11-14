# https://leetcode.com/problems/time-based-key-value-store/
# https://linlaw0229.github.io/2021/04/28/981-Time-Based-Key-Value-Store/

class TimeMap:
    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        arr = self.dic[key]
        left, right = 0, len(arr)
        while left < right:
            mid = (left+ right) //2
            if arr[mid][0] > timestamp:
                right = mid
            else:
                left = mid+1
            
        return "" if right == 0 else arr[right-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)