map <C-J> <C-W>j<C-W>_
map <C-K> <C-W>k<C-W>_

set wmh=0

let mapleader=','
map ,w :w!<ENTER>
map ,f ifor (int ii = 0; ii < DEFINE_MAX; ++ii)<ENTER>{<ENTER>}<ESC>
map ,d istd::cout << "" << std::endl;<ESC>
