"""Fixer for __nonzero__ -> __bool__ methods."""
# Author: Collin Winter

# Local imports
from .. import fixer_base
from .. import pytree
from ..pgen2 import token
from ..pytree import Leaf, Node
from ..fixer_util import Name, syms, LParen, RParen, Newline, Dot, find_indentation

class FixNonzero(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """
    classdef< 'class' any+ ':'
              suite< any*
                     funcdef< 'def' name='__nonzero__'
                              parameters< '(' NAME ')' > any+ >
                     any* > >
    """

    def transform(self, node, results):
        name = results["name"]
        indent = find_indentation(name)
        #new = Name("__bool__", prefix=name.prefix)
        #name.replace(new)

        children = [Leaf(token.NAME, 'def', prefix=indent),
            Leaf(token.NAME, '__bool__', prefix=" "),
            LParen(),
            Leaf(token.NAME, 'self'),
            RParen(),
            Leaf(token.COLON, ':'),
            Newline(),
            Leaf(token.INDENT, "    "),
            Leaf(token.NAME, 'return', prefix=indent),
            Leaf(token.NAME, 'self', prefix=" "),
            Dot(),
            Leaf(token.NAME, '__nonzero__', prefix=""),
            LParen(),
            RParen(),
            Newline(),
        ]
        
        nf = pytree.Node(self.syms.power, children)
        
        node.append_child(nf)