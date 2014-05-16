//
//  llist.c
//  llist
//
//  Created by Kevin Carter on 5/13/14.
//  Copyright (c) 2014 Kevin Carter. All rights reserved.
//
#include <stdlib.h>
#include <stddef.h>
#include <memory.h>
#include "llist.h"



static int ll_link(LinkedList *list, LinkedListEntry *newentry, LinkedListEntry *previousEntry, LinkedListEntry *nextEntry);
static int ll_unlink(LinkedListEntry *entryToUnlink);



#ifdef LL_STATIC_ALLOCATION

#ifndef NUM_USER_ENTRIES
#define NUM_USER_ENTRIES 150
#endif

#define NUM_LISTS 10
#define NUM_ENTRIES NUM_USER_ENTRIES + NUM_LISTS

LinkedList freeLists={0};
LinkedList freeEntries={0};
LinkedList lists[10]={0};

LinkedListEntry entries[NUM_ENTRIES]={0};

int initializeFreeList() {
    int i;
    int retval=LL_SUCCESS;
    
    for(i=0;i<NUM_ENTRIES && retval == LL_SUCCESS;i++) {
        retval = ll_link(&freeEntries,&entries[i],(i>0?&entries[i-1]:NULL),NULL);
    }
    
    freeEntries.first=&entries[0];
    freeEntries.last=&entries[NUM_ENTRIES-1];
    
    for(i=0;i<NUM_LISTS;i++) {
        retval = (ll_append(&freeLists,&lists[i])!=NULL ? LL_SUCCESS : LL_ERR_FREELISTS_INIT_FAILED);
    }
    
    return retval;
}
#else

#endif

static int ll_link(LinkedList *list, LinkedListEntry *newentry, LinkedListEntry *previousEntry, LinkedListEntry *nextEntry) {
    int retval=LL_SUCCESS;
    if(newentry == NULL) {
        retval = LL_ERR_BAD_ENTRY;
    }
    else if(previousEntry!=NULL && previousEntry->owner!=list) {
        retval = LL_ERR_DIFFERENT_LISTS;
    }
    else if(nextEntry!=NULL && nextEntry->owner!=list){
        retval = LL_ERR_DIFFERENT_LISTS;
    }
    else if(newentry->owner!=NULL){
        retval = LL_ERR_ENTRY_ALREADY_OWNED;
    }
    else {
        
        newentry->previous=previousEntry;
        newentry->next=nextEntry;
        
        newentry->owner=list;
        
        if(previousEntry!=NULL) {
            previousEntry->next=newentry;
        }
        
        if(nextEntry!=NULL) {
            nextEntry->previous=newentry;
        }
        
        list->nodeCount++;
    }
    return retval;
}

static int ll_unlink(LinkedListEntry *entryToUnlink) {
    int retval=LL_SUCCESS;
    if(entryToUnlink!=NULL) {
        if(entryToUnlink->owner!=NULL){
            entryToUnlink->owner->nodeCount--;
            entryToUnlink->owner=NULL;
            if(entryToUnlink->previous !=NULL) {
                entryToUnlink->previous->next=entryToUnlink->next;
            }
            
            if(entryToUnlink->next!=NULL) {
                entryToUnlink->next->previous=entryToUnlink->previous;
            }
            
            entryToUnlink->next=entryToUnlink->previous=NULL;
            
        } else {
            retval=LL_ERR_ENTRY_NOT_OWNED;
        }
    } else {
        retval = LL_ERR_BAD_ENTRY;
    }
    return retval;
}

static LinkedListEntry * ll_allocEntry(void *data) {
    LinkedListEntry *newNode;
#ifdef LL_STATIC_ALLOCATION
    if(freeEntries.first!=NULL) {
        newNode = freeEntries.first;
        if((freeEntries.first=freeEntries.first->next)==NULL) {
            freeEntries.last=NULL;
        }
        ll_unlink(newNode);
    }
#else
    newNode= calloc(1,sizeof(*newNode));

#endif
    if(newNode!=NULL){
        newNode->data=data;
    }
    return newNode;
}

static void ll_releaseEntry(LinkedListEntry *entry) {
#ifdef LL_STATIC_ALLOCATION
    ll_link(&freeEntries, entry, NULL, freeEntries.first);
    if(freeEntries.last==NULL) {
        freeEntries.last=entry;
    }
#else
    free(entry);
#endif
}

static void ll_releaseList(LinkedList *list) {
#ifdef LL_STATIC_ALLOCATION
    ll_append(&freeLists, list);
#else
    free(list);
#endif
}

LinkedList *ll_create() {
#ifdef LL_STATIC_ALLOCATION
    return ll_pop(&freeLists);
#else
    return calloc(1,sizeof(LinkedList));
#endif
}

LinkedListEntry * ll_search(LinkedList *list, void * searchParam, int (sortCompareFunc)(void *, void *)) {
    LinkedListEntry *entry=NULL;
    
    if(list!=NULL && sortCompareFunc!=NULL){
        for(entry=list->first;
            entry!=NULL && !sortCompareFunc(entry->data, searchParam);
            entry=entry->next);
    }
    
    return entry;
}

LinkedListEntry *ll_append(LinkedList *list,void *data) {
    LinkedListEntry *retval=NULL;
    if(list!=NULL){
        
        if(list->first==NULL) {
            retval=list->first=list->last=ll_allocEntry(data);
            retval->owner=list;
            list->nodeCount++;
        } else {
            if(list->sortCompareFunc!=NULL){
                retval = ll_insert(list,data);
            }else{
                retval = ll_insertAfter(list->last, data);
            }
        }
        
    }
    return retval;
}

LinkedListEntry *ll_prepend(LinkedList *list,void *data) {
    LinkedListEntry *retval=NULL;
    if(list!=NULL){
        if(list->last==NULL) {
            retval=list->first=list->last=ll_allocEntry(data);
            retval->owner=list;
            list->nodeCount++;
        } else {
            if(list->sortCompareFunc!=NULL){
                retval = ll_insert(list,data);
            }else{
                retval = ll_insertBefore(list->first, data);
            }
        }
    }
    return retval;
}

LinkedListEntry *ll_insertBefore(LinkedListEntry *entry, void *data) {
    LinkedListEntry *newNode=NULL;
    if(entry!=NULL) {
        if(entry->owner->sortCompareFunc!=NULL){
            newNode = ll_insert(entry->owner,data);
        }else{
            newNode=ll_allocEntry(data);
            if(entry==entry->owner->first) {
                entry->owner->first=newNode;
            }
            
            ll_link(entry->owner,newNode, entry->previous, entry);
        }
    }
    return newNode;
}

LinkedListEntry *ll_insertAfter(LinkedListEntry *entry, void *data) {
    LinkedListEntry *newNode=NULL;
    
    
    if(entry!=NULL) {
        if(entry->owner->sortCompareFunc!=NULL){
            newNode = ll_insert(entry->owner,data);
        }else{
            newNode=ll_allocEntry(data);
            
            if(entry==entry->owner->last) {
                entry->owner->last=newNode;
            }
            
            ll_link(entry->owner,newNode,entry,entry->next);
        }
    }
    
    return newNode;
}

//LinkedListEntry *ll_insert(LinkedListEntry *entry, int insertMode, void *data) {
//    return insertMode == LL_INSERT_BEFORE?ll_insertBefore(entry, data) : ll_insertAfter(entry, data);
//}

void * ll_remove(LinkedListEntry *entry, void *(cleanupFunc)(void *)) {
    void *retval = NULL;
    if(entry!=NULL) {
        retval=entry->data;
        if(entry==entry->owner->first) {
            entry->owner->first=entry->next;
        }
        
        if(entry==entry->owner->last) {
            entry->owner->last=entry->previous;
        }
        
        ll_unlink(entry);
        ll_releaseEntry(entry);
    }
    
    return retval;
}

void ll_destroy(LinkedList *list, void *(cleanupFunc)(void *)) {
    if(list!=NULL) {
        ll_clear(list,cleanupFunc);
        ll_releaseList(list);
    }
}

void ll_clear(LinkedList *list, void *(cleanupFunc)(void *)) {
    LinkedListEntry *toDelete=NULL;
    LinkedListEntry *current;
    if(list!=NULL){
        current=list->first;
        while(current!=NULL) {
            toDelete=current;
            current=current->next;
            if(cleanupFunc!=NULL) {
                cleanupFunc(toDelete->data);
            }
            ll_unlink(toDelete);
            ll_releaseEntry(toDelete);
        }
        list->first=list->last=NULL;
        list->nodeCount=0;
    }
}

void * ll_poll(LinkedList *list) {
    void *retval=NULL;
    if(list!=NULL && list->first!=NULL) {
        retval = ll_remove(list->first,NULL);
    }
    return retval;
}

void * ll_pop(LinkedList *list) {
    void *retval=NULL;
    if(list!=NULL && list->last!=NULL) {
        retval = ll_remove(list->last,NULL);
    }
    return retval;
}

void ll_mapInline(LinkedList *list, void *mapParam, void *(mapFunc)(void *,void *)) {
    LinkedListEntry *entry;
    if(list!=NULL && mapFunc!=NULL) {
        for(entry=list->first;entry!=NULL;entry=entry->next) {
            entry->data = mapFunc(entry->data,mapParam);
        }
    }
}

void ll_filterInline(LinkedList *list, void *filterParam, int (filterFunc)(void *, void *)) {
    LinkedListEntry tempEntry;
    LinkedListEntry *entry;
    if(list !=NULL && filterFunc!=NULL) {
        for(entry=list->first;entry!=NULL;entry=entry->next) {
            if(filterFunc(entry->data,filterParam)) {
                tempEntry.next=entry->next;
                ll_remove(entry,NULL);
                entry=&tempEntry;
            }
        }
    }
}

LinkedList *ll_copy(LinkedList *list) {
    return ll_copyAdvanced(list, NULL, NULL, NULL, NULL);
}

void *defaultDeepCopyFunc(void *data,void *param) {
    return data;
}

LinkedList * ll_copyAdvanced(LinkedList *list,
                             void *filterParam,
                             int(filterFunc)(void *, void *),
                             void *deepCopyFuncParam,
                             void *(deepCopyFunc)(void *, void *)) {
    LinkedList *retval = NULL;
    LinkedListEntry *entry;
    if(list!=NULL) {
        if(deepCopyFunc==NULL) {
            deepCopyFunc=defaultDeepCopyFunc;
        }
        retval=ll_create();
        retval->sortCompareFunc=list->sortCompareFunc;
        for(entry=list->first;entry!=NULL;entry=entry->next) {
            if(filterFunc==NULL || !filterFunc(entry->data,filterParam)) {
                ll_append(retval,deepCopyFunc(entry->data,deepCopyFuncParam));
            }
        }
    }
    
    return retval;
}

LinkedList *ll_searchFindAll(LinkedList *list, void * searchParam, int (sortCompareFunc)(void *,void *)) {
    LinkedList *retval=NULL;
    LinkedListEntry *entry;
    
    int sfRes=0;
    if(list!=NULL && sortCompareFunc!=NULL) {
        retval = ll_create();
        for(entry=list->first;entry!=NULL && sfRes!=-1;entry=entry->next) {
            if((sfRes=sortCompareFunc(entry->data,searchParam))) {
                ll_append(retval, entry);
            }
        }
    }
    
    return retval;
}

int ll_assignSortFunction(LinkedList *list, int sortComparator(LinkedListEntry *[], void *)) {
    int retval = LL_SUCCESS;
    if(list!=NULL) {
        if(list->nodeCount>1) {
            retval = LL_RESORT_NOT_YET_SUPPORTED;
        }
        else {
            list->sortCompareFunc=sortComparator;
        }
    } else {
        retval = LL_NULL_LIST;
    }
    return retval;
}
LinkedListEntry *ll_insert(LinkedList *list, void *data) {
    LinkedListEntry *retval=NULL;
    LinkedListEntry *current;
    LinkedListEntry *context[3];
    int sortCompareReturn = LL_SORT_DO_NOT_INSERT_YET;
    if(list->sortCompareFunc!=NULL) {
        if(list->first==NULL) {
            retval = ll_append(list,data);
        }
        
        for(current=list->first;current!=NULL && retval == NULL;current=current->next ){
            context[0]=current->previous;
            context[1]=current;
            context[2]=current->next;
            sortCompareReturn = list->sortCompareFunc(context, data);
            if(sortCompareReturn!=LL_SORT_DO_NOT_INSERT_YET){
                retval = ll_allocEntry(data);
                
                if(sortCompareReturn == LL_SORT_INSERT_BEFORE_CURRENT) {
                    if(current==list->first){
                        list->first=retval;
                    }
                    
                    ll_link(list,retval,current->previous,current);
                    
                } else { /*insert after*/
                    if(current == list->last) {
                        list->last=retval;
                    }
                    ll_link(list,retval,current,current->next);
                }
            }
        }
    } else {
        retval = ll_prepend(list, data);
    }
    return retval;
}
