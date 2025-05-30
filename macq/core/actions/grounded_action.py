from typing import List, Set

from ..planning_object import PlanningObject
from ..fluents.grounded_fluent import GroundedFluent

class GroundedAction:

    name: str
    params: List[PlanningObject]
    positive_preconditions: Set[GroundedFluent]
    negative_preconditions: Set[GroundedFluent]
    add_effects: Set[GroundedFluent]
    delete_effects: Set[GroundedFluent]


    def __init__(self, objects: List[PlanningObject],  is_strips:bool= False):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
