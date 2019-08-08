This Folder contains sample python programs and utilities frequently used in python projects by me.
Also Solutions to the problems attempted in the online coding sites.

# vim settings

:set nocompatible
set backspace=2
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab

filetype on
autocmd FileType python syntax on
autocmd FileType python set ai
autocmd FileType python set smartindent cinwords=if,elif,else,for,while,with,try,except,finally,def,class
autocmd FileType python set makeprg=pylint\ --reports=n\ --msg-template=\"{path}:{line}:\ {msg_id}\ {symbol},\ {obj}\ {msg}\"\ %:p
autocmd FileType python set errorformat=%f:%l:\ %m
autocmd FileType python compiler pylint

