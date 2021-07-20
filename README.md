<div align="center">
    <img src="https://i.imgur.com/ey5K0zG.png" width="">
</div>

<div align="center">
    <a href="https://github.com/Ahmed-Khaled-dev/modern-meerkats/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/License-MIT-green.svg">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg">
    </a>
</div>

## 📒 Table Of Contents
- [About](#🔰-about)
- [Frameworks](#📚-frameworks)
- [Setup](#🔌-setup)
  * [Installation](#installation)
  * [Running the game](#running-the-game)
  * [Executing the commands](#executing-the-commands)
- [Team Members](#🧑💻-team-members)
- [File Structure](#📁-file-structure)

### 🔰 About
All recent games have been about moving with WASD or jumping around or shooting, anything that is direct and easy and simple and ~~fun~~, what if we forced you to think inside A box and come up with some commands that do all the movement for you? So we introduce to you the **Inside The Box Adventure.**

### 📚 Frameworks
<a href="https://blessed.readthedocs.io/en/latest/intro.html">
    <img src="https://img.shields.io/badge/Made%20with-Blessed-1f425f.svg">
</a>
<a href="https://asciimatics.readthedocs.io/en/stable/">
    <img src="https://img.shields.io/badge/Made%20with-Asciimatics-1f425f.svg">
</a>

### 🔌 Setup
- #### Installation
`pip install -r requirements.txt`

- ##### Running the game
`python main.py`

- ##### Executing the commands
`press the INSERT (INS) key`


### 🧑💻 Team members:
- <img align="centre" alt="github" width="20px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/600px-Octicons-mark-github.svg.png" /> Ahmed-Khaled-dev - <img align="centre" alt="github" width="20px" src="https://discord.com/assets/3437c10597c1526c3dbd98c737c2bcae.svg" /> Akayiz#0101 **(Team leader)**
- <img align="centre" alt="github" width="20px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/600px-Octicons-mark-github.svg.png" /> fliepeltje - <img align="centre" alt="github" width="20px" src="https://discord.com/assets/3437c10597c1526c3dbd98c737c2bcae.svg" /> donatas#7996
- <img align="centre" alt="github" width="20px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/600px-Octicons-mark-github.svg.png" /> kcaashish - <img align="centre" alt="github" width="20px" src="https://discord.com/assets/3437c10597c1526c3dbd98c737c2bcae.svg" /> 54bwy#4526
- <img align="centre" alt="github" width="20px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/600px-Octicons-mark-github.svg.png" />  Sai-Shashank - <img align="centre" alt="github" width="20px" src="https://discord.com/assets/3437c10597c1526c3dbd98c737c2bcae.svg" /> greninja#8100
- <img align="centre" alt="github" width="20px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/600px-Octicons-mark-github.svg.png" />  A-erospace - <img align="centre" alt="github" width="20px" src="https://discord.com/assets/3437c10597c1526c3dbd98c737c2bcae.svg" /> _ASP#0567

### 📁 File Structure:
```.
│   .gitignore
│   .pre-commit-config.yaml
│   dev-requirements.txt
│   LICENSE
│   main.py
│   Makefile
│   README.md
│   requirements.txt
│   tox.ini
│   tree.txt
│  
├───.github
│   └───workflows
│           lint.yaml
│  
├───app
│   │   constants.py
│   │   __init__.py
│   │  
│   ├───actions
│   │   │   move.py
│   │   │   wait.py
│   │   │   __init__.py
│   │  
│   ├───entities
│   │   │   exit.py
│   │   │   moving_wall.py
│   │   │   patrol.py
│   │   │   player.py
│   │   │   utils.py
│   │   │   wall.py
│   │   │   __init__.py
│   │  
│   ├───levels
│   │   │   level_0.py
│   │   │   level_1.py
│   │   │   level_2.py
│   │   │   level_3.py
│   │   │   __init__.py
│   │  
│   ├───menus
│   │   │   gameover_menu.py
│   │   │   start_menu.py
│   │   │   victory_menu.py
│   │   │   warning_menu.py
│   │  
│   ├───screens
│   │   │   level.py
│   │  
│   ├───types
│   │   │   events.py
│   │   │   hitbox.py
│   │   │   state.py
│   │   │   __init__.py
│   │  
│   ├───windows
│   │   │   cmd_help.py
│   │   │   cmd_list.py
│   │   │   map.py
│   │   │   user_input.py
│   │   │   utils.py
│  
├───main
│  
├───tests
│   │   test_actions.py
│   │   test_level.py
│   │   test_player.py
│   │  
│   └───entities
│           test_moving_wall.py
│           test_utils.py
```
