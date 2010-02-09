#!/usr/bin/env python
"""Script to auto-generate our API docs.
"""
# stdlib imports
import os
import sys

# local imports
sys.path.append(os.path.abspath('sphinxext'))
from apigen import ApiDocWriter

#*****************************************************************************
if __name__ == '__main__':
    pjoin = os.path.join
    package = 'IPython'
    outdir = pjoin('source','api','generated')
    docwriter = ApiDocWriter(package,rst_extension='.txt')
    # You have to escape the . here because . is a special char for regexps.
    # You must do make clean if you change this!
    docwriter.package_skip_patterns += [r'\.fixes$',
                                        r'\.external$',
                                        r'\.extensions',
                                        r'\.kernel\.config',
                                        r'\.attic',
                                        r'\.quarantine',
                                        r'\.deathrow',
                                        r'\.config\.default',
                                        r'\.config\.profile',
                                        r'\.frontend',
                                        r'\.gui'
                                        ]

    docwriter.module_skip_patterns += [ r'\.core\.fakemodule',
                                        
                                        # XXX These need fixing, disabling for
                                        # now but we need to figure out why
                                        # they are breaking.  Error from sphinx
                                        # for each group copied below
                                        
                                        # AttributeError: __abstractmethods__
                                        r'\.core\.component',
                                        r'\.utils\.traitlets',
        
                                        # AttributeError: __provides__
                                        r'\.kernel\.clusterdir',
                                        r'\.kernel\.configobjfactory',
                                        r'\.kernel\.fcutil',
                                        r'\.kernel\.ipcontrollerapp',
                                        r'\.kernel\.launcher',
                                        r'\.kernel\.task',
                                        r'\.kernel\.winhpcjob',
                                        r'\.testing\.util',
    
                                        # Keeping these disabled is OK
                                        r'\.cocoa',
                                        r'\.ipdoctest',
                                        r'\.Gnuplot',
                                        r'\.frontend\.process\.winprocess',
                                        r'\.Shell',
                                        ]
    docwriter.write_api_docs(outdir)
    docwriter.write_index(outdir, 'gen',
                          relative_to = pjoin('source','api')
                          )
    print '%d files written' % len(docwriter.written_modules)