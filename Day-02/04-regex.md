# Regex

**1. Regular Expressions for Text Processing:**

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters:
    . --> any charactor 
    * --> zero or more occurence
    + --> one or more occurence
    ? --> zero or one occurence
    
    [] --> character class --> [A-Z0-9a-z] 
    
    | --> OR operation
    
    ^ start of a line
    
    $ end of a line

    \d --> match any digit(0-9)
    
    most used re is .*
    .*  --> any charactor  with zero or more occurence 


how to define pattern?

r"mention the pattern"

ex: r".*zeomega.loc"   --> found words starts with anything but last should have  zeomega.loc

   r"^python"  -->  found words start with python 

   r"$loc"  --> found words ends with  loc

   r"[A-Z]+" --> found if starts with any letter between A to Z that is minimum one or more times
  
   r"\d+"  --> start with any digit with one or more occurence   


| **Pattern**           | **Description**                        | **Example**                     |
|-----------------------|----------------------------------------|---------------------------------|
| `.`                   | Matches any single character (except `\n`). | `r"c.t"` matches `"cat"`, `"cot"`. |
| `^`                   | Matches the start of the string.       | `r"^hello"` matches `"hello world"`. |
| `$`                   | Matches the end of the string.         | `r"world$"` matches `"hello world"`. |
| `*`                   | Matches 0 or more repetitions.         | `r"ab*"` matches `"a"`, `"ab"`, `"abb"`. |
| `+`                   | Matches 1 or more repetitions.         | `r"ab+"` matches `"ab"`, `"abb"`. |
| `?`                   | Matches 0 or 1 repetition.             | `r"ab?"` matches `"a"`, `"ab"`. |
| `[abc]`               | Matches any character in brackets.     | `r"[abc]"` matches `"a"`, `"b"`, `"c"`. |
| `\d`                  | Matches any digit (0-9).               | `r"\d+"` matches `"123"`, `"42"`. |
| `\w`                  | Matches any word character (alphanumeric + `_`). | `r"\w+"` matches `"word1"`. |
| `\s`                  | Matches any whitespace character.      | `r"\s+"` matches spaces or tabs. |
