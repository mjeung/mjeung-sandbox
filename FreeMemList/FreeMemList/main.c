//
//  main.c
//  freememlist
//
//  Created by Kevin Carter on 5/14/14.
//  Copyright (c) 2014 Kevin Carter. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "llist.h"

typedef struct pageDef {
    long start;
    long end;
}pageDef;

typedef enum e_commandid {
    RESERVED,
    INIT,
    ALLOCATE,
    FREE,
    PRINT
} commandId;

typedef struct commandStruct {
    char command[50];
    commandId id;
    int requiresNumericSecondArg;
} commandStruct;

commandStruct commands[] = {
    {"init",INIT,1},
    {"allocate",ALLOCATE,1},
    {"free",FREE,1},
    {"print",PRINT,0},
    {0,0,0}
};


void *pageCleanupFunc(void *page) {
//    printf("Freeing: %li\n", ((pageDef *) page)->);
    free(page);
    return NULL;
}

int sortComparator(LinkedListEntry *context[],void *newData) {
    int retval = LL_SORT_DO_NOT_INSERT_YET;
    LinkedListEntry *nextentry = context[LL_SORT_CONTEXT_NEXT];
    LinkedListEntry *currententry = context[LL_SORT_CONTEXT_CURRENT];
    
    pageDef *currentPage = currententry->data;
    pageDef *nextPage = (nextentry == NULL?NULL:nextentry->data);
    pageDef *newPage = newData;
    
    
    if(newPage->start<currentPage->start) {
        retval = LL_SORT_INSERT_BEFORE_CURRENT;
    } else if(newPage->start > currentPage->start) {
        if(nextPage==NULL || newPage->start < nextPage->start) {
            retval = LL_SORT_INSERT_AFTER_CURRENT;
        }
    }
    
//    if((int) newData < (int) currententry->data) {
//        if(previousentry==NULL || (int) newData > (int) previousentry->data) {
//            return LL_SORT_INSERT_BEFORE_CURRENT;
//        }
//    } else if((int) newData > (int) currententry->data) {
//        return LL_SORT_INSERT_AFTER_CURRENT;
//    }
    
    return retval;
}


void initializeFml(LinkedList **freeList, LinkedList **usedList,int blockCount) {
    pageDef *page;
    if(*freeList!=NULL) {
        ll_destroy(*freeList, pageCleanupFunc);
    }
    
    if(*usedList!=NULL) {
        ll_destroy(*usedList, pageCleanupFunc);
    }
    
    *freeList = ll_create();
    ll_assignSortFunction(*freeList, sortComparator);
    *usedList = ll_create();
    ll_assignSortFunction(*usedList, sortComparator);
    
    page = malloc(sizeof(*page));
    page->start=0;
    page->end=blockCount-1;
    ll_append(*freeList, page);
}

int prompt(char *buffer) {
    printf("$ ");
    return scanf("%s",buffer);
}

void *printBlock(void *data,void *param) {
    pageDef *page = (pageDef *) data;
    printf("%li-%li (size %li)\n",page->start,page->end,(page->end-page->start)+1);
    return data;
}

void printData(LinkedList *freeList, LinkedList *usedList) {
    printf("Free memory:\n\n");
    ll_mapInline(freeList, NULL, printBlock);
    
    printf("\nUsed memory:\n\n");
    ll_mapInline(usedList, NULL, printBlock);
}

int isFreeBlockBigEnough(void *data, void *param) {
    long requestedSize = *(long *) param;
    pageDef *page = (pageDef *) data;
    
    return (page->end-page->start+1) >= requestedSize;
}

int performAllocation(LinkedList *freeList, LinkedList *usedList, long requestedSize, long *acquiredAddress) {
    int retval = 1;
    pageDef *acquiredpage;
    pageDef *newPage;
    LinkedListEntry *entry = ll_search(freeList, &requestedSize, isFreeBlockBigEnough);
    
    if(entry!=NULL) {
        acquiredpage=(pageDef *)entry->data;
        newPage=malloc(sizeof(*newPage));
        newPage->start=acquiredpage->start;
        newPage->end=newPage->start+requestedSize-1;
        ll_append(usedList, newPage);
        
        acquiredpage->start+=requestedSize;
        if(acquiredpage->start > acquiredpage->end) {
            ll_remove(entry, pageCleanupFunc);
        }
        *acquiredAddress=newPage->start;
    } else {
        retval = 0;
    }
    return retval;
}

int searchForStartAddress(void *data, void *param) {
    long baseBlockAddress = *(long *)param;
    pageDef *page=(pageDef *)data;
    return page->start == baseBlockAddress;
}

int searchForEndAddress(void *data, void *param) {
    long endBlockAddress = *(long *) param;
    pageDef *page=(pageDef *)data;
    return page->end == endBlockAddress;
}

int performFree(LinkedList *freeList, LinkedList *usedList, long blockBaseAddress) {
    int retval = 1;
    long previousAdjacentAddress;
    long nextAdjacentAddress;
    pageDef *usedPage;
    pageDef *newPage;
    pageDef *previousAdjacentPage;
    pageDef *nextAdjacentPage;
    LinkedListEntry *previousAdjacentEntry;
    LinkedListEntry *nextAdjacentEntry;
    LinkedListEntry *entryToDeallocate = ll_search(usedList, &blockBaseAddress, searchForStartAddress);
    
    if(entryToDeallocate!=NULL) {
        usedPage=(pageDef *)entryToDeallocate->data;

        previousAdjacentAddress=blockBaseAddress-1;
        previousAdjacentEntry=ll_search(freeList, &previousAdjacentAddress, searchForEndAddress);
        
        if(previousAdjacentEntry) {
            previousAdjacentPage=(pageDef *) previousAdjacentEntry->data;
            previousAdjacentPage->end=usedPage->end;
            usedPage=previousAdjacentPage;
        }
        
        nextAdjacentAddress=usedPage->end+1;
        nextAdjacentEntry = ll_search(freeList, &nextAdjacentAddress,searchForStartAddress);
        
        if(nextAdjacentEntry) {
            nextAdjacentPage=(pageDef *)nextAdjacentEntry->data;
            usedPage->end = nextAdjacentPage->end;
            ll_remove(nextAdjacentEntry, pageCleanupFunc);
        }
        
        if(previousAdjacentEntry==NULL) {
            newPage=malloc(sizeof(*newPage));
            newPage->start=usedPage->start;
            newPage->end=usedPage->end;
            ll_append(freeList, newPage);
        }
        
        ll_remove(entryToDeallocate,pageCleanupFunc);
    }else {
        retval = 0;
    }
    
    return retval;
}

void executeCommand(LinkedList **freeList,
                    LinkedList **usedList,
                    commandStruct *command,
                    int numericArg){
    long acquiredAddress=0;
    switch(command->id) {
        case INIT:
            initializeFml(freeList, usedList, numericArg);
            printf("Initialization complete\n\n");
            break;
        case ALLOCATE:
            if(performAllocation(*freeList,*usedList,numericArg,&acquiredAddress)){
                printf("your address is %i\n\n",acquiredAddress);
            } else {
                printf("error, no contiguous available\n\n");
            }
            break;
        case FREE:
            if(performFree(*freeList,*usedList,numericArg)) {
                printf("ok\n\n");
            } else {
                printf("error, not an allocated block\n\n");
            }
            break;
        case PRINT:
            printData(*freeList,*usedList);
            break;
        case RESERVED:
        default:
            printf("Invalid command. Try again.\n\n");
    }
}

int main(int argc, const char * argv[])
{
    commandStruct *currentCommand=NULL;
    char command[1024];
    LinkedList *freeList=NULL;
    LinkedList *usedList=NULL;
    int blockCount;
    int i;
    int numericArg=0;
    
    while((EOF!=prompt(command))) {
        for(i=0;
            (currentCommand=&commands[i])->id!=0 && strcmp(command,commands[i].command)!=0;
            i++) {
                //Empty loop
        }
        if(currentCommand!=NULL){
            if(currentCommand->requiresNumericSecondArg) {
                scanf("%i",&numericArg);
            }
            
            executeCommand(&freeList,&usedList,currentCommand,numericArg);
        }
    }
    
    initializeFml(&freeList,&usedList, blockCount);
    
    
    
    return 0;
}

