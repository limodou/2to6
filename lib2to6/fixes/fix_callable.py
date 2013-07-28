# Copyright 2007 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Fixer for callable().

This converts callable(obj) into isinstance(obj, collections.Callable), adding a
collections import if needed."""

# Local imports
from .. import fixer_base
from ..fixer_util import Call, Name, String, Attr, touch_import

class FixCallable(fixer_base.BaseFix):
    BM_compatible = True

    order = "pre"

    # Ignore callable(*args) or use of keywords.
    # Either could be a hint that the builtin callable() is not being used.
    PATTERN = """
    power< 'callable'
           trailer< lpar='('
                    ( not(arglist | argument<any '=' any>) func=any
                      | func=arglist<(not argument<any '=' any>) any ','> )
                    rpar=')' >
           after=any*
    >
    """

    def transform(self, node, results):
        func = results['func']

        touch_import(None, 'six', node=node)

        args = [func.clone()]
#        args.extend(Attr(Name('collections'), Name('Callable')))
        return Call(Name('six.callable'), args, prefix=node.prefix)

