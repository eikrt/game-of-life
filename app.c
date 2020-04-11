#include "app.h"
#include <stdio.h>
#include "SDL2/SDL.h"

const int WINDOW_WIDTH = 400;
const int WINDOW_HEIGHT = 300;

int main(){
SDL_Renderer *renderer;
SDL_Window *window;
if (SDL_Init(SDL_INIT_VIDEO) < 0) {
	printf("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());

}
else {
	window = SDL_CreateWindow("Game of Life", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_SHOWN);
if (window == NULL) {
	printf("Window could not be created! SDL_Error: %s\n", SDL_GetError());

renderer=SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
loop();

}
return 0;
}

}
void render() {

}
void quit(){


}
void loop() {
	int running = 1;
	SDL_Event e;	
	while (running == 1) {
		while(SDL_PollEvent( &e ) != 0) {
			if (e.type == SDL_QUIT) {
				running = 0;
			}
		}
			printf("shit");
			render(); // from render.h
		}

	
	quit(); // from render.h
	}
