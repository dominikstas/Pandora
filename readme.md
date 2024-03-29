# PANDORA - in development

Radioactive video game.

# Table of contents

- [Prerequisites](#prerequisites)
- [Setting up the project](#setting-up-the-project)
- [Coding style](#coding-style)
- [Useful links](#useful-links)

## Prerequisites

This project can be developed (for sure) right now only on Windows.

The dockerfile is waiting to be tested and finished.

**Development**

* Git
* Python3
* Pygame library (to install: pip install pygame)

## Setting up the project

Clone the repo with:

```
git clone https://github.com/dominikstas/Pandora.git
```

in repo use:

```
Python3 main.py 
```

to open up the game. Remember to use git pull before any work!

## Coding style and structure of files

# style

This project uses 'snake_case' and english (but I don't have working "x" letter on my windows device so sometimes i use "ks")

The ci/cd (github actions) right now is accepting every commit.

# structure

- main folder:
    - .gitignore: files that are ignored by git while commiting
    - dockerfile: docker config, waiting to be finished
    - main.py: Pandora itself
    - requirementes.txt: file with list of python libraries that user have to download
    - readme.md: this file
- .github:
    - basic.yml: github actions config
- assets:
    - audio: for sounds, music etc.
    - fonts
    - sprites: for graphic content
- configs (empty)
- scripts (code zone) 
- tests: they are really cool


## Useful links

- https://github.com/git-guides/git-commit
- https://www.pygame.org/docs/
