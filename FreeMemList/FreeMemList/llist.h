//
//  llist.h
//  llist
//
//  Created by Kevin Carter on 5/13/14.
//  Copyright (c) 2014 Kevin Carter. All rights reserved.
//

#ifndef llist_llist_h
#define llist_llist_h

#ifdef LL_STATIC_ALLOCATION
int initializeFreeList();
#else
#define initializeFreeList() LL_SUCCESS
#endif

#define LL_SORT_INSERT_BEFORE_CURRENT 0
#define LL_SORT_INSERT_AFTER_CURRENT 1
#define LL_SORT_DO_NOT_INSERT_YET 2

#define LL_SORT_CONTEXT_PREVIOUS 0
#define LL_SORT_CONTEXT_CURRENT 1
#define LL_SORT_CONTEXT_NEXT 2


#define LL_SUCCESS 0
#define LL_ERR_DIFFERENT_LISTS 1
#define LL_ERR_ENTRY_ALREADY_OWNED 2
#define LL_ERR_BAD_ENTRY 3
#define LL_NULL_LIST 4
#define LL_ERR_FREELISTS_INIT_FAILED 5
#define LL_ERR_ENTRY_NOT_OWNED 6
#define LL_RESORT_NOT_YET_SUPPORTED 999


typedef struct LinkedListEntry LinkedListEntry;
typedef struct LinkedList LinkedList;

struct LinkedListEntry {
    LinkedListEntry *next;
    LinkedListEntry *previous;
    LinkedList *owner;
    void *data;
};

struct LinkedList {
    LinkedListEntry *first;
    LinkedListEntry *last;
    long nodeCount;
    int (*sortCompareFunc)(LinkedListEntry *[], void *);
};

LinkedList *ll_create();

/*
 * Calls ll_clear and then frees the list.
 *
 * See ll_clear for cleanupFunc notes.
 */
void ll_destroy(LinkedList *list, void *(cleanupFunc)(void *));

/*
 * Walks the list until searchFunc returns 1. A reaturn of 1 from
 * searchFunc indicates the item desired has been found ,searchFunc
 * will be passed the LinkedListEntry.data member for evaluation as
 * the first argument and the searchParam argument as the second.
 * ll_search will return NULL if list is NULL, searchFunc is NULL,
 * or if the item cannot be located. If the item is located, the
 * entry containing the item is returned.
 */
LinkedListEntry *ll_search(LinkedList *list, void * searchParam, int (searchFunc)(void *,void *));

/*
 * Will iterate over the entire list applying searchFunc to each
 * element. If searchFunc returns 1 the element is added to the
 * returned list, 0 it will not. If searchFunc returns -1 the
 * element will be considered a match but the search will be
 * subsequently halted and the result list returned.
 * 
 * The LinkedListEntry.data pointer will contain pointers to 
 * each matching LinkedListEntry in the original list. When the 
 * returned list is destroyed ll_destroy should be called with a 
 * NULL cleanupFunc.
 */
LinkedList *ll_searchFindAll(LinkedList *list, void * searchParam, int (searchFunc)(void *,void *));

LinkedListEntry *ll_append(LinkedList *list,void *data);
LinkedListEntry *ll_prepend(LinkedList *list,void *data);
//LinkedListEntry *ll_insert(LinkedListEntry *entry, int insertMode, void *data);
LinkedListEntry *ll_insertBefore(LinkedListEntry *entry, void *data);
LinkedListEntry *ll_insertAfter(LinkedListEntry *entry, void *data);

int ll_assignSortFunction(LinkedList *list, int sortComparator(LinkedListEntry *[],void *));
LinkedListEntry *ll_insert(LinkedList *list, void *data);


/*
 * cleanupFunc is optional; if supplied it will be called against the
 * LinkedListEntry.data member prior to entry deallocation. The return
 * value of cleanupFunc will be returned by ll_remove if cleanupFunc
 * is supplied otherwise the value in LinkedListEntry->data is returned.
 */
void * ll_remove(LinkedListEntry *entry, void *(cleanupFunc)(void *));

/*
 * Removes the item from the head of the list and returns the object
 * pointed to by LinkedListEntry.data. Returns NULL on empty list.
 */
void * ll_poll(LinkedList *list);

/*
 * Removes item from the tail of the list and returns the object
 * pointed to by LinkedListEntry.data. Returns NULL on empty list.
 */
void * ll_pop(LinkedList *list);

/*
 * cleanupFunc is optional; if supplied it will be called against the
 * LinkedListEntry.data member prior to entry deallocation. The return
 * value of cleanupFunc is ignored in this case.
 */
void ll_clear(LinkedList *list, void *(cleanupFunc(void *)));

/*
 * Applies mapFunc to every element contained in list. The pointer
 * LinkedListEntry.data will be assigned to the return value of mapFunc.
 * The first argument to mapFunc will be LinkedListEntry.data and the
 * second will be mapParam.
 */
void ll_mapInline(LinkedList *list, void *mapParam, void *(mapFunc)(void *,void *));

/*
 * Applies filterFunc to every element in list. If filterFunc returns 1
 * the element will be removed. If cleanup on the data contained in the
 * list entry (LinkedListEntry.data) filterFunc must perform the 
 * cleanup operation before it returns. The first argument to 
 * filterFunc will be the pointer LinkedListEntry.data and the second
 * will be filterParam.
 */
void ll_filterInline(LinkedList *list, void *filterParam, int (filterFunc)(void *, void *));

/*
 * Equivalent to ll_copyAdvanced(list,NULL,NULL,NULL,NULL). Chances
 * are that unless you are actually storing primatives in .data
 * rather than a malloc'd pointer you probably don't want this.
 */
LinkedList *ll_copy(LinkedList *list);

/*
 * Copy advanced allows for filtered and/or data-specific deep copies.
 *
 * If filterFunc is supplied only items for which it returns 0 will
 * be included in the new list (returning 1 indicates that the item
 * should be filtered). The first parameter passed to filterFunc 
 * will be the LinkedListEntry.data of the entry being evaluated; 
 * the second parameter will be filterParam.
 *
 * deepCopyFunc, if supplied, allows for custom behavior for
 * copying LinkedListData.data. The return value of deepCopyFunc
 * will be assigned to the element in the new list. The first
 * parameter passed to deepCopyFunc will be the 
 * LinkedListEntry.data element to be copied and the second will
 * be deepCopyFuncParam. If deepCopyFunc is not supplied the
 * LinkedListEntry.data pointer will simply be copied to the new
 * list.
 *
 * Please note that the filter is applied to the original list's
 * data not on the data that deepCopyFunc produces.
 */
LinkedList * ll_copyAdvanced(LinkedList *list,
                     void *filterParam,
                     int(filterFunc)(void *, void *),
                     void *deepCopyFuncParam,
                     void *(deepCopyFunc)(void *, void *));

#endif
