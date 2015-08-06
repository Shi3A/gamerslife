from django.apps import AppConfig
from django.conf import settings
from rating.redis_driver import Redis as RedisDriver
import redis


class RatingConfig(AppConfig):
    name = 'rating'
    verbose_name = 'Ratings'

    connection = None
    driver = None

    def ready(self):
        if not self.connection:
            if not settings.RATING_DRIVER or settings.RATING_DRIVER == 'redis':
                self.connection = redis.StrictRedis(host=settings.RATING_DRIVER_HOST, port=settings.RATING_DRIVER_PORT,
                                                db=int(settings.RATING_DRIVER_DB))
                self.driver = RedisDriver(self.connection)
