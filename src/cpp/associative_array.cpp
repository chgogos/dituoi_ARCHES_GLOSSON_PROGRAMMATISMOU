#include <iostream>
#include <map>
#include <string>

int main() {
  std::map<std::string, int> associativeArray;

  associativeArray["apple"] = 3;
  associativeArray["banana"] = 5;
  associativeArray["orange"] = 2;

  std::cout << "apple: " << associativeArray["apple"] << std::endl;
  std::cout << "banana: " << associativeArray["banana"] << std::endl;
  std::cout << "orange: " << associativeArray["orange"] << std::endl;

  for (const auto& pair : associativeArray) {
    std::cout << pair.first << ": " << pair.second << std::endl;
  }

  return 0;
}
