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

    def get_deleted(self, model_type, model_id):
        return float(self.redis_connection.zscore(self._get_key(model_type, True), model_id))

    def get_top(self, model_type, limit=100, offset=0, direction=1):
        if direction < 0:
            return self.redis_connection.zrevrange(self._get_key(model_type), offset, limit, True)
        else:
            return self.redis_connection.zrange(self._get_key(model_type), offset, limit, True)

    def soft_delete(self, model_type, model_id):
        current_rating = self.get(model_type, model_id)
        self.redis_connection.zadd(self._get_key(model_type, True), model_id, current_rating)

        self.redis_connection.zrem(self._get_key(model_type), model_id)

    def restore(self, model_type, model_id):
        current_rating = self.get_deleted(model_type, model_id)
        self.redis_connection.zadd(self._get_key(model_type), model_id, current_rating)

        self.redis_connection.zrem(self._get_key(model_type, True), model_id)

    def toggle_state(self, model_type, model_id, future_state):
        """
        Change item rating state. Change only if not already changed
        :type model_type:
        :type model_id:
        :type future_state:
        :return:
        """
        if not future_state:
            if self.get(model_type, model_id) is not None:
                self.soft_delete(model_type, model_id)
        else:
            if self.get_deleted(model_type, model_id) is not None:
                self.restore(model_type, model_id)
