/*

    Hidden Requirement
    * create a function that moves any item from the cache to the most recently used
        * front of cache

    This will occur whenever you:
        * obtain an existing key value pair via get(int key) function
        * update an existing key value pair via put(int key, value)

    When you create a new key value pair value
        * add it to the top of the cache as most recently used

    When cache is at capacity
        * remove least recently used item from cache
            * assign old lru to a temp variable for deletion
            * set prev lru node to have its next pointer to nothing
            * corner case: if mru == lru
                * also set mru to nullptr so that it doesn't access a deleted item from the heap as that causes a runtime error in c++. This error only occurs if capacity of cache is 1
            * delete temp variable
            * set temp variable to nullptr

    doubly linked list
    * most recently used node
    * least recently used node
        * when cache is empty then gets 1 node added in
            * the node will be both the mru and lru node
        * when cache gets 1 node added and its cache size > 0
            * the mru will then become the new node added in
            * new mru will attach its next pointer to the old mru
            * old mru prev will attach to new mru

*/

#include <assert.h>

struct Node {
    int key;
    int val;
    Node* next;
    Node* prev;

    Node(int key, int val, Node* next = nullptr, Node* prev = nullptr) :
        key(key), val(val), next(next), prev(prev) {}
};


class LRUCache {
private:
    int capacity;
    int size;
    Node* mru;
    Node* lru;
    std::unordered_map<int,Node*> cache;
public:
    LRUCache(int capacity) :
        capacity(capacity), size(0), mru(nullptr), lru(nullptr)
    {}

    void updateOrder(Node* curr) {
        assert(curr != nullptr);

        // most recently used node
        if (curr == mru) {
            return;
        }

        // least recently used node
        if (curr == lru) {
            if (lru->prev != nullptr) {
                lru->prev->next = nullptr;
            }

            lru = lru->prev;
        } else {
            Node* next = curr->next;
            Node* prev = curr->prev;

            // middle node
            if (next != nullptr && prev != nullptr) {
                next->prev = curr->prev;
                prev->next = curr->next;
            }
        }

        curr->next = mru;
        curr->prev = nullptr;
        mru->prev = curr;
        mru = curr;
    }
    
    int get(int key) {
        // not found
        if (cache.find(key) == cache.end()) {
            return -1;
        }

        Node* curr = cache[key];
        updateOrder(curr);
        return curr->val;
    }
    
    void put(int key, int value) {
        // if updating existing key value pair
        if (cache.find(key) != cache.end()) {
            cache[key]->val = value;
            Node* curr = cache[key];
            updateOrder(curr);
            return;
        }


        Node* newNode = new Node(key, value);
        cache[key] = newNode;

        // if at capacity
        if (size >= capacity) {
            assert(lru != nullptr);
            assert(mru != nullptr);

            // remove lru
            Node* nodeToDelete = lru;
            if (lru->prev != nullptr) {
                lru->prev->next = nullptr;
            }
            lru = lru->prev;

            // 1 node as capacity edge case
            if (nodeToDelete == mru) {
                mru = nullptr;
            }

            cache.erase(nodeToDelete->key);
            delete nodeToDelete;
            nodeToDelete = nullptr;

            if (size == 1) {
                lru = nullptr;
            }

            if (mru == nullptr) {
                mru = newNode;
                lru = newNode; 
            } else {
                mru->prev = newNode;
                newNode->next = mru;
                mru = newNode;
            }

        
        } else {
            // if under capacity

            // 0 nodes in cache
            if (lru == nullptr && mru == nullptr) {
                mru = newNode;
                lru = newNode;
                ++size;
                return;
            }

            assert(lru != nullptr);
            assert(mru != nullptr);

            mru->prev = newNode;
            newNode->next = mru;
            mru = newNode;
            ++size;
        }
    }
};
