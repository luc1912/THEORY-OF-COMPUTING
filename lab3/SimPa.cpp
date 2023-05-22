#include<iostream>
#include<stack>
#include<vector>

using namespace std;

string epsilon_ispis, pocetni_znak_stoga, pocetno_stanje;
string pomocni[2];


void parseFirstLine(vector< vector<string> > &nizovi, int &brNizova, string &ulaz) {
    getline(cin, ulaz);
    string token1, token2;
    string inner_delimiter = ",";
    string outter_delimiter = "|";
    ulaz += outter_delimiter;
    while (ulaz.find(outter_delimiter) != string::npos) {
    vector<string> simboli;
        token1 = ulaz.substr(0, ulaz.find(outter_delimiter)); //get token
        ulaz.erase(0, ulaz.find(outter_delimiter) + outter_delimiter.length()); //erase token+delimiter
        token1 += inner_delimiter;
        while (token1.find(inner_delimiter) != string::npos) {
            token2 = token1.substr(0, token1.find(inner_delimiter));
            token1.erase(0, token1.find(inner_delimiter) + inner_delimiter.length());
            simboli.push_back(token2);
        }
        nizovi.push_back(simboli);
        brNizova++;
    }
}


void parseNextLine(vector<string> &vector, string &ulaz) {
    getline(cin, ulaz);
    string token1;
    string delimiter = ",";
    ulaz += delimiter;
    while (ulaz.find(delimiter) != string::npos) {
        token1 = ulaz.substr(0, ulaz.find(delimiter)); //get token
        ulaz.erase(0, ulaz.find(delimiter) + delimiter.length()); //erase token+delimiter
        vector.push_back(token1);
    }
}


void funkcijePrijelaza(string &ulaz, vector< vector<string> > &funkcije_prijelaza){
    string token;
    string inner_delimiter = ",";
    string outer_delimiter = "->";
    while(cin >> ulaz){
        vector<string> funkcija;
        token = ulaz.substr(0, ulaz.find(inner_delimiter)); //get token
        funkcija.push_back(token);
        ulaz.erase(0, ulaz.find(inner_delimiter) + inner_delimiter.length()); //erase token+delimiter
        token = ulaz.substr(0, ulaz.find(inner_delimiter)); //get token
        funkcija.push_back(token);
        ulaz.erase(0, ulaz.find(inner_delimiter) + inner_delimiter.length()); //erase token+delimiter
        token = ulaz.substr(0, ulaz.find(outer_delimiter)); //get token
        funkcija.push_back(token);
        ulaz.erase(0, ulaz.find(outer_delimiter) + outer_delimiter.length()); //erase token+delimiter
        ulaz += inner_delimiter;
        while(ulaz.find(inner_delimiter) != string::npos){
            token = ulaz.substr(0, ulaz.find(inner_delimiter)); //get token
            funkcija.push_back(token);
            ulaz.erase(0, ulaz.find(inner_delimiter) + inner_delimiter.length()); //erase token+delimiter
        }
        funkcije_prijelaza.push_back(funkcija);
    }
}


string ispis_stoga(stack<string> stog){
    string ispis;
    while(!stog.empty()){
        ispis += stog.top();
        stog.pop();
    }
    return ispis;
}


bool prihvatljivo(string trenutno_stanje, vector<string> prihvatljiva_stanja){
    for(const string& stanje : prihvatljiva_stanja){
        if(stanje == trenutno_stanje) return true;
    }
    return false;
}


void provjera(stack<string> stog, const vector< vector<string> >& funkcije_prijelaza, const string& trenutno_stanje){
    for(vector<string> prijelaz : funkcije_prijelaza){
        if(prijelaz[0] == trenutno_stanje && prijelaz[1] == "$" && prijelaz[2] == stog.top()){
            pomocni[0] = prijelaz[3];
            pomocni[1] = prijelaz[4];
            return;
        }
    }
}


void epsilon(const string& trenutno_stanje, const vector< vector<string> >& funkcije_prijelaza, stack<string> &stog) {
    for (vector<string> prijelaz : funkcije_prijelaza) {
        string vrh_stoga = stog.top();
        stog.pop();
        if (prijelaz[0] == trenutno_stanje && prijelaz[2] == vrh_stoga && prijelaz[1] == "$") {
            epsilon_ispis += prijelaz[0] + "#" + vrh_stoga + ispis_stoga(stog) + "|";
            string pomocni_stog = prijelaz[4];
            for (int i = pomocni_stog.size() - 1; i >= 0; i--) {
                stog.push(string(1, pomocni_stog[i])); // Push individual characters onto the stack
            }
            pocetno_stanje = prijelaz[3];
            pocetni_znak_stoga = vrh_stoga;
            if (prijelaz[4] != "$") epsilon(prijelaz[3], funkcije_prijelaza, stog);
            else break;
        }
        else stog.push(vrh_stoga);
    }
}



int main(){
    vector< vector<string> > ulazni_nizovi, funkcije_prijelaza;
    int br_nizova = 0;
    vector<string> stanja, ulazni_znakovi, znakovi_stoga, prihvatljiva_stanja;
    string ulaz;
    parseFirstLine(ulazni_nizovi, br_nizova, ulaz);
    parseNextLine(stanja, ulaz);
    parseNextLine(ulazni_znakovi, ulaz);
    parseNextLine(znakovi_stoga, ulaz);
    parseNextLine(prihvatljiva_stanja, ulaz);
    cin >> pocetno_stanje;
    cin >> pocetni_znak_stoga;
    funkcijePrijelaza(ulaz, funkcije_prijelaza);


    for(int i = 0; i < br_nizova; i++){
        stack<string> stog;
        stog.push(pocetni_znak_stoga);
        epsilon(pocetno_stanje, funkcije_prijelaza, stog);
        string trenutno_stanje = pocetno_stanje;
        string ispis = epsilon_ispis + trenutno_stanje + "#" + ispis_stoga(stog) + "|";
        epsilon_ispis = "";
        bool krivo = false;
        pomocni[0] = "";
        pomocni[1] = "";
        int iteracija = 0;
        while(iteracija < ulazni_nizovi[i].size()){
            bool pronadjen = false;
            string trenutni_znak = ulazni_nizovi[i][iteracija];
            string vrh_stoga = stog.top();
            stog.pop();
            for(vector<string> prijelaz : funkcije_prijelaza){
                if(prijelaz[0] == trenutno_stanje && (prijelaz[1] == trenutni_znak || prijelaz[1] == "$") && prijelaz[2] == vrh_stoga){
                    if(prijelaz[1] == trenutni_znak) iteracija++;
                    trenutno_stanje = prijelaz[3];
                    if(prijelaz[4] != "$"){
                        for(int j = prijelaz[4].size()-1; j >= 0; j--){
                            stog.push(prijelaz[4].substr(j, 1));
                        }
                    }
                    pronadjen = true;
                    break;
                }
            }
            if(!pronadjen){
                ispis += "fail|";
                krivo = true;
                trenutno_stanje = "";
                break;
            }
            ispis += trenutno_stanje + "#" + ispis_stoga(stog) + "|";
        }
        if(!krivo && !prihvatljivo(trenutno_stanje, prihvatljiva_stanja)){
            provjera(stog, funkcije_prijelaza, trenutno_stanje);
        }
        while(!pomocni[0].empty() && !pomocni[1].empty() && !prihvatljivo(trenutno_stanje, prihvatljiva_stanja)){
            trenutno_stanje = pomocni[0];
            stog.pop();
            for(int j = pomocni[1].size()-1; j >= 0; j--){
                stog.push(pomocni[1].substr(j, 1));
            }
            ispis += trenutno_stanje + "#" + ispis_stoga(stog) + "|";
            pomocni[0] = "";
            pomocni[1] = "";
            provjera(stog, funkcije_prijelaza, trenutno_stanje);
        }
        ispis += prihvatljivo(trenutno_stanje, prihvatljiva_stanja) ? "1" : "0";
        cout << ispis << endl;
    }
    return 0;
}