#include <deque>
#include <iostream>
#include <vector>
using namespace std;
class MovingAverage {
    std::deque<int> m_queue;
    int             m_avg_size;
    long long       m_sum;
public:
    MovingAverage(int size):m_queue(), m_avg_size(size), m_sum(0) { }
    
    double next(int val) {
        m_queue.push_back(val);
        m_sum += val;
        auto count = m_queue.size();
        while (count > m_avg_size){
            auto val_ = m_queue.front();
            m_sum -= val_;
            m_queue.pop_front();
            count = m_queue.size();
        }
        double result = double(m_sum) / double(count);
        return result; 
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */

int main(){
    MovingAverage ma(3);
    vector<int> inputs{1, 10, 3, 5};
    for ( auto val : inputs){
        cout << ma.next(val) << endl;
    }
    return 0;
}