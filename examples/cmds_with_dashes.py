#!/usr/bin/env python
# coding=utf-8
"""

"""
import cmd2


class CmdLineApp(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        self.rename_command('speed_up', 'speed-up')
        self.rename_command('run_pyscript', 'run-pyscript')
        self.self_in_py = True

    def do_speed_up(self, args):
        self.poutput("going faster")

    def help_speed_up(self):
        self.poutput("help for going faster")

    def do_debug(self, args):
        """some dochelp on the debug command"""
        import ipdb; ipdb.set_trace()

    def help_mytopic(self):
        self.poutput('additional help on a topic that is not a command')


if __name__ == '__main__':
    import sys
    c = CmdLineApp()
    sys.exit(c.cmdloop())
