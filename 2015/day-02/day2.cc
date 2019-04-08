#include <iostream>
#include <fstream>
#include <string>
#include <regex>

using namespace std;

int main() {
	ifstream infile("input");
	string line;
	regex pat("(\\d+)");
	int numbers[3];

	while (getline(infile, line)) {
		smatch finds;
		regex_search(line, finds, pat);

		cout << finds.str(2) << endl;
	}
	//ifs.getline(line,20)
	return 0;
}