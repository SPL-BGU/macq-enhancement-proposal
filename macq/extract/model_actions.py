from typing import List, Set

from .signature_parameter import ObjectType, SignatureParameter
from .model_fluents import ParameterBoundLiteral, GroundedFluent

class LiftedAction:

    name: str
    params: List[SignatureParameter]
    positive_preconditions: Set[ParameterBoundLiteral]
    negative_preconditions: Set[ParameterBoundLiteral]
    add_effects: Set[ParameterBoundLiteral]
    delete_effects: Set[ParameterBoundLiteral]


    def __init__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError



#notice that 'GroundedFluent' renames the Fluent instance available in the trace package.
class GroundedAction:

    name: str
    params: List[SignatureParameter]
    positive_preconditions: Set[GroundedFluent]
    negative_preconditions: Set[GroundedFluent]
    add_effects: Set[GroundedFluent]
    delete_effects: Set[GroundedFluent]


    def __init__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
