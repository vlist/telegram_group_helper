from pathlib import Path

class Framework():
    def __init__(self) -> None:
        pass

    def findAllModules(self, module_root_dir: Path) -> None:
        """Find all modules in the directory provied by module_root_dir.

        This method finds all modules in the "module_root_dir". Load all modules and provides an array
        of module registeration functions ("self.module_register_functions") for "registerAllModules".

        Args:
            module_root_dir (Path): Path to the directory that contains module files.
        """
        pass

    def registerAllModules(self) -> None:
        """Register all modules found by "findAllModules". 

        This method register all modules in the "self.module_register_functions". Registeration process
        provides the following informations:
            1. Name of the module
            2. Dependencies required by the module.
            3. Dependencies provided by the module.
            4. Entry point of the moduel. ("run()" method)
            5. Exit point of the module. (Optional.)
        """
        pass

    def buildDAG(self) -> None:
        """Create the DAG based on the dependencies required and provided by all modules.

        This method create the Directed Acyclic Graph (DAG) based on the dependencies required
        and provided by all modules. The DAG is also validated at current setp to ensures acyclicality
        and reachability of all nodes.
        
        Note: If feed_back type exists. Treat it as node that does not have any dependencies.
              For the first time, feed_back will be initialzied with "inital_value" in the Data.

        """
        pass

    def solveDAG(self) -> None:
        """Solve the DAG and prove the order at which each module will be executed.

        This method performs topological sorting on the DAG created and validated by "buildDAG".
        This method solve the DAG through either Kahn's algorithm or Depth-first search. Those 
        two methos are interchangeable.
        """
        pass

    def launchModules(self) -> None:
        """Launch modules on-the-fly.

        This method launches modules based on the result from "solveDAG". It ensures that modules
        launched have all their dependencies satisfied (Data.ready == True).

        If a module depends on a feed_back type of data. The feed_back will be treated as a new 
        data_in after "flush" is invoked and the dependencies of the module that reuqires feed_back 
        will be evaluted every time during run time. And the dependencies provided by the module 
        will also be treated as a new data_out. All modules that dependends on the data_out will 
        also be relaunched.

        (This method will be complicated... It can build a sub graph and invoke "solveDAG" again 
        for the new graph.)
        """
        pass