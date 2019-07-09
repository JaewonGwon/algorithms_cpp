#include <iostream>
#include <tuple>
#include <algorithm>

using namespace std;

struct Grades {
    string name;
    int kor;
    int eng;
    int math;
};

bool compare(Grades& a, Grades& b) {
    if(a.kor < b.kor) {
        return true;
    }
    else if(a.kor == b.kor && a.eng > b.eng) {
        return true;
    }
    else if(a.kor == b.kor && a.eng == b.eng && a.math < b.math) {
        return true;
    }
    
    return false;
}