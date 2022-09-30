
 An esolang based on legendre symbols. This language is heavily based off of [Kak](https://esolangs.org/wiki/Kak).

# Spec

 ## Lexer

  The lexer only accepts the following characters:
   `(`, `/`, `)`, `0-9`.
 
  No other characters such as whitespace or alphabetic letters are allowed.
 
 ## Semantics
  A Legend program consists of `n` [legendre symbols](https://en.wikipedia.org/wiki/Legendre_symbol) of the form `(a/p)` where `a` is some positive number and `p` is an odd prime. 
  
  Each legendre symbol evaluates to `0`, `1` or `-1`. Each value corresponds to some instructions:
  | Value |                          Instruction                                      |
  | ----- |                            :----:                                         |
  | -1    | Move the pointer to the right and flip the bit at the new location        |
  | 1     | Move the pointer to the left if the pointer index is greater than one (1) |
  | 0     | Skip the next instruction if the current cell's bit is zero (0)           |
  
  Thus, every program structure has infinitely many implementations.
  
# Use

 The interpreter lies in `i.pl` (it's golfed by the way). 
 
 To run a program: `legend.exe program.leg`
 
 ## Windows
 
  Go into the directory and run this command: `swipl -o legend.exe -c i.pl --goal=main`. Now you will have a `legend.exe` which you can use like this: `legend.exe program.leg`.
  
# Example
 
 The file [hello_world.leg](hello_world.leg) contains a possibile hello world in Legend. 
 
 (Image to show the program with text wrapping)
 ![image](https://user-images.githubusercontent.com/92041779/193173700-8d5336aa-b9cc-4769-9318-df917f1d14c7.png)

 When compiled it produces a binary string:
 
 ```
 $ legend.exe hello_world.leg
 010010000110010101101100011011000110111100101100001000000101011101101111011100100110110001100100001000010
 ```
 
 *SIDE NOTE: The program [hello_gen.py](hello_gen.py) was used this generate this program randomly. It was not written by hand.*
 
 If you split this binary string into octals, it forms the ASCII text `Hello, World!`. 
 
 Proof:
 
 ![image](https://user-images.githubusercontent.com/92041779/193173857-695720ab-2cea-4bfd-9c02-b443efd060d1.png)
