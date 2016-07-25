#!/usr/bin/env python3 


def gen_1a() :
    yield 1
    yield 2
    for v in gen2() :
        yield v
    yield 'a'
    yield 'b'

def gen_1b() :
    try:
        yield 1
        yield 2
        v = gen2()
        while True:
            yield next(v)
    except StopIteration:
        yield 'a'
        yield 'b'
    

def gen2() :
    yield [1, 2, 3]
    yield ['a', 'b', 'c']


for v in gen_1a() :
    print(v)
print('-----------')
for v in gen_1b() :
    print(v)

