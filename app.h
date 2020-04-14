#ifndef APP_H_
#define APP_H_
#include "structs.h"
#include "SDL2/SDL.h"
struct Components{
	SDL_Surface *surface;
	SDL_Surface *tilesurface;
	SDL_Window *window;
};
struct Tile {
	int x,y;
	SDL_Surface *tilesurface;
};
struct Components components;
int main();
void init();
void loop();
void SDL_init(struct Components components);
//SDL_SURFACE loadMedia();
void quit();
void render(struct Components components, int map[16][16]);
#endif
