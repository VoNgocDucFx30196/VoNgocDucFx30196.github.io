#include <iostream>

using namespace std;
int tinhTongChuSo(int x) {
    int sum = 0;
    while (x > 0) {
        sum += x % 10;
        x /= 10;
    }
    return sum;
}
long long tinhTongCacX(long long A, long long B) {
    long long tongX = 0;

    for (long long X = A; X <= B; ++X) {
        int tempX = X % 9;
        if (tempX == 0) {
            tempX = 9;
        }
        tongX += tempX;
    }

    return tongX;
}
int main() {
    long long A, B;
    cin >> A >> B;

    long long ketQua = tinhTongCacX(A, B);

    cout << ketQua << endl;

    return 0;
}
