import argparse
import os
import importlib.machinery
import importlib.util
import trality_simulator
from inspect import getmembers, isfunction, isclass, ismodule

import trality_simulator.indicators
import trality_simulator.orders
import trality_simulator.plotter
import trality_simulator.scheduler
import trality_simulator.helpers
import trality_simulator.portfolio
import trality_simulator.data



def add_parser(subparsers, module_name):
    return subparsers.add_parser(
        module_name, add_help=False,
        help=('Test a stategy code with historical data'))


def backtesting(subparsers, module_name, argv):

    parser = add_parser(subparsers, module_name)
    parser.add_argument(dest='strategy',
        help='strategy python source file')
    args = parser.parse_args(argv)

    # file name of the strategy
    file_name = os.path.basename(args.strategy)
    module_name = file_name.replace('.py$', '')
    # load the file as a module
    loader = importlib.machinery.SourceFileLoader(module_name, args.strategy)
    spec = importlib.util.spec_from_loader(module_name, loader)
    my_strategy = importlib.util.module_from_spec(spec)

    # gather all the functions and class of a module
    # eg c_core is the core module with schedule and other
    # methods

    trality_sim_mod = getmembers(trality_simulator, ismodule)

    for sim_module in trality_sim_mod:
        trality_sim_fun = getmembers(sim_module[1], isfunction)
        trality_sim_class = getmembers(sim_module[1], isclass)
        for fun in trality_sim_fun:
            # Add each method/class in the module
            setattr(my_strategy, fun[0], fun[1])

    loader.exec_module(my_strategy)
    print(my_strategy.schedule.all)
