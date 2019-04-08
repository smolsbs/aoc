#include <iostream>
#include <fstream>

using namespace std;

int main () {
	
	ifstream ifs;
	int floor = 0;
	int steps = 1;
	ifs.open("input", ifstream::in);
	char c;
	while (ifs.get(c)) {
		if (c == '(') {
			floor++;
		}
		else {
			floor--;
		}
		if (floor == -1) {
			cout << "Santa has entered floor -1 at " << steps << endl;
		}
		steps++;
	}
	cout << "The floor is " << floor << endl;
	ifs.close();

    return 0;
}