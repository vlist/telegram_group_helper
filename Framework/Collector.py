from Data import Data
import FrameworkException as FE


class Collector:
    def __init__(self) -> None:
        self.module_name = ""  # Name of the module
        self.data_in = dict([])  # Input data of the current module (Dependencies required.) {name -> Data}
        self.data_out = dict([])  # Output data of the current module (Dependencies provided.) {name -> Data}
        self._inited = False  # If this module is initialized.

    def addOut(self, *data: Data):
        # Note: Here we only assert if the name of the variable is unique in either data_in or data_out.
        #       The uniqueness of the data in both data_in and data_out will be asserted during DAG solving.
        if self._inited:
            return
        for this_data in data:
            if this_data.name in self.data_out:
                raise FE.MultipleInstancesException(
                    "\"{:s}\" already exists in the data_out for this module.".format(this_data.name))
            self.data_out[this_data.name] = this_data

    def addIn(self, *data: Data):
        # Note: Here we only assert if the name of the variable is unique in either data_in or data_out.
        #       The uniqueness of the data in both data_in and data_out will be asserted during DAG solving.
        if self._inited:
            return
        for this_data in data:
            if this_data.name in self.data_in:
                raise FE.MultipleInstancesException(
                    "\"{:s}\" already exists in the data_in for this module.".format(this_data.name))
            self.data_in[this_data.name] = this_data

    def registerModuleName(self, name: str):
        if self._inited:
            return
        self.module_name = name

    def flushVar(self, data: Data):
        # Coordinate with other Collectors
        pass

    def getData(self) -> Data:
        pass

    def registration_complete(self):
        self._inited = True
