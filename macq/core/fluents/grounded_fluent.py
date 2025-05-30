from typing import List

from ..planning_object import PlanningObject

class GroundedFluent:
    name: str
    objects: List[PlanningObject]

    def __init__(self, name: str, objects: List[PlanningObject]):
        self.name = name
        self.objects = objects