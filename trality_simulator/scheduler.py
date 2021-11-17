state = []
dataMap = {}


def schedule(interval, symbol):
    def scheduler(func):
        return func(state, dataMap)

    return scheduler
