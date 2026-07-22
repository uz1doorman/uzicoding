#include <iostream>

using namespace std;

class LinkedList {
private:
    struct Node
    {
        int data;
        Node* next;
        Node(const int& val) : data(val), next(nullptr) {}
    };
    
    Node* head;
    Node* tail;
    size_t count;

public:
    LinkedList() : head(nullptr), tail(nullptr), count(0) {}

    ~LinkedList() {
        clear();
    }

    LinkedList(const LinkedList&) = delete;
    LinkedList& operator=(const LinkedList&) = delete;

    void clear() {
        Node* curr = head;
        while (curr != nullptr) {
            Node* temp = curr;
            curr = curr->next;
            delete temp;
        }
        head = tail = nullptr;
        count = 0;
    }

    bool empty() {
        return count == 0;
    }

    size_t size() {
        return count;
    }

    void pushFront(const int& value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
        if (tail == nullptr) tail = newNode;
        ++count;
    }

    void pushBack(const int& value) {
        Node* newNode = new Node(value);
        if (tail == nullptr) {
            tail = head = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        ++count;
    }

    void popFront() {
        Node* temp = head;
        head = head->next;
        if (head == nullptr) {
            tail = nullptr;
        }
        delete temp;
        --count;
    }
};
