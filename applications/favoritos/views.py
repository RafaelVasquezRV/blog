from django.shortcuts import render

from django.db import IntegrityError

from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.views.generic import (
    View,
    ListView,
    DeleteView,
)

from django.http import HttpResponseRedirect

from .models import Favorites

from applications.entrada.models import Entry
# Create your views here.


class UserPageListView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)
    

class AddFavoritosView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        # recuperar el usuario
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        # registramos favorito
        try:
            Favorites.objects.create(
                user=usuario,
                entry=entrada,
            )
        except IntegrityError:
            # context = self.get_context_data(mensaje='No se puede agregar')
            # return self.render_to_response(context)
            return render("entrada/detail.html", {"message": 'No se puede agregar'})

        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil',
            )
        )



class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')
