"""Fixer that changes raw_input(...) into input(...)."""
# Author: Andre Roberge

# Local imports
from .. import fixer_base
from ..fixer_util import Name, touch_import

class FixRawInput(fixer_base.BaseFix):

    BM_compatible = True
    PATTERN = """
              power< name='raw_input' trailer< '(' [any] ')' > any* >
              """

    def transform(self, node, results):
        touch_import('six.moves', 'input', node=node)
        name = results["name"]
        name.replace(Name("input", prefix=name.prefix))
