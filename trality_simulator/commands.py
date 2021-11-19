#!/usr/bin/env python
# -*- coding: utf-8 -*-


from trality_simulator.misc import get_modules, DefaultHelpParser, \
    SubcommandHelpFormatter
from trality_simulator import __version__
import trality_simulator.subcommands


def main():
    '''
    Execute the function with args
    '''
    parser = DefaultHelpParser(
        prog='trality', formatter_class=lambda prog:
        SubcommandHelpFormatter(prog, max_help_position=20, width=75),
        description=('Trality simulation suite'),
        add_help=True,
        epilog='This is version %s - %s - %s' %
        (__version__.version, __version__.author, __version__.date))
    subparsers = parser.add_subparsers(dest='module')

    modules = get_modules(trality_simulator.subcommands, subparsers, {})
    try:
        args, extra = parser.parse_known_args()
        if args.module in modules.keys():
            modules[args.module](subparsers, args.module, extra)
        else:
            if args.module is None:
                return parser.print_help()
            else:
                return parser.parse_args(args)
    except IndexError:
        return parser.print_help()

if __name__ == "__main__":
    main()
