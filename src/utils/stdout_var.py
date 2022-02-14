from typing import Any


def stdout_var(varname: str, varval: Any) -> None:
    # prints out the var name and associated value
    var_name = varname.split("=")[0] if "=" in varname else varname
    print(var_name, ": ", varval)
