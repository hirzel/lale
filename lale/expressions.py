# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ast #see also https://greentreesnakes.readthedocs.io/
import astunparse
import pprint
from typing import cast, Any, Dict, List, Optional, Union

class Expr:
    _expr : ast.Expr

    def __init__(self, expr):
        #assert isinstance(expr, ast.Expr)
        self._expr = expr

    def __bool__(self) -> bool:
        raise TypeError(f'Cannot convert expression e1=`{str(self)}` to bool.'
                        'Instead of `e1 and e2`, try writing `[e1, e2]`.')

    def __eq__(self, other):
        if isinstance(other, Expr):
            comp = ast.Compare(left=self._expr, ops=[ast.Eq()],
                               comparators=[other._expr])
            return Expr(comp)
        else:
            return False

    def __ge__(self, other) -> Union[bool, 'Expr']:
        if isinstance(other, Expr):
            comp = ast.Compare(left=self._expr, ops=[ast.GtE()],
                               comparators=[other._expr])
            return Expr(comp)
        else:
            return False

    def __getattr__(self, name : str) -> 'Expr':
        attr = ast.Attribute(value=self._expr, attr=name)
        return Expr(attr)

    def __getitem__(self, key: Union[int, str, slice]) -> 'Expr':
        key_ast: Union[ast.Index, ast.Slice]
        if isinstance(key, int):
            key_ast = ast.Index(ast.Num(n=key))
        elif isinstance(key, str):
            key_ast = ast.Index(ast.Str(s=key))
        elif isinstance(key, slice):
            key_ast = ast.Slice(key.start, key.stop, key.step)
        else:
            raise TypeError(f'expected int, str, or slice, got {type(key)}')
        subscript = ast.Subscript(value=self._expr, slice=key_ast)
        return Expr(subscript)

    def __str__(self) -> str:
        return astunparse.unparse(self._expr).strip()

def count(group: Expr) -> Expr:
    call = ast.Call(func=ast.Name(id='count'), args=[group._expr], keywords=[])
    return Expr(call)

def mean(group: Expr) -> Expr:
    call = ast.Call(func=ast.Name(id='mean'), args=[group._expr], keywords=[])
    return Expr(call)

def variance(group: Expr) -> Expr:
    call = ast.Call(func=ast.Name(id='variance'), args=[group._expr], keywords=[])
    return Expr(call)

def distinct_count(group: Expr) -> Expr:
    call = ast.Call(func=ast.Name(id='distinct_count'), args=[group._expr], keywords=[])
    return Expr(call)

def day_of_month(subject: Expr, fmt:Optional[str]=None) -> Expr:
    args: List[Union[ast.Expr, ast.Str]]
    if fmt is None:
        args = [subject._expr]
    else:
        args = [subject._expr, ast.Str(s=fmt)]
    call = ast.Call(func=ast.Name(id='day_of_month'), args=args, keywords=[])
    return Expr(call)

def day_of_week(subject: Expr, fmt:Optional[str]=None) -> Expr:
    args: List[Union[ast.Expr, ast.Str]]
    if fmt is None:
        args = [subject._expr]
    else:
        args = [subject._expr, ast.Str(s=fmt)]
    call = ast.Call(func=ast.Name(id='day_of_week'), args=args, keywords=[])
    return Expr(call)

def day_of_year(subject: Expr, fmt:Optional[str]=None) -> Expr:
    args: List[Union[ast.Expr, ast.Str]]
    if fmt is None:
        args = [subject._expr]
    else:
        args = [subject._expr, ast.Str(s=fmt)]
    call = ast.Call(func=ast.Name(id='day_of_year'), args=args, keywords=[])
    return Expr(call)

def hour(subject: Expr, fmt:Optional[str]=None) -> Expr:
    args: List[Union[ast.Expr, ast.Str]]
    if fmt is None:
        args = [subject._expr]
    else:
        args = [subject._expr, ast.Str(s=fmt)]
    call = ast.Call(func=ast.Name(id='hour'), args=args, keywords=[])
    return Expr(call)

def item(group: Expr, value : Union[int, str]) -> Expr:
    args: List[Union[ast.Expr, ast.Num, ast.Str]]
    if isinstance(value, int):
        args = [group._expr, ast.Num(n=value)]
    elif isinstance(value, str):
        args = [group._expr, ast.Str(s=value)]
    else:
        raise TypeError(f'expected int or str value, got {type(value)}')
    call = ast.Call(func=ast.Name(id='item'), args=args, keywords=[])
    return Expr(call)

def max(group: Expr) -> Expr:
    call = ast.Call(func=ast.Name(id='max'), args=[group._expr], keywords=[])
    return Expr(call)

def min(group: Expr) -> Expr:
    call = ast.Call(func=ast.Name(id='min'), args=[group._expr], keywords=[])
    return Expr(call)

def minute(subject: Expr, fmt:Optional[str]=None) -> Expr:
    args: List[Union[ast.Expr, ast.Str]]
    if fmt is None:
        args = [subject._expr]
    else:
        args = [subject._expr, ast.Str(s=fmt)]
    call = ast.Call(func=ast.Name(id='minute'), args=args, keywords=[])
    return Expr(call)

def month(subject: Expr, fmt:Optional[str]=None) -> Expr:
    args: List[Union[ast.Expr, ast.Str]]
    if fmt is None:
        args = [subject._expr]
    else:
        args = [subject._expr, ast.Str(s=fmt)]
    call = ast.Call(func=ast.Name(id='month'), args=args, keywords=[])
    return Expr(call)

def replace(subject: Expr, old2new: Dict[Any, Any]) -> Expr:
    old2new_str = pprint.pformat(old2new)
    old2new_ast = ast.parse(old2new_str)
    call = ast.Call(func=ast.Name(id='replace'),
                    args=[subject._expr, old2new_ast], keywords=[])
    return Expr(call)

def sum(group: Expr) -> Expr:
    call = ast.Call(func=ast.Name(id='sum'), args=[group._expr], keywords=[])
    return Expr(call)

it = Expr(ast.Name(id='it'))
