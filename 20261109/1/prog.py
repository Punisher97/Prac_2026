class Omnibus:
    _counts = {}

    def __init__(self):
        self.__dict__["_names"] = set()

    def __setattr__(self, name, value):
        if name not in self._names:
            self._names.add(name)
            self._counts[name] = self._counts.get(name, 0) + 1

    def __getattr__(self, name):
        return self._counts.get(name, 0)

    def __delattr__(self, name):
        if name in self._names:
            self._names.remove(name)
            self._counts[name] -= 1

    def __del__(self):
        for name in self._names:
            self._counts[name] -= 1


if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())
