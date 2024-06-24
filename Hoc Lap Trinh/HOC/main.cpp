#include<bits/stdc++.h>
#define ll long long
using namespace std;



int main()
{
    //freopen("CHIAHET.INP","r",stdin);
    //freopen("CHIAHET.OUT","w",stdout);
    ll m,n,k,kq=0;
    cin>>m>>n>>k;
    for(ll i=m;i<=n;i++)if(i%k==0)kq++;
    cout<<kq;
}
