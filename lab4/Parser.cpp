#include<iostream>
#include<stack>
#include<vector>
#include<string>

using namespace std;

stack<string> ispisivanje;
vector<string> ulaz;
string trenutni_element;
bool dane;

void A();
void B();
void C();
void S();

void ispis() {
    stack<string> obrnutistog;
    while (!ispisivanje.empty()) {
        obrnutistog.push(ispisivanje.top());
        ispisivanje.pop();
    }
    while (!obrnutistog.empty()) {
        string element = obrnutistog.top();
        cout << element;
        obrnutistog.pop();
    }
    cout << endl;
    cout << (dane ? "DA" : "NE") << endl;
    exit(0);
}

void C(){
    ispisivanje.push("C");
    A();
    A();
}


void A(){
    ispisivanje.push("A");

    if(trenutni_element != "b" && trenutni_element != "a"){
        dane = false;
        ispis();
    }

    if(trenutni_element == "b"){
        ulaz.erase(ulaz.begin());
        trenutni_element = ulaz[0];
        C();
    }
    else if(trenutni_element == "a"){
        ulaz.erase(ulaz.begin());
        trenutni_element = ulaz[0];
    }
}


void S(){
    ispisivanje.push("S");
    if(trenutni_element != "a" && trenutni_element != "b"){
        dane = false;
        ispis();
    }
    if(trenutni_element == "a"){
        ulaz.erase(ulaz.begin());
        trenutni_element = ulaz[0];
        A();
        B();
    }
    else if(trenutni_element == "b"){
        ulaz.erase(ulaz.begin());
        trenutni_element = ulaz[0];
        B();
        A();
    }

}


void B(){
    ispisivanje.push("B");

    if(trenutni_element != "c") return;

    for(int i = 0; i < 2; i++){
        if(trenutni_element != "c"){
            dane = false;
            ispis();
        }
        ulaz.erase(ulaz.begin());
        trenutni_element = ulaz[0];
    }

    S();

    if(trenutni_element == "b"){
        ulaz.erase(ulaz.begin());
        trenutni_element = ulaz[0];
    }else{
        dane = false;
        ispis();
    }


    if(trenutni_element == "c"){
        ulaz.erase(ulaz.begin());
        trenutni_element = ulaz[0];
    }else{
        dane = false;
        ispis();
    }
}


int main(void){
    
    string linija;
    cin >> linija;

    for(char c:linija){
        string str(1, c);
        ulaz.push_back(str);
    }

    ulaz.push_back("END");

    trenutni_element = ulaz[0];

    S();

    if(trenutni_element != "END"){
        dane = false;
        ispis();
    }
    else{
        dane = "DA";
        ispis();
    }

    return 0;
}