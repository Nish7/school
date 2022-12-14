hello: hello.o hellofuncs.o
	gcc -o hello hello.o hellofuncs.o
hellofuncs.o: hellofuncs.c
	gcc -c hellofuncs.c
hello.o: hellofuncs.h hello.c
	gcc -c hello.c
clean:
	rm -f hello.o hellofuncs.o hello

# sample workflow
# 1. make hello
# 2. make changes in the hellofuncs.c
# 3. make hellofuncs.c
# 4. make hello

# sthis avoid recompiling hello.c

# Alternate: compiling each time
# hello: hello.c hellofuncs.c hellofuncs.h
# 	gcc -o hello hello.c hellofuncs.c