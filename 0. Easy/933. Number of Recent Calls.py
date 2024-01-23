from collections import deque


class RecentCounter:
    def __init__(self) -> None:
        self.counter = 0
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.counter += 1

        while self.queue[0] < t - 3000:
            self.queue.popleft()
            self.counter -= 1

        return self.counter
