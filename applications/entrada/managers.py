from django.db import models


class EntryManager(models.Manager):
    """Procedimiento para entrada"""

    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,            
        ).order_by('-created').first()
    
    def entradas_en_home(self):
        # devuelve las últimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]
    
    def entradas_recientes(self):
        # devuelve las últimas 6 entradas entradas recientes
        return self.filter(
            public=True,
        ).order_by('-created')[:6]
