"""
/!\ Permit to add automaticly datas from backend in models/database Datadisp
"""


from datadisp.models import Datadisp
data = Datadisp(author = 'Fostin', title = 'blabla', description = 'description')
data.save()

"""
data.title() # change title
data.author() # change author
data.save() #update db
"""