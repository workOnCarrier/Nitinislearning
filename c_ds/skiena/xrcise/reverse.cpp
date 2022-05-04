
#include <iostream>

using namespace std;

class Node{
    int m_data;
    Node* m_next;
public:
    Node(int data): m_data(data), m_next(NULL){}
    void set_next(Node* next){m_next = next;}
    int get_data(){return m_data;}
    Node* get_next(){return m_next;}
};
typedef void (*operator_func)(Node*);

Node* reverse(Node* head);

Node* populate_test_data(Node* head, int test_value){
    for (int cur=0; cur<test_value; cur++){
        Node* new_val = new Node(cur);
        new_val->set_next(head);
        head  = new_val;
    }
    return head;
}

void display_node(Node* node){cout << " " << node->get_data();}
void visit(Node* head, operator_func func){
    Node* curr = head;
    while (NULL != curr){
        func(curr);
        curr = curr->get_next();
    }
}
void test_display(int loop){
    Node* head = NULL;
    head = populate_test_data(head,loop);
    visit(head, display_node);
}
Node* reverse(Node* head){
    Node* cur = head; 
    Node* prev = NULL; 
    if (NULL == head) return head;
    while(true){
        if (NULL == cur) {
            head = prev;
            break;
        }else{
            head = cur->get_next();
            cur->set_next(prev);
            prev = cur;
            cur = head;
        }
    }
    return head;
}

void test_reverse(int loop){
    Node* head = NULL;
    head = populate_test_data(head,loop);
    visit(head, display_node);
    cout << "\nreversed" << endl;
    head = reverse(head);
    visit(head, display_node);
    cout << "\n---" << endl;
}


int main(){
    cout << "hello world from reverse.cpp" << endl;
    cout << "\ntesting 0" << endl;
    test_reverse(0);
    cout << "\ntesting 1" << endl;
    test_reverse(1);
    cout << "\ntesting 2" << endl;
    test_reverse(2);
    cout << "\ntesting 3" << endl;
    test_reverse(3);
    cout << "\ntesting 4" << endl;
    test_reverse(4);
    cout << "\n";
    return 0;
}