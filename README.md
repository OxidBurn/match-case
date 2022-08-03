# match-case
Recipes and Tricks for Effective Structural Pattern Matching in Python


## RegexEql Matching

The match/case syntax provides a lot of matching patterns out-of-the-box, but unfortunately there's currently no native way to match against regular expressions. We can however, implement it pretty easily thanks to the fact that structural pattern matching `uses == (__eq__)` to evaluate the match. Therefore, all we need is a class that implements custom `__eq__` method

## JSON Processing

Common use case for match/case is efficient matching of JSON structures in form of Python's dictionaries. This can be done with mapping pattern which is triggered by `case {...}`

## Set Membership

Similarly to RegEx matching shown earlier, we don't have an option to match against sets of values. We can however, once again take advantage of `__eq__` and implement our own set-matching class

## Matching Positional Arguments

By default, when using the class pattern to match a class such as `case MyClass(key="value"):` ..., you're required to use keyword arguments. That can however, be little verbose in case your class has many arguments. To solve this we can use `__match_args__`

## Exhaustiveness

Another hard to debug issue you might encounter stems from missing a valid branch/case - that is - when match doesn't cover all the possible cases.

