from datetime import datetime
from multiprocessing import Lock


class Data:
    def __init__(self, name: str) -> None:
        """Constructor of the Data object

        Question: Are we going to use MultiProcessing on different machines? If so, we may need
                  serialization & deserialization methods.

        Args:
            name (str): name of the data. This must be unique with in the same module.
        """
        self.name = name  # Name of the data. It must be unique in the same model.
        self.pay_load = None  # Pay load
        self.last_update = datetime.utcnow()  # Update time of the data
        self.lock = Lock()  # Multiprocess lock. ensure that the data can only be read/write by a single process.
        self.feed_back = False  # If this is a feedback-able data. If true, initial_value must be provided.
        self.ready = False  # If this data ready to use. It must be true to be considered as OK to pass to the
        # module that requires this.

        # if type == "numpy_array":
        #     setattr(self, "serialize", self.__numpy_array_serializer)
        #     setattr(self, "deserialize", self.__numpy_array_deserializer)
        # elif type == "json":
        #     setattr(self, "serialize", self.__json_serializer)
        #     setattr(self, "deserialize", self.__json_deserializer)
        # elif type == "external":
        #     pass
        # elif type == "raw":
        #     pass
        # elif type == "self_defined":
        #     if serializer != None and deserializer != None:
        #         setattr(self, "serialize", serializer)
        #         setattr(self, "deserialize", deserializer)
        #     else:
        #         raise(FE.InputError("Serializer and Deserialize must be provided for \"self_defined\" type"))
        # else:
        #     raise(FE.FeatureNotImplementedError("Support {:0} type".format(str(type))))

    # def __numpy_array_serializer(self, option_1):
    #     pass

    # def __numpy_array_deserializer(self):
    #     pass

    # def __json_serializer(self):
    #     pass

    # def __json_deserializer(self):
    #     pass

    def setData(self, pay_load) -> None:
        """Load the content of the Data object.

        All setData call must be used with lock in place!!

        Args:
            pay_load (any type): Pay load of the object.
        """
        self.pay_load = pay_load
        self.last_update = datetime.utcnow()

    def getData(self):
        """Get the content of the Data object.

        All getData call must be used with lock in place!!

        Returns:
            any type: Pay load of the object.
        """
        return self.pay_load

    def __enter__(self):
        self.lock.acquire()
        return self

    def __exit__(self):
        self.lock.release()
