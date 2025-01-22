X = 3
Y = 4 # test123
main: 
    li $v0, 1
    li $a0, 69
    syscall
    li $v0, 11
    li $a0, '\n'
    syscall
