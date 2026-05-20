#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<string> cities{"arta", "ioannina", "preveza", "igoumenitsa"};
  sort(cities.begin(), cities.end(),
       [](auto a, auto b) { return a.length() < b.length(); });
  for (auto city : cities) {
    cout << city << endl;
  }
}
