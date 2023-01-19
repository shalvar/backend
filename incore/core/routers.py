from rest_framework.routers import DefaultRouter
from main.views import MainViewSet
from concert.views import ConcertViewSet
from film.views import FilmViewSet

from authentication.views import UserViewSet

router = DefaultRouter()

router.register('main', MainViewSet)
router.register('concert', ConcertViewSet)
router.register('film', FilmViewSet)
router.register('auth', UserViewSet)
