# Membership Operations in Python

## Introduction

Membership operators in Python are used to check whether a value is present in a sequence or collection, such as a list, tuple, or string. The membership operators are "in" and "not in."

## List of Membership Operators

1. **in:** Returns `True` if the left operand is found in the sequence on the right.
2. **not in:** Returns `True` if the left operand is not found in the sequence on the right.

### Examples

```
#### in Operator

fruits=['apple','kiwi','banana']

checking_banana='banana' in fruits
if checking_banana:
    print('Banana is available in fruits list')

#### not in Operator

checking_orange='orange' not in fruits
if checking_orange:
    print('Orange is not available in fruits list')
```
