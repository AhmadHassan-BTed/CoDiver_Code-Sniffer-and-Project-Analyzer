from dataclasses import dataclass

@dataclass
class CodeMetrics:
    lines_of_code: int
    functions: int
    classes: int
    cyclomatic_complexity: int
    cognitive_complexity: int
    function_points: float
    defect_density: float
