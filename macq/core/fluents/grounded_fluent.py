from typing import List

from ..planning_object import PlanningObject

class GroundedFluent:
    name: str
    objects: List[PlanningObject]

    def __init__(self, name: str, objects: List[PlanningObject]):
        self.name = name
        self.objects = objects

    def get_binding(self, action_parameters: List[PlanningObject]) -> List[int]:
        """Returns indices of fluent objects in action parameters list."""
        binding = []
        for obj in self.objects:
            try:
                binding.append(action_parameters.index(obj))
            except ValueError:
                raise ValueError(f"Object {obj} not found in action parameters {action_parameters}")
        return binding

    def __str__(self):
        return f"{self.name} {' '.join(planning_object.name for planning_object in self.objects)}"

    def details(self):
        if len(self.objects) > 0:
            string = f"{self.name} {' '.join([o.name for o in self.objects])}"

        else:
            string = self.name
        return f"({string})"


    def __repr__(self):
        return self.details()

    def _serialize(self):
        return str(self)