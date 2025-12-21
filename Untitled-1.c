#include<stdio.>
#include<stdlib.h>
int main(){
char sexe;
printf("entrer votre sexe(m ou f)");
scanf("%C",&sexe);
if (sexe=='m'){
    printf("vous etes un homme");
}
else if (sexe=='f'){
    printf("vous etes une femme");
}
else{
    printf("saisie invalide");
}
return 0;
}
