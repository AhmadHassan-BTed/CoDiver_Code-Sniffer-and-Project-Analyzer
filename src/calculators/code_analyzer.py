import ast
from typing import Optional
from ..core.models import CodeMetrics

def calculate_cognitive_complexity(node, complexity=0, nesting=0):
    if isinstance(node, (ast.If, ast.While, ast.For)):
        complexity += (1 + nesting)
        nesting += 1
    elif isinstance(node, ast.Try):
        complexity += (1 + nesting)

    for child in ast.iter_child_nodes(node):
        complexity = calculate_cognitive_complexity(child, complexity, nesting)

    return complexity

def calculate_function_points(metrics: CodeMetrics) -> float:
    return (metrics.functions * 3 + metrics.classes * 5) * 0.7

def analyze_python_file(file_content: str) -> Optional[CodeMetrics]:
    try:
        tree = ast.parse(file_content)

        loc = len(file_content.splitlines())
        functions = len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
        classes = len([node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)])

        complexity = 1
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.Assert)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1

        cognitive = calculate_cognitive_complexity(tree)

        metrics = CodeMetrics(
            lines_of_code=loc,
            functions=functions,
            classes=classes,
            cyclomatic_complexity=complexity,
            cognitive_complexity=cognitive,
            function_points=0,
            defect_density=0
        )

        metrics.function_points = calculate_function_points(metrics)
        metrics.defect_density = (complexity * cognitive) / (loc if loc > 0 else 1)

        return metrics
    except Exception:
        return None
