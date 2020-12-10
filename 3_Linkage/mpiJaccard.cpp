/******************************************************************************
* FILE: mpiJaccard.c
* DESCRIPTION:  
*   MPI Jaccard index based simmilarity matrix
*   NOTE: Based on the work of Barney,B. et al for matrix multimplication found at 
*   https://computing.llnl.gov/tutorials/mpi/samples/C/mpi_mm.c
* AUTHOR: Lemoga
*   BCEM, Universidad de los Andes, Bogotá, Colombia
******************************************************************************/
#include "mpi.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <iterator>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>

#define MASTER 0               /* taskid of first task */
#define FROM_MASTER 1          /* setting a message type */
#define FROM_WORKER 2          /* setting a message type */

/**
*       Calculates Jaccard index between two vectors
*/
double jaccard(char *v1, int rowA, int rowB, int colLen){
        int f11 = 0, f00 = 0;
        for (unsigned int j=0; j < colLen; j++){
                if(v1[rowA*colLen+j] == v1[rowB*colLen+j]){
                        if((int)v1[rowA*colLen+j]-48)//parse chart to int
                                f11++;
                        else
                                f00++;
                }
        }
        return double(f11) / double(colLen - f00);
}

int main (int argc, char *argv[]){
/****************  Define some variables for MPI process ****************/
        int numRows = atoi(argv[1]);
        int numColumns = atoi(argv[2]);
	int	numtasks,              /* number of tasks in partition */
		taskid,                /* a task identifier */
		numworkers,            /* number of worker tasks */
		source,                /* task id of message source */
		dest,                  /* task id of message destination */
		mtype,                 /* message type */
		rows,                  /* rows of matrix A sent to each worker */
		averow, extra, offset, /* used to determine rows sent to each worker */
		i, j, k, rc;           /* misc */
        char *data = new char[numRows*numColumns];
	double	c[numRows][numRows];   /* result matrix C */
	MPI_Status status;

	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&taskid);
	MPI_Comm_size(MPI_COMM_WORLD,&numtasks);
	if (numtasks < 2 ) {
		printf("Need at least two MPI tasks. Quitting...\n");
		MPI_Abort(MPI_COMM_WORLD, rc);
		exit(1);
	}
	numworkers = numtasks-1;


/**************************** master task ************************************/
	if (taskid == MASTER){
		printf("mpi_mm has started with %d tasks.\n",numtasks);
		printf("Initializing features matrix...\n");
	        std::string row;
	        std::ifstream file("matrix.txt");
	        for(int i=0; i<numRows; i++){
                for(int j=0; j<numRows; j++){
                        c[i][j]=0.0;
                }
	        }
	        for (int i = 0; i < numRows; ++i){
	                getline(file,row);
	                std::istringstream iss(row);
	                int j=0;
	                while(iss){
	                        iss >> data[i*numColumns+j];
	                        j++;
	                }
	        }
		file.close();
		printf("feature-genes matrix saved\n");
                for(int i=0;i<numRows;i++){
                        for(int j=0; j<numColumns; j++){
                                printf("%c\t", data[i*numColumns+j]);
                        }
                        std::cout <<'\n';
                }
		/* Send matrix data to the worker tasks */
		averow = numRows/numworkers;
		extra = numRows%numworkers;
	      	offset = 0;
	      	mtype = FROM_MASTER;
	      	for(dest=1; dest<=numworkers; dest++){
			rows = (dest <= extra) ? averow+1 : averow;   	
	         	printf("Sending %d rows to task %d offset=%d\n",rows,dest,offset);
		        MPI_Send(&offset, 1, MPI_INT, dest, mtype, MPI_COMM_WORLD);
	        	MPI_Send(&rows, 1, MPI_INT, dest, mtype, MPI_COMM_WORLD);
		        MPI_Send(&(data[0]), numRows*numColumns, MPI_CHAR, dest, mtype,MPI_COMM_WORLD);
		        MPI_Send(&numColumns, 1, MPI_INT, dest, mtype, MPI_COMM_WORLD);
		        offset = offset + rows;
		}
	
		/* Receive results from worker tasks */
	      	mtype = FROM_WORKER;
	      	for (int i=1; i<=numworkers; i++){
			source = i;
	         	MPI_Recv(&offset, 1, MPI_INT, source, mtype, MPI_COMM_WORLD, &status);
	         	MPI_Recv(&rows, 1, MPI_INT, source, mtype, MPI_COMM_WORLD, &status);
	         	MPI_Recv(&c[offset][0], rows*numRows, MPI_DOUBLE, source, mtype,MPI_COMM_WORLD, &status);
		        printf("Received results from task %d\n",source);
		}
	
		/* Print results */
		std::ofstream result;
		result.open("similarityMatrix.txt");
		for (int i=0; i<numRows; i++){
                        for (j=0; j<numRows; j++){
                                result << c[i][j] << '\t';
                        }
			result << '\n';
                }
		result.close();
	      	printf("******************************************************\n");
	      	printf("Result Matrix:\n");
	      	for (int i=0; i<numRows; i++){
			printf("\n"); 
	        	for (j=0; j<numRows; j++){
	            		printf("%6.2f   ", c[i][j]);
	      		}
		}
	      	printf("\n******************************************************\n");
	      	printf ("Done.\n");
   	}

/**************************** worker task ************************************/
	if (taskid > MASTER){
		mtype = FROM_MASTER;
	        MPI_Recv(&offset, 1, MPI_INT, MASTER, mtype, MPI_COMM_WORLD, &status);
		MPI_Recv(&rows, 1, MPI_INT, MASTER, mtype, MPI_COMM_WORLD, &status);
	        MPI_Recv(&(data[0]), numRows*numColumns, MPI_CHAR, MASTER, mtype, MPI_COMM_WORLD, &status);
	        MPI_Recv(&numColumns, 1, MPI_INT, MASTER, mtype, MPI_COMM_WORLD, &status);
		
		for (int i = offset; i < offset+rows; i++) {
       	        	for (int j = 0; j < numRows; j++) { 
	                        c[i][j] = jaccard(data,i,j,numColumns);
	                }
        	}

	      	mtype = FROM_WORKER;
	      	MPI_Send(&offset, 1, MPI_INT, MASTER, mtype, MPI_COMM_WORLD);
	      	MPI_Send(&rows, 1, MPI_INT, MASTER, mtype, MPI_COMM_WORLD);
	      	MPI_Send(&c[offset][0], rows*numRows, MPI_DOUBLE, MASTER, mtype, MPI_COMM_WORLD);
   	}
   	MPI_Finalize();

	delete [] data;
        return 0;
}
