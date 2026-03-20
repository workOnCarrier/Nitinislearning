class Solution {
    bool dfs(int i, unordered_map<int, vector<int>>& deps, set<int>& completed, set<int>& required, vector<int>& result ){
        if (completed.contains(i)) {   // true
            return true;
        }
        if ( !deps.contains(i) ){
            completed.insert(i);   // 
            result.push_back(i);   // 
            return true;
        }
        required.insert(i);                 // {1}
        auto dependencies = deps[i];          // 0
        for (auto depends : dependencies){
            if ( required.contains(depends)){ 
                return false;
            }
            auto found = this->dfs(depends, deps, completed, required, result);
            if ( !found ){ 
                return false;
            }
        }
        completed.insert(i);
        result.push_back(i);
        if (required.contains(i)){ required.erase(i);}
        return true;
    }

public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        set<int> completed;
        vector<int> result;
        map<int, vector<int>> deps;
        auto depCmp = [&deps](int a, int b){ return deps[a].size() > deps[b].size(); };
        priority_queue<int, vector<int>, decltype(depCmp)> pq(depCmp);
        for (auto val: prerequisites){
            deps[val[0]].push_back(val[1]);
        }
        for ( int i = 0; i < numCourses; ++ i){ // 1
            if (!deps.contains(i)){deps[i] = vector<int>();}
            pq.push(i);
        }
        while ( !pq.empty()){
            int i = pq.top();
            pq.pop();
            if ( completed.contains(i)) continue;
            set<int> required;
            auto status = this->dfs(i, deps, completed, required, result);
            if (!status) break;
        }
        if (result.size() < numCourses) return vector<int>();
        return result;
    }
};