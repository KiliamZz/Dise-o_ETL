def categoria (valor_categoria):
    if valor_categoria == 'Less than $40K':
        return 'Muy bajo'
    elif valor_categoria == '$40K - $60K':
        return 'bajo'
    elif valor_categoria == '$60K - $80K':
        return 'Intermedio'
    elif valor_categoria == '$80K - $120K':
        return 'Alto'
    elif valor_categoria == '$120K +':
        return 'Muy Alto'
    elif valor_categoria == 'Unknown':
        return 'Desconocido'