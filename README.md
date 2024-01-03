# smart-ls

Smart-ls is like Tinder's Smart Photos feature but for your directory! (This is also NOT an endorsement of Tinder, meet people IRL instead.)

Instagram slideshows don't reveal which specific photo garnered likes. Conversely, Tinder's Smart Photos feature cleverly rotates your first photo shown to others, tracks responses, and prioritizes your most popular photos. This sparked an idea: why not apply a similar approach to organizing directory contents?

My program `smart-ls` smartly lists and sorts directory contents by their last access time, helping you quickly find the most recently used files and directories. This can be adapted to a different metric like frequency of access.

## Installation

#### Build from source

To install smart-ls, clone the repository and build from source:

```sh
$ git clone github.com/TesfaAsmara/smart-ls
$ cd smart-ls
```
## Usage

Run `python smart-ls` in your terminal to start the app. Smart-ls will display the contents of your current directory, sorted by the last access time.

