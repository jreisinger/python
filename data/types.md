Data types:

    Name           Example               Note
    ------         -------               -----
    list           [ 1, 3.4, 'hello' ]   array in Perl
    dictionary     { 'a': 3, 'b': 42 }   dict in Python slang
    tuple          ( 10, 20, 30 )        immutable list, parens are optional
    set            { "a", "b", "c" }     dict without values

List comprehension

    [ <expression> for <item> in <iterable> ]
    nums = [number for number in range(1,6)]

    [ <expression> for <item> in <iterable> if <condition> ]
    even_nums = [number for number in range(1,6) if number % 2]

Dictionary comprehension

    { <key_expression> : <value_expression> for <expression> in <iterable> }
    word = 'letters'
    letter_counts = {letter : word.count(letter) for letter in word}

Set comprehesion

    { <expression> for <expression> in <iterable> }

Generator comprehension (tuples do not have comprehensions!)
    
    generator_object = (number for number in range(1, 6))

    for number in generator_object:
        print(number)
    number_list = list(generator_object)


A generator can be run only once. Lists, sets, strings, and dicts exist in
memory, but a generator creates its values on the fly and can't be restarted.
