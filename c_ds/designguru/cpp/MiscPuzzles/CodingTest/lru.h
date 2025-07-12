#include <memory>
#include <stdexcept>
#include <iostream>

/// LRU cache ...

template <typename T>
struct Node_{
    T value;
    int key;
    std::shared_ptr<struct Node_<T>> next;
    std::shared_ptr<struct Node_<T>> prev;
};

template<typename T>
using Node = Node_<T>;


template <typename T>
class LRU {
public:
    LRU(int size):m_head(), m_tail(), m_currSize(0), m_size(size){}
    T get(int key){
        auto currNode = m_head;
        while (currNode != nullptr){
            if (currNode->key == key){
                // get the head to point to this node
                if (m_head != currNode) {
                    currNode->prev->next = currNode->next;
                    if (currNode->next != nullptr){
                        currNode->next->prev = currNode->prev;
                    }
                    auto prev_head = m_head;
                    currNode->prev = nullptr;
                    currNode->next = prev_head;
                    prev_head->prev = currNode;
                }
                // return 
                return currNode->value;
            }
            currNode = currNode->next;
        }
        throw std::runtime_error("key not found");
    }
    void put(int key, T val){
        auto newNode = std::make_shared<Node<T>>(val, key, nullptr, nullptr);
        if (m_currSize >= m_size){
            // if (m_head == m_tail) // assuming this is not a valid case
            auto last_node = m_tail;
            // move tail to last - 1
            m_tail = m_tail->prev;
            m_tail->next = nullptr;
            // remove the last node  -- when it goes out of scope
        }
        // add the new node at the head
        auto prev_head = m_head;
        m_head = newNode;
        newNode->next = prev_head;
        if (prev_head != nullptr) prev_head->prev = newNode;
        ++m_currSize;
    }
private:
    std::shared_ptr<Node<T>> m_head;
    std::shared_ptr<Node<T>> m_tail;
    int  m_currSize;
    const int  m_size;
};

