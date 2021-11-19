# TODO: Implement all members in data
# TODO: Implement shell functions for all indicators in indicators.py

from inspect import getmembers, isfunction
from trality_simulator import indicators


class Data:
    def __init__(self, symbol=None, base=None, quoted=None, keys=None) -> None:
        self.symbol = symbol
        self.base = base
        self.quoted = quoted
        self.keys = keys

        # Register all of the functions in indicators.py so they can be called
        # from data using dot notation
        self.indicator_map = {}
        for ind_name, ind_function in getmembers(indicators, isfunction):
            self.indicator_map[ind_name] = lambda *x: ind_function(self.__dict__, *x)

    def __getattr__(self, name: str):
        """If __getattributes__ fails to find a class attribute (called using
        dot notation), then this function is called. This function checks
        if the attribute is an indicator function.
        """
        try:
            return self.indicator_map[name]
        except KeyError:
            raise AttributeError

    def select(self, var_name):
        return self.__dict__[var_name]

    def select_last(self, var_name):
        return self.__dict__[var_name][-1]


# Code for testing below this line
def main():
    data = Data()
    print(data.test_indicator(11, 5))
    print(data.not_here)


if __name__ == "__main__":
    main()
