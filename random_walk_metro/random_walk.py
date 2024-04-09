import terrain_gen # my terrain gen file
# implement random walk



class grid_walk():
    def __init__(self, grid: list[list[float]]):
        self.grid = grid
        self.xy_t: tuple[float] = (0,0)


    def walk_single_step(self):
        return None
    

    def walk(self) -> None:
        return None



def main():
    grid = terrain_gen.get_grid()
    terrain_gen.plot_grid(grid)
    return None

if __name__ == '__main__':
    main()