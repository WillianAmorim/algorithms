def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    quantidade = 0
    
    for estudante in permanence_period:
        estudante_min, estudante_max = estudante

        if type(estudante_min) != int:
            return None
        
        if type(estudante_max) != int:
            return None
            
        if estudante_min <= target_time <= estudante_max:
            quantidade += 1
    return quantidade
