#include <atomic>
#include <cstddef>

template <typename T>
class LocklessQueue {
public:
    LocklessQueue(std::size_t capacity) :
        buffer_(new T[capacity]),
        capacity_(capacity),
        head_(0),
        tail_(0)
    {}

    ~LocklessQueue() {
        delete[] buffer_;
    }

    bool enqueue(const T& value) {
        std::size_t tail = tail_.load(std::memory_order_relaxed);
        std::size_t next_tail = increment(tail);
        if (next_tail == head_.load(std::memory_order_acquire)) {
            return false; // queue is full
        }
        buffer_[tail] = value;
        tail_.store(next_tail, std::memory_order_release);
        return true;
    }

    bool dequeue(T& value) {
        std::size_t head = head_.load(std::memory_order_relaxed);
        if (head == tail_.load(std::memory_order_acquire)) {
            return false; // queue is empty
        }
        value = buffer_[head];
        head_.store(increment(head), std::memory_order_release);
        return true;
    }

private:
    std::size_t increment(std::size_t index) const {
        return (index + 1) % capacity_;
    }

    T* const buffer_;
    const std::size_t capacity_;
    std::atomic<std::size_t> head_;
    std::atomic<std::size_t> tail_;
};
