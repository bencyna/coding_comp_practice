#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string s;
    cin >> s;
    s = s.substr(0, s.size());
    
    vector<int> prefixW(s.size());
    vector<int> postfixW(s.size());
    int j = s.size() - 2;
    bool consecuitiveVsPre = s[0] == 'v';
    bool consecuitiveVsPost = s[s.size() - 1] == 'v';
    
    // build prefix and suffix ws
    for (int i = 1; i < s.size() - 1; i++) {
        char prefix = s[i];
        char postfix = s[j];
        
        if (prefix == 'v') {
            if (consecuitiveVsPre) {
                prefixW[i] = prefixW[i - 1] + 1;
            } else {
                prefixW[i] = prefixW[i - 1];
            }
            
            consecuitiveVsPre = true;
        } else {
            prefixW[i] = prefixW[i - 1];
            consecuitiveVsPre = false;
        }
        
        if (postfix == 'v') {
            if (consecuitiveVsPost) {
                postfixW[j] = postfixW[j + 1] + 1;
            } else {
                postfixW[j] = postfixW[j + 1];
            }
            
            consecuitiveVsPost = true;
        } else {
            postfixW[j] = postfixW[j + 1];
            consecuitiveVsPost = false;
        }
        
        j--;
    }
    
    int wow_factor = 0;
    for (int i = 1; i < s.size() - 1; i++) {
        if (s[i] == 'o') {
            wow_factor += prefixW[i] * postfixW[i];
        }
    }
    
    cout << wow_factor << endl;
    return 0;
}
