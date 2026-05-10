import pandas as pd
from typing import Dict

def analyze_agile_metrics(sprint_data: pd.DataFrame) -> Dict[str, float]:
    if sprint_data.empty:
        return {}

    velocity = sprint_data['completed_points'].mean() if 'completed_points' in sprint_data.columns else 0
    
    planned_sum = sprint_data['planned_points'].sum()
    scope_creep = ((sprint_data['added_points'].sum() / planned_sum) * 100
                   if 'added_points' in sprint_data.columns and 'planned_points' in sprint_data.columns and planned_sum > 0 else 0)

    return {
        'average_velocity': round(velocity, 2),
        'scope_creep_percentage': round(scope_creep, 2)
    }
