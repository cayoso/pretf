from pretf.api import block


def terraform(var):
    yield block("output", "five", {"value": var.five})

    yield block("output", "six", {"value": var.six})

    yield block("output", "seven", {"value": var.seven})
