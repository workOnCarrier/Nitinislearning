// https://en.cppreference.com/w/cpp/language/parameter_pack
#include <iostream>
#include <utility>
#include <string>


class ExecuterConduit{
  public:
    ExecuterConduit(){}

    template <typename Task, typename ... Args>
    bool TaskPipeline(Task & executer, Args&&... executer_args){
        auto result = executer(std::forward<Args>(executer_args)...);
        return result;
    }
    
    template <typename Task, typename ... Args>
    bool TaskPipeline2(Task & executer, Args&&... executer_args){
        bool result = false;
        std::string supliment = " with supliment ";
 // this usage of std::forward<Args>(args) ... doest not work
//         auto lambda_wrapper = [&result, supliment, &executer, ... args = std::forward<Args>(executer_args)] () {
//             result = executer(supliment, std::forward<Args>(args)...);
//         };
// this works
        auto lambda_wrapper = [&result, supliment, &executer, ... args = std::forward<Args>(executer_args)](){
            result = executer(supliment, args...);
        };

// this works
//        auto lambda_wrapper = [&result, &executer, supliment, args = std::tuple<Args...>(std::forward<Args>(executer_args)...)]() {
//            result = std::apply([&](const auto&... captured_args) {
//                return executer(supliment, captured_args...);
//            }, args);
//        };
        lambda_wrapper();
        return result;
    }
};

bool IsExecableTask(const std::string &param){
    std::cout << "Param received in task:" << param << std::endl;
    return true;
}

bool IsExecableTask2(const std::string &param, const std::string &param2, std::string param_3){
    std::cout << "Param received in task:" << param << "#" << param2 << std::endl;
    std::cout << "param 3:" << param_3 << std::endl;
    return true;
}

class TaskManager{
  public:
    TaskManager():m_ec(){}
    void SubmitTasks(){
        std::string funny_value = "is this funny?";
        bool result = m_ec.TaskPipeline(IsExecableTask, funny_value );
        std::cout << "execution with" << result << std::endl;
    }
    void SubmitTasks2(){
        std::string funny_value = "is this funny?", additional = "another value";
        bool result = m_ec.TaskPipeline2(IsExecableTask2, funny_value, additional );
        std::cout << "execution with" << result << std::endl;
    }
  private:
  ExecuterConduit m_ec;
};

int main(){
    TaskManager tm;
    tm.SubmitTasks();
    tm.SubmitTasks2();
    return 0;
}