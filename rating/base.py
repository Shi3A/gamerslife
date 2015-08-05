from abc import ABCMeta, abstractmethod, abstractproperty


class Base:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, model_type, model_id, value):
        """
        Set rating value

        :type model_type: str
        :type model_id: int
        :type value: float
        :return: None
        """

    @abstractmethod
    def get(self, model_type, model_id):
        """
        Get rating value

        :type model_type: str
        :type model_id: int
        :return: int
        """

    @abstractmethod
    def incr(self, model_type, model_id):
        """
        Increment rating value

        :type model_type: str
        :type model_id: int
        :return: None
        """

    @abstractmethod
    def decr(self, model_type, model_id):
        """
        Decrement rating value

        :type model_type: str
        :type model_id: int
        :return: None
        """

    @abstractmethod
    def get_top(self, model_type, limit=100, offset=0, direction=1):
        """
        Get rating list of specific collection (model_type)

        :type model_type: str
        :type limit: int
        :type offset: int
        :return: OrderedDict in {id:rating} format
        """

    @abstractmethod
    def soft_delete(self, model_type, model_id):
        """
        Delete item rating, but save it to another place to can be restored in future

        :type model_type: str
        :type model_id: int
        :return: None
        """

    @abstractmethod
    def restore(self, model_type, model_id):
        """
        Restore item rating

        :type model_type: str
        :type model_id: int
        :return: None
        """

    @staticmethod
    def _get_key(model_type, deleted_list=False):
        """
        Return prefixed unique key for rate item
        :type model_type: int
        :return: str
        """
        prefix = ""
        if deleted_list:
            prefix = "deleted_"
        return "rating_{0}{1}" % {prefix, model_type}

    @abstractmethod
    def toggle_state(self, model_type, model_id, future_state):
        """
        Change rating state
        :type model_type: str
        :type model_id: int
        :type future_state: bool
        :return:
        """
