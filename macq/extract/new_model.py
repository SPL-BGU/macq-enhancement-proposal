from json import dumps, loads
from typing import Set, Union

import tarski
import tarski.fstrips as fs
from tarski.fol import FirstOrderLanguage
from tarski.io import fstrips as iofs
from tarski.syntax import land
from tarski.syntax.formulas import CompoundFormula, Connective, top

from ..trace import Fluent
from ..utils import ComplexEncoder
from .learned_action import LearnedAction, LearnedLiftedAction
from .learned_fluent import LearnedFluent, LearnedLiftedFluent

#TODO check option to use the pddl-parser


class LiftedActionModel:
    pass

class GroundedActionModel:
    pass