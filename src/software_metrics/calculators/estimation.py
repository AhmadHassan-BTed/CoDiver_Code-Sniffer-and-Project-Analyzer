from typing import Dict

def calculate_cocomo(kloc: float) -> Dict[str, float]:
    if kloc == 0:
        return {'effort': 0, 'time': 0, 'staff': 0}
        
    effort = 2.4 * (kloc ** 1.05)
    time = 2.5 * (effort ** 0.38)
    staff = effort / time if time > 0 else 0
    return {
        'effort': round(effort, 2),
        'time': round(time, 2),
        'staff': round(staff, 2)
    }
