def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    quantidade = 0
    for est_min, est_max in permanence_period:
        if not isinstance(est_min, int) or not isinstance(est_max, int):
            return None
        if est_min <= target_time <= est_max:
            quantidade += 1
    return quantidade
