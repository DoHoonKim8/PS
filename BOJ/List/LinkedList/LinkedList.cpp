#include <iostream>
#include <cstdlib>

using namespace std;

class InvalidIndexException {};

template<typename T>
class ListNode {
public:
    T value;
    ListNode<T>* next;

    ListNode<T> () : next(nullptr) {}
    ListNode<T> (T value, ListNode<T>* next) : value(value), next(next) {}
};

template<typename T>
class LinkedList {
public:
    int size;
    ListNode<T>* head;

    LinkedList<T> () : size(0), head(nullptr) {}

    ~LinkedList<T> () {
        ListNode<T>* t1 = head;
        ListNode<T>* t2;

        while (t1 != nullptr) {
            t2 = t1 -> next;
            delete t1;
            t1 = t2;
        }
    }

    void insert(int k, T value) {
        try {
            if (k < 0 || k > size) throw InvalidIndexException();
            if (k == 0) {
                head = new ListNode<T> (value, head);
            } else {
                ListNode<T>* dest = head;
                for (int i = 0; i < k - 1; i++) dest = dest -> next;
                dest -> next = new ListNode<T> (value, dest -> next);
            }
        } catch (InvalidIndexException e) {
            cerr << "잘못된 인덱스입니다." << endl;
            exit(1);
        }
    }

    void erase(int k) {
        try {
            if (k < 0 || k >= size) throw InvalidIndexException();
            if (k == 0) {
                ListNode<T>* t = head;
                head = head -> next;
                delete t;
            } else {
                ListNode<T>* dest = head;
                for (int i = 0; i < k - 1; i++) dest = dest -> next;
                ListNode<T>* t = dest;
            }
        } catch (InvalidIndexException e) {

        }
    }
};
