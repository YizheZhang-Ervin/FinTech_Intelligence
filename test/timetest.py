from timeit import Timer


def f1(): pass


def f2(): pass


def timetest1(func1, **others):
    """
    :param func1: function
    :param others: value/nums/name1
    :return: function + value + time
    """
    value = others.get('value', 1)
    nums = others.get('nums', 1)
    name1 = others.get('name1', 'f1')
    global f1
    f1 = func1
    if type(value) == str:
        p1 = f'f1("{value}")'
        rst1 = func1(value)
    elif type(value) == int or type(value) == float or type(value) == complex or type(value) == list:
        p1 = f'f1({value})'
        rst1 = func1(value)
    elif len(value) > 1:
        p1 = f'f1({value[0]},{value[1]})'
        rst1 = func1(value[0], value[1])
    else:
        p1 = f'f1({value})'
        rst1 = func1(value)
    t1 = Timer(p1, "from test.timetest import f1").timeit(nums)
    print(f'{name1} Value:{rst1}, Time:{t1}')


def timetest2(func1, func2, **others):
    """
    :param func1: function
    :param func2: function
    :param others: value/nums/name1/name2
    :return: function + value + time
    """
    value = others.get('value', 1)
    nums = others.get('nums', 1)
    name1 = others.get('name1', 'f1')
    name2 = others.get('name2', 'f2')
    global f1, f2
    f1, f2 = func1, func2
    if type(value) == str:
        p1 = f'f1("{value}")'
        p2 = f'f2("{value}")'
        rst1 = func1(value)
        rst2 = func2(value)
    elif type(value) == int or type(value) == float or type(value) == complex or type(value) == list:
        p1 = f'f1({value})'
        p2 = f'f2({value})'
        rst1 = func1(value)
        rst2 = func2(value)
    elif len(value) > 1:
        p1 = f'f1({value[0]},{value[1]})'
        p2 = f'f2({value[0]},{value[1]})'
        rst1 = func1(value[0], value[1])
        rst2 = func2(value[0], value[1])
    else:
        p1 = f'f1({value})'
        p2 = f'f2({value})'
        rst1 = func1(value)
        rst2 = func2(value)

    t1 = Timer(p1, "from test.timetest import f1").timeit(nums)
    t2 = Timer(p2, "from test.timetest import f2").timeit(nums)
    print(f'{name1} Value:{rst1}, Time:{t1} \n{name2} Value:{rst2}, Time:{t2}')
