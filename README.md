# smart-ls

Smart-ls is like Tinder's Smart Photos feature but for your directory!

If you post a slideshow of photos on Instagram, it will not show you on which photo people liked your post. However, Tinder's Smart Photos feature alternates the photo first seen by others when you’re shown on Tinder, notes each response as others swipe on you, and reorders your photos to show your best ones first.

I thought: "Hmm... where else can I apply this concept?" And my directories came to mind!

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

