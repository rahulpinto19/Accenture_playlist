# Python
def check(num, divisors):
    for divisor in divisors:
        if num % divisor == 0:
            return False
    return True

def DesiredArray(Arr, N, k):
    num = 1
    result = 0
    while k != 0:
        if check(num, Arr):
            result += num
            k -= 1
        num += 1
    return result

K = 4
N = 5
Arr = [2, 3, 4, 5, 6]
print(DesiredArray(Arr, N, K))


// Java
public class DesiredArray {
    
    public static boolean check(int num, int[] divisors) {
        for (int divisor : divisors) {
            if (num % divisor == 0) {
                return false;
            }
        }
        return true;
    }

    public static int DesiredArray(int[] Arr, int N, int k) {
        int num = 1, result = 0;
        while (k != 0) {
            if (check(num, Arr)) {
                result += num;
                k--;
            }
            num++;
        }
        return result;
    }

    public static void main(String[] args) {
        int K = 4;
        int N = 5;
        int[] Arr = {2, 3, 4, 5, 6};
        System.out.println(DesiredArray(Arr, N, K));
    }
}


// C++
#include <iostream>
#include <vector>
using namespace std;

bool check(int num, vector<int>& divisors) {
    for (int divisor : divisors) {
        if (num % divisor == 0) {
            return false;
        }
    }
    return true;
}

int DesiredArray(vector<int>& Arr, int N, int k) {
    int num = 1, result = 0;
    while (k != 0) {
        if (check(num, Arr)) {
            result += num;
            k--;
        }
        num++;
    }
    return result;
}

int main() {
    int K = 4;
    int N = 5;
    vector<int> Arr = {2, 3, 4, 5, 6};
    cout << DesiredArray(Arr, N, K) << endl;
    return 0;
}
