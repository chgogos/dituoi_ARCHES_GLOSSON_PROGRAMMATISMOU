#include <iostream>
using namespace std;

class Point {
public:
    int x, y;
    
    Point(int x, int y) : x(x), y(y) {}
    
    Point operator+(const Point& other) {
        return Point(x + other.x, y + other.y);
    }
    
    friend ostream& operator<<(ostream& os, const Point& p) {
        os << "(" << p.x << ", " << p.y << ")";
        return os;
    }
};

int main() {
    Point p1(1, 2);
    Point p2(3, 4);
    Point p3 = p1 + p2;  
    
    cout << p3 << endl;  
    return 0;
}