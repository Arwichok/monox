# MonoX - monobank api wrapper


### Install

```commandline
pip install monox
```

### Guide

```python
from monox import MonoX

async with MonoX() as mono:
    currency_info = await mono.currency()
    print(currency_info) # [Currency(a=980, b=860, date=29292929, buy=99.22, sell=89.4, cross=22.4)]
```
