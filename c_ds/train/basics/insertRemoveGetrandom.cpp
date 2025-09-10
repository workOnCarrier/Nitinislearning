#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class RandomizedSet {
    unordered_map<int,int> m_keyValues;
    vector<int>  m_values;
public:
    RandomizedSet():m_values(), m_keyValues() {
        srand(RAND_MAX);
    }
    
    bool insert(int val) {
        if( m_keyValues.find(val) == m_keyValues.end()){ 
            m_values.push_back(val);
            m_keyValues.insert(make_pair(val, val));
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
         if( m_keyValues.find(val) != m_keyValues.end()){ 
            for ( auto index = m_values.begin(); index !=  m_values.end(); ++index) {
                if (*index == val) {
                    m_values.erase(index);
                }
            }
            m_keyValues.erase(val);
            return true;
        }
        return false;       
    }
    
    int getRandom() {
        float randomNum = (float) rand() / RAND_MAX;
        float target = randomNum * m_values.back();
        return *lower_bound(begin(m_values), end(m_values), target);
        int index = lower_bound(begin(m_values), end(m_values), target) - begin(m_values);
        return m_values[index];
    }
};

void test(){
    // Your RandomizedSet object will be instantiated and called as such:
    // RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom
    // [],[1],[2],[2],[],[1],[2],[]
    RandomizedSet* obj = new RandomizedSet();
    cout <<  "\t inserting 1:" << obj->insert(1) << endl;
    cout <<  "\t remove 2:" << obj->remove(2) << endl;
    cout <<  "\t inserting 2:" <<  obj->insert(2) << endl;
    cout <<  "\t getRandom \t:" <<  obj->getRandom() << endl;
    cout <<  "\t remove 1:" << obj->remove(1) << endl;
    cout <<  "\t inserting 2:" <<  obj->insert(2) << endl;
    cout <<  "\t getRandom \t:" <<  obj->getRandom() << endl;
    cout << "-----" << endl;
}
void test_2(){
    // ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
    // [[],             [-1],    [-2],    [-2],    [],          [-1],   [-2],       []]
    RandomizedSet* obj = new RandomizedSet();
    cout <<  "\t inserting -1:" << obj->insert(-1) << endl;
    cout <<  "\t remove -2:" << obj->remove(-2) << endl;
    cout <<  "\t inserting -2:" <<  obj->insert(-2) << endl;
    cout <<  "\t getRandom \t:" <<  obj->getRandom() << endl;
    cout <<  "\t remove -1:" << obj->remove(-1) << endl;
    cout <<  "\t inserting -2:" <<  obj->insert(-2) << endl;
    cout <<  "\t getRandom \t:" <<  obj->getRandom() << endl;
    cout << "-----" << endl;
}

int main(){
    test();
    test_2();
    return 0;
}