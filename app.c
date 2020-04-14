#include "app.h"
#include <stdio.h>
#include "SDL2/SDL.h"
#include <time.h>
const int WINDOW_WIDTH = 400;
const int WINDOW_HEIGHT = 300;
const int map_height = 16;
const int map_width = 16;
int main(){
init();
SDL_init(components);

loop(components);
return 0;
}

void init() {
	
}
void SDL_init(struct Components components) {
	if (SDL_Init(SDL_INIT_VIDEO) < 0) {
		printf("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
	
	}
	else {
		components.window = SDL_CreateWindow("Game of Life", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_SHOWN);
	if (components.window == NULL) {
		printf("Window could not be created! SDL_Error: %s\n", SDL_GetError());

	}
}

//components.renderer=SDL_CreateRenderer(components.window, -1, SDL_RENDERER_ACCELERATED);
	components.surface = SDL_GetWindowSurface( components.window);

	SDL_FillRect(components.surface, NULL, SDL_MapRGB(components.surface->format,0xFF,0xFF,0xFF));

		
	components.tilesurface = SDL_LoadBMP("res/tile.bmp");
	
	SDL_BlitSurface (components.tilesurface, NULL, components.surface, NULL);

	SDL_UpdateWindowSurface( components.window );
}
//SDL_Surface loadMedia() {
//	SDL_Surface img;
//	img = SDL_LoadBMP("res/background.bmp");
//	if (img == NULL) {
//	printf("failed to load image");
	

//	}
//	return img;
//}
void render(struct Components components, int map[16][16]) {

//	SDL_FillRect(components.surface, NULL, SDL_MapRGB(components.surface->format,0xFF,0xFF,0xFF));

SDL_BlitSurface (components.tilesurface, NULL, components.surface, NULL);
SDL_UpdateWindowSurface(components.window);
}
void quit(){

	components.surface= NULL;
    	components.window = NULL;
    	
    	SDL_Quit();
}


void loop(struct Components components) {
	int map[16][16] = {};
	
	for (int i=0; i<map_width;i++){
		for (int j=0; j<map_width;j++){
			map[i][j] = 0;
		}

	}

	int running = 1;
	SDL_Event e;	
	while (running == 1) {
		while(SDL_PollEvent( &e ) != 0) {
			if (e.type == SDL_QUIT) {
				running = 0;
			}
		}
			
			render(components, map);
			SDL_Delay(10);
		}

			
	quit(); // from render.h
	}
