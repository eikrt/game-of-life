OBJS = app.c

CC = gcc


LINKER_FLAGS = -lSDL2
OBJ_NAME = application
all : $(OBJS)
	$(CC) $(OBJS) $(COMPILER_FLAGS) $(LINKER_FLAGS) -o $(OBJ_NAME)

