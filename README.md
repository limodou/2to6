2to6
========

## What's it

I need to port python 2.x source file to python 3.x, and I know 2to3 tool can do these convertion very well,
but I also want to keep python 2.x support. So I found six is a wrapper which can be compatible with python 2.x
and python 3.x. I think I can use 2to3 to do this thing, so I fork the 2to3 code, and change it enable it can
suit for six. That's why 2to6 existed.

## Details

Bacause I don't know 2to3 very well, so I just try my best to change the 2to3 code to fit my needs. So this
tool may not suit for you. But you can change it yourself I think. Converting source code is not as easy as I thought.

### urllib

### __nonzero__

__nonzero__ will be kept, and it'll auto append __bool__ to the end of class. For example:

```
class A(object):
    def __nonzero__(self):
        return bool(self.var)
```

It'll be converted to:

```
class A(object):
    def __nonzero__(self):
        return bool(self.var)
    def __bool__(self):
        return self.__nonzero__()
```

### octal

```
0755 -> 493
```

### (int, long)

```
isinstance(a, (int, long)) -> isinstance(a, six.integer_types)
```