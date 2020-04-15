#!/usr/bin/env python
# coding=utf-8
"""

"""
import cmd2


class CmdLineApp(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        self.rename_command('run_script', 'run-script')


if __name__ == '__main__':
    import sys
    c = CmdLineApp()
    sys.exit(c.cmdloop())
