#!/usr/bin/env python

import os
import os.path
import json

import ansible
import ansible.runner
import ansible.playbook
import ansible.inventory

from ansible import callbacks
from ansible import utils


def run_the_book(playbook='localhost.yml', mypath=None, module_path=None, diff=False, noop=False, debug=False):

    if mypath is not None:
        local_inventory = ansible.inventory.Inventory(host_list=mypath + '/inventory')
    else:
        local_inventory = ansible.inventory.Inventory()

    local_inventory.subset('localhost')

    # setting callbacks
    stats = callbacks.AggregateStats()
    if not debug:
        playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
        runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)
    else:
        playbook_cb = callbacks.PlaybookCallbacks(verbose=True)
        runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=True)

    pb = ansible.playbook.PlayBook(
        playbook=playbook,
        stats=stats,
        module_path=module_path,
        callbacks=playbook_cb,
        runner_callbacks=runner_cb,
        inventory=local_inventory,
        check=noop,
        diff=diff
    )
    # running the playbook
    pr = pb.run()

    return pr


def main(argv):

    mypath = os.path.abspath(os.path.dirname(__file__))
    module_path = mypath + '/modules'

    try:
        output = run_the_book(
            playbook=mypath + '/' + argv.playbook,
            mypath=mypath,
            module_path=module_path,
            diff=argv.diff,
            noop=argv.noop,
            debug=argv.debug
        )
        print json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))
        return(0)

    except Exception as e:
        print 'Error: something went wrong'
        print 'Exception: {0}'.format(e)

    return(1)
