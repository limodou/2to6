"""Fix function attribute names (f.func_x -> f.__x__)."""
# Author: Collin Winter

# Local imports
#from .. import pytree
#from .. import fixer_base
#from ..fixer_util import Name, touch_import, Call
#
#
#class FixFuncattrs(fixer_base.BaseFix):
#    BM_compatible = True
#
#    PATTERN = """
#    power< call_name=any+ trailer< '.' attr=('func_closure' | 'func_doc' | 'func_globals'
#                                  | 'func_name' | 'func_defaults' | 'func_code'
#                                  | 'func_dict') > next=any* >
#    """
#
#    def transform(self, node, results):
#        
#        touch_import(None, 'six', node=node)
#        
#        syms = self.syms
#        attr = results["attr"][0]
#        call_ = results['call_name'][0]
#        args = [Name(call_.value, prefix="")]
#        tail = []
#        if results['next']:
#            tail = [x.clone() for x in results['next']]
#        new = Call(Name("six.get_function_%s" % attr.value[5:]), args, call_.prefix)
#        if tail:
#            new = pytree.Node(syms.power, [new] + tail)
#        new.prefix = node.prefix
#        return new
#        
from .. import fixer_base
from ..fixer_util import Name

class FixFuncattrs(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = """
    power< any+ trailer< '.' attr=('func_closure' | 'func_doc' | 'func_globals'
                                  | 'func_name' | 'func_defaults' | 'func_code'
                                  | 'func_dict') > any* >
    """

    def transform(self, node, results):
        attr = results["attr"][0]
        attr.replace(Name(("__%s__" % attr.value[5:]),
                          prefix=attr.prefix))
