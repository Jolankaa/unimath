

def NonCompliancaRecognition():
    """
    This error is caused by the given parameter 
    being given that does not match the definition of the given operation.

    Reasons:
    may be caused by giving an inappropriate value to the domain
    A value that is not appropriate for the given operation may have been given
    
    """

    print("[ERROR] Non-Complianca Recognition Error ")
    exit()

class DefinitionError(Exception): 
    """
    Mathematics is based on definitions.
    If you make a definitional error in the operations, 
    the whole operation will be wrong.
    This error occurs when you make the mathematical definition incorrect.
    """
    pass

class SizeLimitExceededError(Exception):
    """The operations described are only valid in 2 and 3 dimensional planes and spaces."""
    pass

class WrongDataTypeError(Exception):
    """
    An error is thrown because the data type in the given 
    parameter does not match the requested data type.
    """

    """
    def __init__(self, variable_name, expected_type):
        message = f" The variable {variable_name} must be of type {expected_type.__name__}"
        super().__init__(message)
    """
    pass

class RequiredModule(Exception):
    """
    There are external modules required for some functions.
    If the required module is not installed, you will get this error.
    """
    pass

class NonSymbolicValue(Exception):
    pass