

def makeScheduler():
    ''' define interval, symbol and number of cadles available '''
    handler = []
    def schedule(interval, symbol, window_size=100):
        def handlers(fn):
            handler.append(
                {
                    'name': fn.__name__,
                    'fn': fn,
                    'interval': interval,
                    'symbols': symbol,
                    'window_size': window_size
                }
            )
            return fn
        return handlers
    schedule.all =  handler
    return schedule


schedule = makeScheduler()
