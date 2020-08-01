

def assert_eq(val, expect):
    if val == expect:
        return
    else:
        err = "%s not equal %s" % (val, expect)
        raise AssertionError(err)

