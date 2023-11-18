from typing import List


class DataMemory:
    def __init__(self) -> None:
        self._storage: List[int] = [0] * 256

    def __getitem__(self, position: int) -> int:
        return self._storage[position]

    def __setitem__(self, position: int, value: int) -> None:
        self._storage[position] = value
