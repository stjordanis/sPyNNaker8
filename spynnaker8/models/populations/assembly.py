from pyNN import common as pynn_common
from spinn_front_end_common.utilities import globals_variables


class Assembly(pynn_common.Assembly):
    _simulator = globals_variables.get_simulator()
