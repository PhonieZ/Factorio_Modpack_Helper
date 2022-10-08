# Factorio Modpack Helper
This is a program that helps in making modpacks for Factorio.

## What Exactly This Program Does
This modpack helper program streamlines the long winded and 
tedious process of pasting every single mod into the dependencies
portion of your info.json file, by letting you just paste the 
raw links of the mods you want in your modpack into the input
file. This modpack helper program then processes these links, 
and spits out a ready to use dependencies array in the output 
file (even with support to mark mods as incompatible or as 
optional).

## Usage
First, run the modpack_helper.exe if on Windows (or run the py 
file in the bin folder if on mac), and an input and output txt
file will be created.

Next, paste all the links to the mods you want to add to your
modpack in the input file. If you want to mark a mod as optional, 
you should add a question mark in front of the link to mark it as 
optional, and if you want to mark it as incompatible, you should 
an exclamation mark in front of the link to mark it as incompatible.

Finally, now run the program again, and in the output file an array
of dependencies should be generated for you to put in your modpack's
info.json file, you are now done!
