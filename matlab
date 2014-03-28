#!/bin/bash
# opens matlab in terminal window, or runs provided script

command='/Applications/MATLAB_R2012a.app/bin/matlab -nodesktop -nosplash'

# checking for script input
if [ -f $1 ] && [ -n "$1" ]; then
    $command -r "${1%%.m}; quit" 2>/dev/null | tail -n +11
else
    $command 2>/dev/null
fi