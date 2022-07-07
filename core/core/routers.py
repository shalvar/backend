from rest_framework.routers import DefaultRouter
from main.views import MainViewSet
from contert.views import ContertViewSet
from film.views import FilmViewSet

from authentication.views import UserViewSet

router = DefaultRouter()

router.register('main', MainViewSet)
router.register('contert', ContertViewSet)
router.register('film', FilmViewSet)
router.register('auth', UserViewSet)