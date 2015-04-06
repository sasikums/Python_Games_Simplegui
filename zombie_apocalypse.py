#http://www.codeskulptor.org/#user39_UFXf2fVhK8_13.py
"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zom in self._zombie_list:
            yield zom

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
       
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for hum in self._human_list:
            yield hum
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        checked = [blank[:] for blank in self._cells]  
        distances = [[self._grid_height*self._grid_width \
                     for dummy_cols in range(self._grid_width)]\
                     for dummy_rows in range(self._grid_height)]
        
        if entity_type == ZOMBIE:
            entity_list = self._zombie_list
        else:
            entity_list = self._human_list
        
        spread = poc_queue.Queue()
        
        for ent in entity_list:
            spread.enqueue(ent)			#enque boundary cells
            checked[ent[0]][ent[1]] = FULL #set cells with entity as
            distances[ent[0]] [ent[1]] = 0 	#full and distance to 0
                
        while len(spread)>0:
            cell = spread.dequeue()
            neighbors = self.four_neighbors(cell[0],cell[1])
            for neighbor in neighbors:
                row,col = neighbor[0],neighbor[1]
                if checked[row][col]==EMPTY:
                    checked[row][col]=FULL
                    spread.enqueue(neighbor)
                    
                    distances[row][col]=min(distances[row][col],
                                            distances[cell[0]]\
                                            [cell[1]]+1)
       
        return distances
                    
                    
        
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        
        for index,human in enumerate(self._human_list):
            #find options for humans to move
            move_options=list([human])
            near_cells=self.eight_neighbors(human[0],human[1])
            for neigh in near_cells:
                if self.is_empty(neigh[0],neigh[1]):
                    move_options.append(neigh)
            #Compare possible moves to nearest zombie to find best move
            max_dist = -10000
            best_moves=[]
           
            for move in move_options:
                if zombie_distance[move[0]][move[1]]>max_dist:
                    best_moves=list([move])
                    max_dist=zombie_distance[move[0]][move[1]] 
                elif zombie_distance[move[0]][move[1]]==max_dist:
                    best_moves.append(move)
            #final move is a random choice between best moves
            final_move=random.choice(best_moves)
            #update human position to final move
            self._human_list[index]=final_move
            
            
        
        
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for index,zombie in enumerate(self._zombie_list):
            #find options for zombies to move
            move_options=list([zombie])
            near_cells=self.four_neighbors(zombie[0],zombie[1])
            for zomb in near_cells:
                if self.is_empty(zomb[0],zomb[1]):
                    move_options.append(zomb)
            #Compare possible moves to nearest human to find best move
            min_dist = 10000
            best_moves=[]
            for move in move_options:
                if human_distance[move[0]][move[1]]<min_dist:
                    best_moves=list([move])
                    min_dist=human_distance[move[0]][move[1]]
                elif human_distance[move[0]][move[1]]==min_dist:
                    best_moves.append(move)
            #final move is a random choice between best moves
            final_move=random.choice(best_moves)
            #update human position to final move
            self._zombie_list[index]=final_move
            

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Zombie(3, 3, [], [(1, 1)], [(2, 2)]))

