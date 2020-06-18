# Info about used plugins for vim

## Some general info

### Path to the vim settings

Getting path
```
:version
```

Common used pathes:
	* System: _/etc/vimrc_
	* User files:
		* _$HOME/.vimrc_
		* _~/.vim/vimrc_

## Plugins

### Plugin manager
I'm using default plugin manager that appeared in vim starting version 8.0. Alternatively I could use Vungle (listed in the plugins section).

To use it all plugins from git should be placed in ~/.vim/pack/alkor/start directory. Alkor may be replaced with any suitable name.

For managing setting I'm using git with private repo in [github]( https://github.com/lexa107/vim_settings). Check readme of the repo to get full info about the repo usage

### General plugins
	* Plugin manager[Currently not used]:  [Vundle](https://github.com/VundleVim/Vundle.vim)
	* Project navigation: [NERDtree](https://github.com/preservim/nerdtree)
	* Addition to project navigation to support git: [NERDtree-git](https://github.com/Xuyuanp/nerdtree-git-plugin)
	* Auto completion: [YouCompleteMe](https://github.com/ycm-core/YouCompleteMe)
	* Syntax highlighting: [Syntatic](https://github.com/vim-syntastic/syntastic)
