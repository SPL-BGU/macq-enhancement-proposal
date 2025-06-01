from typing import List, Set

from ..signature_parameter import SignatureParameter
from ..fluents.parameter_bound_fluent import ParameterBoundFluent

class LiftedAction:

    name: str
    params: List[SignatureParameter]
    positive_preconditions: Set[ParameterBoundFluent]
    negative_preconditions: Set[ParameterBoundFluent] | None
    add_effects: Set[ParameterBoundFluent]
    delete_effects: Set[ParameterBoundFluent]


    def __init__(self, name: str, params: List[SignatureParameter]):
        self.positive_preconditions = set()
        self.negative_preconditions = None
        self.add_effects = set()
        self.delete_effects = set()
        self.name = name
        self.params = params

    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError