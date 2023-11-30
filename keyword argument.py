def display_info(name,rolln,sec,cllg):
    data=f'''
    Name:{name}
    Section:{sec}
    Roll no.:{rolln}
    college:{cllg}'''
    return data
out=display_info(sec='CD',rolln=3,cllg='GLA',name='Utkarsh')
print(out)
