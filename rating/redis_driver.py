from base import Base


class Redis(Base):
    redis_connection = None

    def __init__(self, redis_connection):
        """

        :param redis_connection: redis.Redis
        :return:
        """
        super(Redis, self).__init__()
        self.redis_connection = redis_connection

    def incr(self, model_type, model_id):
        self.redis_connection.zincrby(self._get_key(model_type), model_id, 1)

    def decr(self, model_type, model_id):
        self.redis_connection.zincrby(self._get_key(model_type), model_id, -1)

    def set(self, model_type, model_id, value):
        self.redis_connection.zadd(self._get_key(model_type), model_id, value)

    def get(self, model_type, model_id):
        return float(self.redis_connection.zscore(self._get_key(model_type), model_id))

    def get_top(self, model_type, limit=100, offset=0, direction=1):
        if direction < 0:
            return self.redis_connection.zrevrange(self._get_key(model_type), offset, limit, True)
        else:
            return self.redis_connection.zrange(self._get_key(model_type), offset, limit, True)
