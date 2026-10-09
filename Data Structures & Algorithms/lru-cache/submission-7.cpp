/*
    Hidden Requirement
    * Use Order
        Most Recently Used ---> Least Recently Used
    * need a mechanism that moves any element in the cache from their relative order between most recently used to least recently used up to most recently used
    * This mechanism needs to be done in O(1) time on average

    Properties the data structure needs to achieve
    * O(1) read and write access -- hash map
    * O(1) insertion and deletion -- doubly linked list

    hash map
    * key = key
    * value = ListNode pointer

    ListNodes
    * pointer to most recently used item
    * pointer to least recently used item
*/

#include <assert.h>

struct ListNode {
    ListNode* next;
    ListNode* prev;
    int key;
    int val;

    ListNode(int key, int val, ListNode* next = nullptr, ListNode* prev = nullptr) :
        key(key), val(val), next(next), prev(prev) {}
};

class LRUCache {
private:
    int capacity;
    int size;
    ListNode* mru;
    ListNode* lru;
    std::unordered_map<int,ListNode*> cache;
public:
    LRUCache(int capacity) :
        capacity(capacity),
        size(0),
        mru(nullptr),
        lru(nullptr) 
    {}

    void updateOrder(ListNode* curr) {
        assert(curr != nullptr);
        assert(mru != nullptr);
        assert(lru != nullptr);
        
        if (curr == mru) {
            return;
        }

        // if last node
        if (curr == lru) {
            if (lru->prev != nullptr && lru->prev->next != nullptr) {
                lru->prev->next = nullptr;
            }
            lru = lru->prev;

            mru->prev = curr;
            curr->next = mru;
            curr->prev = nullptr;
            mru = curr;
            return;
        }

        // 1 = 2 = 3
        // if a middle node, assign it's neighbors pointers away from it
        if (curr->prev != nullptr && curr->prev->next != nullptr) {
            curr->prev->next = curr->next;
        }

        if (curr->next != nullptr && curr->next->prev != nullptr) {
            curr->next->prev = curr->prev;
        }

        mru->prev = curr;
        curr->next = mru;
        curr->prev = nullptr;
        mru = curr;
    }

    void printOrder() {
        std::cout << "MRU TO LRU ORDER:\n";
        for (ListNode* curr = mru; curr != nullptr; curr = curr->next) {
            std::cout << curr->key << ":" << curr->val << " ";
        }
        std::cout << "\n\n";
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }

        ListNode* curr = cache[key];
        updateOrder(curr);
        //printOrder();

        return curr->val;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            // update existing value
            cache[key]->val = value;
            updateOrder(cache[key]);
            //printOrder();
            return;
        }

        if (size < capacity) {
            ListNode* l = new ListNode(key, value);

            if (size == 0) {
                assert(mru == nullptr);
                assert(lru == nullptr);
                mru = l;
                lru = l;
            } else {
                assert(mru != nullptr);
                assert(lru != nullptr);
                mru->prev = l;
                l->next = mru;
                mru = l;
            }

            cache[key] = l;
            ++size;
        } else {
            // evict lru item from cache
            //  - update new lru to be the node its pointing to previously
                    // edge case: could be capacity size 1 so lru would be pointing at nullptr
                    // which would mean that lru and mru would need to be reassigned to the new item as it is a replacement
            assert(lru != nullptr);
            ListNode* itemToDelete = lru;
            if (lru->prev != nullptr) {
                lru->prev->next = nullptr;
            }

            // edge case: mru == lru
            if (mru == lru) {
                mru = nullptr;
            }

            lru = lru->prev;
            cache.erase(itemToDelete->key);
            //std::cout << "removing: " << itemToDelete->key << std::endl;
            delete itemToDelete;
            itemToDelete = nullptr;

            // initialize ListNode l
            ListNode* l = new ListNode(key, value);
            cache[key] = l;
            if (mru == nullptr && lru == nullptr) {
                mru = l;
                lru = l;
            } else {
                // set l as mru
                mru->prev = l;
                l->next = mru;
                mru = l;
            }
        }
    }
};
