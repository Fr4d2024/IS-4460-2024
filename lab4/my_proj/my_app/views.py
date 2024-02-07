from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects


def title_name(the_name: str):
    return the_name.title()

def title_names(names:list):
    new_names = [x.title() for x in names]
    return new_names

class HomePageView(View):
    def get(self, request):
     
        my_name = "FRED"

        new_name = title_name(my_name)

        the_names = ['Fred','Drake','Javier']

        new_names = my_functions.fix_names_list(the_names)

        car1 = my_objects.car('green','honk honk')
        car2 = my_objects.car('blue','beep beep')

        car2.make = "Toyota"
        

        the_context = {'hi':'Hello worlds!',
                       'name':new_name,
                       'names_list':the_names,
                       'car1':car1,
                       'car2':car2
                       }

        return render(request, 'my_app/index.html', the_context)