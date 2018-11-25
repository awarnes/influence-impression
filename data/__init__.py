"""To enable cross folder imports? TODO: This shit is dumb"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))