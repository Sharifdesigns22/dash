class DashException(Exception):
    pass


class NoLayoutException(DashException):
    pass


class CallbackException(DashException):
    pass


class NonExistantIdException(CallbackException):
    pass


class NonExistantPropException(CallbackException):
    pass


class NonExistantEventException(CallbackException):
    pass


class UndefinedLayoutException(CallbackException):
    pass


class IncorrectTypeException(CallbackException):
    pass


class MissingEventsException(CallbackException):
    pass


class LayoutIsNotDefined(CallbackException):
    pass


class IDsCantContainPeriods(CallbackException):
    pass


# Better error name now that more than periods are not permitted.
class InvalidComponentIdError(IDsCantContainPeriods):
    pass


class CantHaveMultipleOutputs(CallbackException):
    pass


# Renamed for less confusion with multi output.
class DuplicateCallbackOutput(CantHaveMultipleOutputs):
    pass


class PreventUpdate(CallbackException):
    pass


class DuplicateIdError(DashException):
    pass


class InvalidCallbackReturnValue(CallbackException):
    pass


class InvalidConfig(DashException):
    pass


class InvalidResourceError(DashException):
    pass


class InvalidIndexException(DashException):
    pass


class DependencyException(DashException):
    pass


class ResourceException(DashException):
    pass
