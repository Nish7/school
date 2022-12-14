# Makefile are great when our c program is built many source files
# make -f mfname target (rename Makefile)

hello: helloWorld.c # target dependencies
	gcc -o helloWorld helloWorld.c  

# make target -> before the commands are run, make [d] is run.
# if the target depencies does not exists, throws error
world: h1.c
	gcc -o hi h1
h1.c: helloWorld.c
	cp helloWorld.c h1.c

# make clean -> to clean up and start fresh
clean:
	rm h1.c hi




