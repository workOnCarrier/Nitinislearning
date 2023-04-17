template <typename T>
class SpmcQueue {
public:
    SpmcQueue(std::size_t capacity, std::size_t num_consumers) :
        buffer_(new T[capacity]),
        capacity_(capacity),
        head_(new std::atomic<std::size_t>[num_consumers]),
        tail_(0)
    {
        for (std::size_t i = 0; i < num_consumers; ++i) {
            head_[i].store(0, std::memory_order_relaxed);
        }
    }

    ~SpmcQueue() {
        delete[] buffer_;
        delete[] head_;
    }

    bool enqueue(const T& value) {
        const std::size_t current_tail = tail_.load(std::memory_order_relaxed);
        const std::size_t next_tail = increment(current_tail);
        if (next_tail == head_[0].load(std::memory_order_acquire)) {
            return false; // queue is full
        }
        buffer_[current_tail] = value;
        tail_.store(next_tail, std::memory_order_release);
        return true;
    }

    bool dequeue(T& value, std::size_t consumer_id) {
        const std::size_t current_head = head_[consumer_id].load(std::memory_order_relaxed);
        if (current_head == tail_.load(std::memory_order_acquire)) {
            return false; // queue is empty
        }
        const std::size_t next_head = increment(current_head);
        const std::size_t target_index = (current_head % capacity_) * num_consumers_ + consumer_id;
        const std::size_t allocated_index = allocation_counter_.fetch_add(1, std::memory_order_relaxed) % num_consumers_;
        if (allocated_index != consumer_id) {
            return false; // another consumer has already read this element
        }
        value = buffer_[target_index];
        head_[consumer_id].store(next_head, std::memory_order_release);
        return true;
    }

private:
    std::size_t increment(std::size_t index) const {
        return (index + 1) % capacity_;
    }

    T* const buffer_;
    const std::size_t capacity_;
    std::atomic<std::size_t> tail_;
    std::atomic<std::size_t>* const head_;
    std::atomic<std::size_t> allocation_counter_{0};
    const std::size_t num_consumers_;
};
