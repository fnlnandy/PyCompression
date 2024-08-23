# PyTxtComp
`PyTxtComp` is a Python project that allows one to compress text into a "smaller" size in most cases.

# Logic
What the script does is simple, it reads text in a file, gathers the `15` most used characters to code on 4 bits (instead of 8). It then writes a header for the decompressor to parse eventually, and starts encoding each character.

When decompressing, the script will read that header and decode each byte accordingly.

# Usage
The script, as stated above, has two modes:
|Argument|Mode|
|--------|----|
|-c|Compression|
|-d|Decompression|

For now, `-c` takes precedence on `-d`, meaning that once you specify `-c` it will default in compression mode.

To run it, you can input:
```shell
$ python main.py -c # Or python3
$ python main.py -d # Or python3
```

# To-do
- [ ] Use `argparse`/`optparse`.
- [ ] Parse the file name from the arguments as well.
- [ ] Make it so that the user doesn't have to output the destination file.