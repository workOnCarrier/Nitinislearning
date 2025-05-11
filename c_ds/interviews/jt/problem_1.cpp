#include <vector>
#include <iostream>
#include <string>
using namespace std;

// Declare the solution function (from your parser code)
string solution(string& spec);

void addToken(string token, vector<string>& tokens)
{
    // Trim leading whitespace.
    if (!token.empty()) {
        size_t start = token.find_first_not_of(" ");
        token = start != string::npos ? token.substr(start) : "";
    }

    // Do not add empty tokens.
    if (token.empty()) {
        return;
    }

    tokens.push_back(token);
}

void tokenize(const string& spec, const string& sep,
              vector<string>& tokens)
{
    // Split specification into tokens.

    // Loop over every char in specification.
    size_t start=0;
    for (size_t end=0; end < spec.size(); ++end) {
        // If current char is a separator, then add the
        // current token and separator to the tokens list.
        if (sep.find(spec[end]) != string::npos) {
            addToken(spec.substr(start, end-start), tokens);
            addToken(spec.substr(end, 1), tokens);
            start = end+1;
        }
    }
    // Add the last token to tokens list.
    addToken(spec.substr(start), tokens);
}

struct FuncArgs {
    string func;
    string args;
};
typedef vector<FuncArgs> Frame;

void parse(const vector<string>& tokens, vector<Frame>& stack)
{
    // Parse tokens into a useful stack structure.
    // All parallel tasks should live in the same stack Frame.

    // TODO: I am not sure what the issue is, but I know
    // that this stack is not being populated entirely as intended.

    // Initial stack frame.
    stack.push_back(Frame());

    for (size_t i=0; i < tokens.size(); ++i) {
        const string& tok = tokens[i];
        // New stack frame.
        if (tok == "," || tok == ";") {
            stack.push_back(Frame());
        }
            // Tokens within (...) are args that should be kept together.
        else if (tok == "(") {
            string args;
            while (tokens[++i] != ")")
                args += tokens[i];
            Frame& frame = stack.back();
            FuncArgs& fa = frame.back();
            fa.args = "(" + args + ")";
        }
            // Every other non separator token is a func.
        else if (tok != "{" && tok != "}" &&
                 tok != ")")
        {
            Frame& frame = stack.back();
            FuncArgs fa;
            fa.func = tok;
            frame.push_back(fa);
        }
    }
}

void eval(const vector<Frame>& stack,
          const string& partial,
          size_t index,
          vector<string>& expanded)
{
    // Evaluate the stack to expand all function compositions.

    // Base case: done building expansion, save result and return.
    if (index == stack.size()) {
        expanded.push_back(partial);
        return;
    }

    // Recursive case: build each current FuncArgs around partial
    // and recurse.
    const Frame& frame = stack[index];
    for (const FuncArgs& fa : frame) {
        // TODO: Hmmm, I am not sure how to handle args here.
        string newPartial = fa.func + "(" + partial + ")";
        eval(stack, newPartial, index+1, expanded);
    }
}

string solution(string& spec)
{
    // Split specification into tokens.
    vector<string> tokens;
    tokenize(spec, ",;(){}", tokens);
    for (auto token : tokens){
        std::cout << token << ", ";
    }

    // Parse tokens into a useful stack structure.
    vector<Frame> stack;
    parse(tokens, stack);

    // Evaluate the stack to expand all function compositions.
    vector<string> expanded;
    eval(stack, "input", 0, expanded);

    // Combine results into single new line delimited string.
    string result;
    for (const auto& e : expanded)
        result += "\n" + e;

    return result;
}

void runTest(const string& testName, const string& spec) {
    string input = spec; // Make mutable copy
    string result = solution(input);
    cout << "==== " << testName << " ====\n";
    cout << "Input:    " << spec << "\n";
    cout << "Output:   " << result << "\n\n";
}

int main() {
    runTest("Test 1: Simple Serial", "task1,task2,task3");
    runTest("Test 2: Simple Parallel", "task1,{task2;task3}");
    runTest("Test 3: Parallel with Empty", "task1,task2,{task3;}");
    runTest("Test 4: With Arguments", "task1('b',kw=1),task2(1,2,var1='a')");
    runTest("Test 5: Compound Parallel", "{func1;func2},{func3;func4}");
    runTest("Test 6: Nested with Args", "taskA(1),{taskB('x');taskC},{taskD;taskE(2,kw=3)}");

    return 0;
}
