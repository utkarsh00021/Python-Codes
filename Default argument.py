def display_info(name,rolln,sec='CD',cllg='GLA'):
    data=f'''
    Name:{name}
    Section:{sec}
    Roll no.:{rolln}
    college:{cllg}'''
    return data
out=display_info('Utkarsh',25)
print(out)
