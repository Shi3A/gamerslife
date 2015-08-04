from abc import ABCMeta, abstractmethod, abstractproperty


class Base:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, model_type, model_id, value):
        """
        Set rating value

        :param model_type: basestring
        :param model_id: int
        :param value: float
        :return: None
        """

    @abstractmethod
    def get(self, model_type, model_id):
        """
        Get rating value

        :param model_type: basestring
        :param model_id: int
        :return: int
        """

    @abstractmethod
    def incr(self, model_type, model_id):
        """
        Increment rating value

        :param model_type: basestring
        :param model_id: int
        :return: None
        """

    @abstractmethod
    def decr(self, model_type, model_id):
        """
        Decrement rating value

        :param model_type: basestring
        :param model_id: int
        :return: None
        """

    @abstractmethod
    def get_top(self, model_type, limit=100, offset=0, direction=1):
        """
        Get rating list of specific collection (model_type)

        :param model_type: basestring
        :param limit: int
        :param offset: int
        :return: OrderedDict in {id:rating} format
        """

    def _get_key(self, model_type):
        """
        Return prefixed unique key for rate item
        :param model_type: int
        :return: basestring
        """
        return "rating_{0}" % {model_type}