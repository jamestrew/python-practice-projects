/**********************************************************
 *              APS106 GROUP PROJECT                      *
 *                                                        *
 *      James Trew              999640508                 *
 *      Mark Henderson          999754163                 *
 *      Aerrow Ghanbaryfar      999550971                 *
 *                                                        *
 *      Programmed on Windows                             *
 **********************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <windows.h>

/************************************************************
 *      DECLARATION OF GLOBAL VARIABLES                     *
 ************************************************************/

#define INVALID 0
#define VALID 1

#define RANDOM 1
#define FROM_FILE 2
#define EXIT_GAME 3

#define COMPUTER 1
#define INTERACTIVE 2

//functions for various in-game options
int get_board_option();
int get_board_size();
int get_play_mode();

void grid_gen();
void print_grid();

int read_board_from_file();
int interactive_play();
int computer_play();
int moves_possible();
int get_coord(); //gets coordinates from user
void calculate_coord();
int check_coord(); //checks that the chosen letter is valid
int elimination(int y, int x);
void shiftAll();
void shift(int ground); //assists in shiftALL() function
void collapseAll();
void collapse(int ground, int x); //assists in collapseALL() function
int write_log_file();


int entries=0, board_option, play_option;
char array[36][36];//actual array
int check[36][36];//used to calculate; 0 for not checked 1 for checked
char column[36];
char board_line[100];
char c;
int iRowSize, iColSize, rCoord, cCoord;
char file_name[13];
int score, finscore;
int calcscore;
int i, j, n;
int check_column;
int count=0;

FILE *board_file;
FILE *CheckOutLineLog;

/************************************************************
 *      MAIN                                                *
 ************************************************************/

int main(){
    get_board_option(); //gets board option
    if (board_option==RANDOM) {
        get_board_size(); //gets board size and generates board
        grid_gen();
    }
    if (board_option==FROM_FILE) { //gets board from file
        read_board_from_file();
    }
    if (board_option!=EXIT_GAME) {
        get_play_mode();
        if (play_option!=EXIT_GAME) {write_log_file();} //begins game (eiter mode) and begins printing to CheckOutLineLog
        if (play_option==COMPUTER) {computer_play();}
        if (play_option==INTERACTIVE) {interactive_play();}
        if (play_option!=EXIT_GAME) {fprintf(CheckOutLineLog, "END");} //finishes printing to CheckOutLineLog
    }
    fclose(CheckOutLineLog); //closes file
    fclose(board_file);
    system("cls");
    printf(" \tC H E C K  O U T   L I N E \n\n");
    printf("\n\tTHANK YOU FOR PLAYING\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    return 0;
}

//DONE
/********************************************************************
 *      GET BOARD OPTION                                            *
 ********************************************************************/
int get_board_option(){

   entries=INVALID;
   while (entries==INVALID) {
        system("cls"); //clears the console
        printf(" \tC H E C K  O U T   L I N E \n\n");
        printf("Please select option for generating board: \n"); //instructions
        printf("1. Generate random grid \n");
        printf("2. Get grid from file \n");
        printf("3. Exit game\n");
        printf("Enter option: ");
        scanf("%d", &board_option); //reads input
        if (board_option==RANDOM || board_option==FROM_FILE || board_option==EXIT_GAME){ //validates input
            entries=VALID;
        }
        else{
            printf("\nPlease enter a valid option. \n\n");
            system("pause");
        }
    }

    system("cls");
    return 0;
}

//DONE
/***************************************************************************
 *      GET BOARD SIZE                                                     *
 ***************************************************************************/
int get_board_size(){
   entries=INVALID;
   while (entries==INVALID){
        system("cls");
        printf(" \tC H E C K  O U T   L I N E \n\n");
        printf("Please specify the size of the board (eg 3 4 for 3x4): "); //instructions
        scanf("%d %d", &iRowSize, &iColSize);
        if (iRowSize>0 && iColSize>0 && iRowSize<37 && iColSize <37){ //validates input
            entries=VALID;
        }
        else{
            printf("Please enter valid numbers. Number of rows and columns must: \n");
            printf("    a) Be greater than 0 \n    b) Not be greater than 35\n\n");
            system("pause");
        }
    }
    return 0;
}

//DONE
/*************************************************************************
 *      RANDOM BOARD GENERATION AND STORAGE                              *
 *************************************************************************/
void grid_gen(){ //generation of grid
    srand((unsigned)time(NULL)); //call this function once; it "seeds" the RNG

    for (i=0; i<iRowSize; ++i){
        for (j=0; j<iColSize; ++j){
            int iColor;

            iColor=rand()%4+1; //generating random number (1 through 4)
            char cColor;

            switch (iColor) { //converting random numbers into letters (g, r, y, b)
            case 1: cColor ='g';
                break;
            case 2: cColor='r';
                break;
            case 3: cColor= 'y';
                break;
            case 4: cColor= 'b';
                break;
            }
            array[i][j]=cColor; //storing the random letters
        }
    }
}

//DONE
/************************************************************************
 *      PRINT BOARD                                                     *
 ************************************************************************/
void print_grid(){ //printing the letters stored in the array
    int c, k=55;
    system("cls");
    printf(" \tC H E C K  O U T   L I N E");
    printf("\n\n");

    for (i=0; i<iRowSize; ++i){
        if (iRowSize-1-i>9)
        {
        printf("%c ", iRowSize-(i+1)+k); //prints out y-axis borders from Z-A
        }

        else{
        printf("%d ", iRowSize-i-1); //prints out y-axis borders from 9-0
        }

        for (j=0; j<iColSize; ++j){
            printf(" %c", array[iRowSize-1-i][j]); //printing out letters
        }
        printf("\n");
    }
    printf("\n");
    printf("  ");
    for (c=0; c<iColSize; ++c){ //prints x-axis boarders 0 through Z
        if (c>9){
            printf(" %c", c+k);
        }

        else
            printf(" %d", c);
    }

    printf("\n");

}

//DONE

/************************************************************************
 *      READING BOARD FROM A FILE                                       *
 ************************************************************************/
int read_board_from_file(){
    char tmp[100];
    entries=INVALID;
    while (entries==INVALID) {
        system("cls");
        printf("Please enter a file name (xxxxxxxxx.yyy): ");
        scanf("%s", file_name); //scans file name
        board_file=fopen(file_name, "r");
        if (board_file ==NULL){ //check that file exists
            printf("\nThat file name does not exist. Try Again\n");
            system("pause");
            entries=INVALID;
        }
        else{ //once file existance is confirmed, reads file
            fgets(tmp,100,board_file);//first line is row col
            sscanf(tmp, "%d %d", &iRowSize, &iColSize); //gets the number of cols and rows from file
            for (i=0; i<iRowSize; ++i){ //reads the characters and stores them into an array
                fgets(tmp,100,board_file);
                for (j=0; j<iColSize; ++j)
                    array[iRowSize-1-i][j]=tmp[j];
            }
            entries=VALID;
        }
    }
    return 0;
}

//DONE
/***************************************************************************
 *      PLAY MODE OPTION                                                   *
 ***************************************************************************/
int get_play_mode(){
    entries=INVALID;
    while (entries==INVALID){
        print_grid();
        printf("\n\nPlease select option for playing the game: \n"); //instructions

        printf("1. Computer play\n");
        printf("2. Interactive play\n");
        printf("3. Exit game\n");
        printf("Enter option: ");
        scanf("%d", &play_option); //reads input

        if (play_option==COMPUTER || play_option==INTERACTIVE || play_option==EXIT_GAME){ //validates input
            entries=VALID;
        }
        else{
            printf("\nPlease enter a valid option. \n");
            system("pause");
        }
    }
    return 0;
}
//DONE
/***************************************************************
 *      INTERACTIVE PLAY                                       *
 ***************************************************************/
int interactive_play(){
    score=0;
    finscore=0;
    while (moves_possible()==VALID) {
        get_coord(); //gets the coordinates that the player wants to delete
        n=0;
        elimination(rCoord, cCoord);
        collapseAll();
        shiftAll();
        get_score();
    }
    print_grid();
    get_score();
    printf("\n\nInteractive Game is over... you got %d points\n\n", finscore);
    fprintf(CheckOutLineLog, "%d %d %d\n", rCoord, cCoord, finscore);
    system("pause");
    return 0;
}


/***************************************************************
 *      COMPUTER PLAY                                          *
 ***************************************************************/
int computer_play(){
    score=0;
    finscore=0;

    while (moves_possible()==VALID){
        calculate_coord(); //gets the coordinates that will maximize points
        print_grid();
        printf("SELECTED: \nRow: %d\nColumn: %d\n",rCoord,cCoord);
        n=0;
        elimination(rCoord, cCoord);
        collapseAll();
        shiftAll();
        get_score();
        printf("\tSCORE: %d\n", finscore);
        fprintf(CheckOutLineLog, "%d %d %d\n",rCoord,cCoord,finscore);
        system("pause");
    }
    print_grid();

    printf("\n\nComputer Mode is over... Computer got %d points\n\n", finscore);
    system("pause");
    return 0;
}
//DONE
/*************************************************************************
 *      CHECK TO QUIT                                                    *
 ************************************************************************/
int moves_possible(){
    int a,b;
    for(a=0;a<iRowSize;a++){
        for(b=0;b<iColSize;b++){
            if(array[a][b]!=' '){
                if((a>0&&array[a-1][b]==array[a][b])||(a<(iRowSize-1)&&array[a+1][b]==array[a][b])||
                        (b>0&&array[a][b-1]==array[a][b])||(b<(iColSize-1)&&array[a][b+1]==array[a][b])){
                    return VALID;
                }
            }
        }
    }

    return INVALID;
}


/**********************************************************************
 *      GET COORDINATES                                               *
 **********************************************************************/
int get_coord()
{
    char a, b; //a=rCoord, b=cCoord
    entries=INVALID;
    while (entries==INVALID){
        count++;
        if (count>1){
            fprintf(CheckOutLineLog, "%d %d %d\n", rCoord, cCoord, finscore);
        }
        system("cls");
        print_grid();
        printf("\tSCORE: %d\n", finscore);
        printf("Select coordinates of the letter you want to delete\n");

        printf("Row: ");
        scanf("%d",&rCoord);

        printf("Column: ");
        scanf("%d",&cCoord);

        if (rCoord>iRowSize || rCoord<0 || cCoord>iColSize || cCoord<0){
            printf("Coordinates are outside of the board\n");
            entries=INVALID;
            system("pause");
        }
        else if(array[rCoord][cCoord]==' '){
            printf("No valid color\n");
            system("pause");
            entries=INVALID;
        }
        else if((rCoord>0&&array[rCoord-1][cCoord]==array[rCoord][cCoord])||(rCoord<(iRowSize-1)&&array[rCoord+1][cCoord]==array[rCoord][cCoord])||
                (cCoord>0&&array[rCoord][cCoord-1]==array[rCoord][cCoord])||(cCoord<(iColSize-1)&&array[rCoord][cCoord+1]==array[rCoord][cCoord]))
            entries=VALID;
        else{
            printf("Not a possible choice\n");
            system("pause");
        }
    }
    return 0;
}

/***************************************************************
 *      COMPUTER CALCULATION                                   *
 ***************************************************************/
void calculate_coord(){
    int y, x;
    calcscore=0;
    int maxscore=0;
    for(y=0;y<iRowSize;++y)
        for(x=0;x<iColSize;++x)
            check[y][x]=0;

    for (y=0;y<iRowSize;++y){
        for(x=0;x<iColSize;++x){
            if(array[y][x]!=' '&&check[y][x]==0){
                calcscore=0;
                calculate_score(y,x);
                if(calcscore>maxscore){
                    maxscore=calcscore;
                    rCoord=y;
                    cCoord=x;
                }
            }
        }
    }
}

void calculate_score(int y,int x){
    calcscore=calcscore+1;
    char temp = array[y][x];
    check[y][x] = 1;
    if(x>0&&array[y][x-1]==temp&&check[y][x-1]==0){calculate_score(y,x-1);}
    if(x<iRowSize-1&&array[y][x+1]==temp&&check[y][x+1]==0){calculate_score(y,x+1);}
    if(y>0&&array[y-1][x]==temp&&check[y-1][x]==0){calculate_score(y-1,x);}
    if(y<iColSize-1&&array[y+1][x]==temp&&check[y+1][x]==0){calculate_score(y+1,x);}
    return;
}


//DONE
/****************************************************************************
 *      ELIMINATION                                                         *
 ****************************************************************************/
int elimination(int y, int x){
    n=n+1;
    char temp = array[y][x];
    array[y][x] = ' ';

    if(x>0&&array[y][x-1]==temp){elimination(y,x-1);}
    if(x<iRowSize-1&&array[y][x+1]==temp){elimination(y,x+1);}
    if(y>0&&array[y-1][x]==temp){elimination(y-1,x);}
    if(y<iColSize-1&&array[y+1][x]==temp){elimination(y+1,x);}
    return;
}


//DONE
/***************************************************************
 *      GET SCORE                                              *
 ***************************************************************/
int get_score(){
   score=n;
   finscore+=pow(score, 2);
   //printf("eliminated: %d\n", score);
   //printf("SCORE: %d\n\n", finscore);
   //fprintf(CheckOutLineLog, "%d %d %.0f\n", rCoord, cCoord, finscore);
   n=0;
   return 0;
}


//DONE
/***************************************************************
 *      COLLAPSE COLUMNS LIKE VIRTUAL GRAVITY                   *
 ****************************************************************/
void collapseAll(){
    int a;
    for(a=0;a<iColSize;++a)
        collapse(0,a);
}


void collapse(int ground, int x){
   if(ground>iRowSize-1)//too high
       return;
   if(array[ground][x]!=' '){//something is in this point -> check what is above it
       collapse(ground+1,x);
       return;
   }
   //the point is a space - check if there is anything above it "floating"
   int a,b;
   b=iRowSize;
   for(a=ground;a<iRowSize;++a){
       if(array[a][x]!=' '){
           b=a;
           break;
       }
   }
   if(b!=iRowSize){//something is above ground at b
       for (a=0;a+b<iRowSize;++a){
           array[ground+a][x]=array[b+a][x];//bring down and replace with a ' '
           array[b+a][x]=' ';
       }
       collapse(ground+1,x);
   }
   return;//nothing above ground - return
}

//DONE
/****************************************************************
 *      SHIFT EMPTY COLUMNS LEFT                                *
 ****************************************************************/
void shiftAll(){
    shift(0);
}


void shift(int ground){
    if(ground>iColSize)
        return;
    if(array[0][ground]!=' '){
        shift(ground+1);
        return;
    }

   //the point is a space - check if there is anything above it "floating"
   int a,b,tmp;
   b=iColSize;
   for(a=ground;a<iColSize;++a){
       if(array[0][a]!=' '){
           b=a;
           break;
       }
   }
   if(b!=iColSize){//something is above ground at b
       for (a=0;a+b<iColSize;++a){
           for(tmp=0;tmp<iRowSize;++tmp){
               array[tmp][ground+a]=array[tmp][b+a];//bring down and replace with a ' '
               array[tmp][b+a]=' ';
           }
       }
       shift(ground+1);
   }
   return;//nothing above ground - return
}


//DONE
/***************************************************************
 *      WRITING LOG FILE                                        *
 ****************************************************************/
int write_log_file(){
    int k=55;
    int c;
    CheckOutLineLog=fopen("CheckOutLineLog.txt", "w");
    fprintf(CheckOutLineLog, "James Trew,              999640508\n");
    fprintf(CheckOutLineLog, "Mark Henderson,          999754163\n");
    fprintf(CheckOutLineLog, "Aerrow Ghanbaryfar,      999550971\n");
    fprintf(CheckOutLineLog, "\n%d %d\n", iRowSize, iColSize);
    for (i=0; i<iRowSize; ++i) {
        if (iRowSize-i-1>9) {
            fprintf(CheckOutLineLog, "%c ", iRowSize-(i+1)+k); //prints out y-axis borders from Z-A
        }
        else {
            fprintf(CheckOutLineLog, "%d ", iRowSize-i-1); //prints out y-axis borders from 9-0
        }

        for (j=0; j<iColSize; ++j) {
            fprintf(CheckOutLineLog, " %c", array[iRowSize-1-i][j]); //printing out letters
        }
        fprintf(CheckOutLineLog, "\n");
    }
    fprintf(CheckOutLineLog, "\n  ");
    for (c=0; c<iColSize; ++c) {
        if (c>9) {
            fprintf(CheckOutLineLog, " %c", c+k); //prints out x-axis borders from A-Z
        }
        else {
            fprintf(CheckOutLineLog, " %d", c);//prints out x-axis borders from 0=9
        }
    }
    fprintf(CheckOutLineLog, "\n\n");
    fprintf(CheckOutLineLog, "START\n");

    return 0;
}

