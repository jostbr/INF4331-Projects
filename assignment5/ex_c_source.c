
/* Silly program that utilises different parts (e.g. this multiline comment)
 of c syntax and highlighter.py' ability to syntax highlight C source code. */

# include <stdio.h>
# include <stdlib.h>
# include <stdbool.h>

// Main function that does something silly.
int main(int argc, char const *argv[]){
    char* name_of_city = 'New Mombasa';     // Define name of city to be studied
    int population = 100;                  // Set the population of this city
    int* bad_ID_tracker = malloc(sizeof(int) * (int)(population / 4));
    int bad_ID_counter = 0;          // To keep track of how many with bad ID
    bool found_odd_healthy = false;  // Keep track of find of odd healthy in popul.
    int ID;
    
    for (ID = 1; ID <= population; ID++){
        if (ID > (int)(population / 2) && (ID % 2 != 0)){
            bad_ID_tracker[bad_ID_counter] = ID;            // Store bad ID
            bad_ID_counter = bad_ID_counter + 1;            // Update bad ID counter
            printf("ID: %d - You have an unhealthy high and odd ID\n", ID);
            printf("This is the worst kind of ID; you should have it checked\n");
        }

        else if (ID < (int)(population / 2) && (ID % 2 != 0)){
            found_odd_healthy = true;
            printf("ID: %d - You have an odd ID, but at least it's healthy\n", ID);
        }

        else{
            printf("ID: %d Your ID is either unhealthy even or healthy even\n", ID);
            continue;        // Totally unescessary
        }
    }

    while (found_odd_healthy == true){
        found_odd_healthy = false;   // No reason to do this, but do it anyway

        for (ID = 1; ID < population; ID++){
            if (ID < (int)(population / 4)){
                bad_ID_tracker[ID] = 70 * ID + 10;   // Random stuff
            }
        }

        break;                       // No need to brake here, but do it anyway
    }
}
