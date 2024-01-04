template <typename T>
class BroadcastQueue {
public:
    BroadcastQueue(std::size_t capacity, std::size_t num_consumers) :
        buffer_(new T[capacity]),
        capacity_(capacity),
        head_(new std::atomic<std::size_t>[num_consumers]),
        generation_(new std::atomic<std::size_t>[capacity]),
        tail_(0)
    {
        for (std::size_t i = 0; i < num_consumers; ++i) {
            head_[i].store(0, std::memory_order_relaxed);
        }
        for (std::size_t i = 0; i < capacity; ++i) {
            generation_[i].store(0, std::memory_order_relaxed);
        }
    }

    ~BroadcastQueue() {
        delete[] buffer_;
        delete[] head_;
        delete[] generation_;
    }

    bool enqueue(const T& value) {
        const std::size_t current_tail = tail_.load(std::memory_order_relaxed);
        const std::size_t next_tail = increment(current_tail);
        const std::size_t current_generation = generation_[current_tail].load(std::memory_order_relaxed);
        buffer_[current_tail] = value;
        generation_[current_tail].store(current_generation + 1, std::memory_order_release);
        tail_.store(next_tail, std::memory_order_release);
        return true;
    }

    bool dequeue(T& value, std::size_t consumer_id) {
        const std::size_t current_head = head_[consumer_id].load(std::memory_order_relaxed);
        const std::size_t current_tail = tail_.load(std::memory_order_acquire);
        if (current_head == current_tail) {
            return false; // queue is empty
        }
        const std::size_t target_index = current_head % capacity_;
        const std::size_t target_generation = generation_[target_index].load(std::memory_order_relaxed);
        if (target_generation > last_seen_generation_[consumer_id]) {
            value = buffer_[target_index];
            last_seen_generation_[consumer_id] = target_generation;
            head_[consumer_id].store(current_head + 1, std::memory_order_release);
            return true;
        }
        return false;
    }

private:
    std::size_t increment(std::size_t index) const {
        return (index + 1) % capacity_;
    }

    T* const buffer_;
    const std::size_t capacity_;
    std::atomic<std::size_t>* const head_;
    std::atomic<std::size_t>* const generation_;
    std::atomic<std::size_t> tail_;
    std::size_t last_seen_generation_[num_consumers]{0};
    const std::size_t num_consumers_;
};
