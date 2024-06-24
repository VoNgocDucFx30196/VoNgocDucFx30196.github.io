#include<bits/stdc++.h>
#include<conio.h>
#include<cstdlib>
#include<unistd.h>
#define ll long long
#define str string

using namespace std;

const ll n=2;
str cmd ="";
str nameMaterial[n]={"Wood","Stone"};
ll SpeedBRMaterial[n]={2,1};
ll WoodToUpdate[n]={100,200};
ll StoneToUpdate2[n]={50,10};
map<str,ll>CountMaterial;

void Update()
{
    for(ll i=0;i<n;i++)
    {
        for(ll a=1;a<=SpeedBRMaterial[i];a++)
            CountMaterial[nameMaterial[i]]++;
    }
}

void play()
{
    while(1)
    {
        system("cls");
        for(ll i=0;i<n;i++)
        {
            cout<<nameMaterial[i]<<": "<<CountMaterial[nameMaterial[i]]<<" ("<<SpeedBRMaterial[i]<<")\n";
        }
        Update();
        sleep(1);
    }
}


void load_screen()
{
    system("cls");
    cout<<"Have Fun\n";
    ll i=0;
    while(i<=10){
        ll temp = rand()%5;
        i+=temp;
        if(i>10)temp -=i%10;
        for(ll a=0;a<=temp;a++)cout<<'=';
        if(i<10)temp = rand()%3;
        else temp=0;
        sleep(temp);
    }
    play();
}

bool checkNandP(str n,str p,str nt,str pt)
{
    if(n!=nt)return 0;
    if(p!=pt)return 0;
    return 1;
}

int main()
{
    string name,nametest;
    string pass,passtest;
    char key;
    cout<<"Sign In\n";
    cout<<"Enter Signname:";cin>>name;
    cout<<"Enter Password:";cin>>pass;
    while(true){
        system("cls");
        cout<<"Welcome to SP\n To login press'l'\n";
        while(1)if(kbhit()){key=_getch();break;}
        if(key=='l'){
            cout<<"Enter Signname:";cin>>nametest;
            cout<<"Enter Password:";cin>>passtest;
            if(checkNandP(name,pass,nametest,passtest)==1)load_screen();
            else cout<<"Invalid Infomation!";
        }
    return 0;
    }
}
