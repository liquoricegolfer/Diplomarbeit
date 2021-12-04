#include <stdlib.h>
#include <stdio.h>
#include <conio.h>
#include <unistd.h>
#include <time.h>

int Zufallszahl ()
{

    int randomZahl;

    srand(time(NULL));
    randomZahl = rand()%100 + 1;
    return randomZahl;
}

int Gegnerpositionierung (int Score, int Block1, int Block2, int Block3, int Block4){

    int Gegner = Zufallszahl() + 10;

    if (Score <= 73){
        if (Gegner == 18 || Gegner == 28 || Gegner == 38 || Gegner == 48 || Gegner == 58 || Gegner == 68 || Gegner == 78 || Gegner == 88 || Gegner == 98){
            Gegner = Zufallszahl() + 10;
        }

        else if (Gegner == 11 || Gegner == 21 || Gegner == 31 || Gegner == 41 || Gegner == 51 || Gegner == 61 || Gegner == 71 || Gegner == 81 || Gegner == 91){
            Gegner = Zufallszahl() + 10;
        }

        else if (Gegner == Block1 + 1 || Gegner == Block1 + 10 || Gegner == Block1 + 11 || Gegner == Block1 + 9 || Gegner == Block1 - 1 || Gegner == Block1 - 10 || Gegner == Block1 - 11 || Gegner == Block1 - 9){
            Gegner = Zufallszahl() + 10;
        }

        else if (Gegner == Block2 + 1 || Gegner == Block2 + 10 || Gegner == Block2 + 11 || Gegner == Block2 + 9 || Gegner == Block2 - 1 || Gegner == Block2 - 10 || Gegner == Block2 - 11 || Gegner == Block2 - 9){
            Gegner = Zufallszahl() + 10;
        }

        else if (Gegner == Block3 + 1 || Gegner == Block3 + 10 || Gegner == Block3 + 11 || Gegner == Block3 + 9 || Gegner == Block3 - 1 || Gegner == Block3 - 10 || Gegner == Block3 - 11 || Gegner == Block3 - 9){
            Gegner = Zufallszahl() + 10;
        }

        else if (Gegner == Block4 + 1 || Gegner == Block4 + 10 || Gegner == Block4 + 11 || Gegner == Block4 + 9 || Gegner == Block4 - 1 || Gegner == Block4 - 10 || Gegner == Block4 - 11 || Gegner == Block4 - 9){
            Gegner = Zufallszahl() + 10;
        }
    }
return Gegner;
}

int Abschusskontrolle (int Schussa, int Schussb, int Schussc, int Gegner1){
int weitergabe = 0;

if (Schussa == Gegner1 + 10 || Schussa == Gegner1 + 1 || Schussa == Gegner1 - 1){
    weitergabe = 1;
}
else if (Schussb == Gegner1 + 10 || Schussb == Gegner1 + 1 || Schussb == Gegner1 - 1){
    weitergabe = 2;
}
else if (Schussc == Gegner1 + 10 || Schussc == Gegner1 + 1 || Schussc == Gegner1 - 1){
    weitergabe = 3;
}
return weitergabe;
}



int main()
{
    /*
    S = Schwarz
    R = Rot
    B = Blau
    */

    char Spielfeld[200];
    int Standort = 175;
    char Knopfdruck;
    bool exit = false;
    int Platzhalter[10];
    int SpielerSchussA, SpielerSchussB, SpielerSchussC;
    int Gegner1Position = 300, Gegner2Position =300, Gegner3Position =300, Gegner4Position =300, Gegner5Position =300;
    int Score = 0;





    //Spielfeld erstellen
    for (int i = 0; i < sizeof(Spielfeld); i++)
    {
        Spielfeld[i] = 'S';
    }

    //Spielerraumschiff zum Zeitpunkt t = 0
    Spielfeld[Standort] = 'B';
    Spielfeld[Standort + 1] = 'B';
    Spielfeld[Standort - 10] = 'B';
    Spielfeld[Standort + 11] = 'B';
    Spielfeld[Standort + 9] = 'B';
    Spielfeld[Standort - 1] = 'B';



//Spielfeld aktualisierung nach 1 sek; sleep(1) am ende der Schleife
    while(!exit)
    {

        //erneuerung des cls fensters
        system("cls");

        for (int i = 0; i < sizeof(Spielfeld); i++)
        {
            //Zeilsensprung nach jedem 10. Block für ein 10x20 Feld
            if (i % 10 == 0)
            {
                printf("\n");
            }

            //Ausgabe des 20x10 Spielfeldes
            printf("%c ", Spielfeld[i]);

            if(kbhit())  // Nur, wenn auch eine Taste gedrückt wird werden die Blöcke auf dem Spielfeld abhängig von der Eingabe geändert
            {
                Knopfdruck = getch(); // int Knopfdruck ist der eingegebene Buchstabe

                if (Knopfdruck == 'a' || Knopfdruck == 'w' || Knopfdruck == 's' || Knopfdruck == 'd'){
                //alte Position des Spielers wird zwischengepeichert
                Platzhalter[1] = Standort;
                Platzhalter[2] = Standort + 1;
                Platzhalter[3] = Standort - 10;
                Platzhalter[4] = Standort + 11;
                Platzhalter[5] = Standort + 9;
                Platzhalter[6] = Standort - 1;

                //alte Position des SPielers wird Schwarz damit der Spieler keine "Fußabdrücke hinterlässt
                Spielfeld[Platzhalter[1]] = 'S';
                Spielfeld[Platzhalter[2]] = 'S';
                Spielfeld[Platzhalter[3]] = 'S';
                Spielfeld[Platzhalter[4]] = 'S';
                Spielfeld[Platzhalter[5]] = 'S';
                Spielfeld[Platzhalter[6]] = 'S';
                }

                //Spieler bewegt sich nach oben
                if (Knopfdruck =='w')
                {


                    //if bedingung damit der Spieler den für ihn vorhergesehenen Bereich nicht verlässt
                    if (Standort > 149 && Standort < 160)
                    {
                        Standort = Standort + 10;
                    }



                    Standort = Standort - 10;
                    Spielfeld[Standort] = 'B';
                    Spielfeld[Standort + 1] = 'B';
                    Spielfeld[Standort - 10] = 'B';
                    Spielfeld[Standort + 11] = 'B';
                    Spielfeld[Standort + 9] = 'B';
                    Spielfeld[Standort - 1] = 'B';

                }

                //Spieler bewegt sich nach links
                else if (Knopfdruck == 'a')
                {

                    //vietuelle Wand an der linkesn Seite des Spielfeldes
                    if (Standort == 151 || Standort == 161 || Standort == 171 || Standort == 181 || Standort == 191)
                    {

                        Standort = Standort + 1;

                    }



                    Standort = Standort - 1;



                    Spielfeld[Standort] = 'B';
                    Spielfeld[Standort + 1] = 'B';
                    Spielfeld[Standort - 10] = 'B';
                    Spielfeld[Standort + 11] = 'B';
                    Spielfeld[Standort + 9] = 'B';
                    Spielfeld[Standort - 1] = 'B';

                }

                //Spieler bewegt sich nach rechts
                else if (Knopfdruck == 'd')
                {

                    //virtuelle Mauer rechts
                    if (Standort == 158 || Standort == 168 || Standort == 178 || Standort == 188 || Standort == 198)
                    {

                        Standort = Standort - 1;
                    }



                    Standort = Standort + 1;
                    Spielfeld[Standort] = 'B';
                    Spielfeld[Standort + 1] = 'B';
                    Spielfeld[Standort - 10] = 'B';
                    Spielfeld[Standort + 11] = 'B';
                    Spielfeld[Standort + 9] = 'B';
                    Spielfeld[Standort - 1] = 'B';
                }

                //bewegung nach unten
                else if (Knopfdruck =='s')
                {
                    //Virtuelle Mauer am Boden des Spielfeldes
                    if (Standort > 179 && Standort < 190)
                    {
                        Standort = Standort - 10;
                    }






                    Standort = Standort + 10;
                    Spielfeld[Standort] = 'B';
                    Spielfeld[Standort + 1] = 'B';
                    Spielfeld[Standort - 10] = 'B';
                    Spielfeld[Standort + 11] = 'B';
                    Spielfeld[Standort + 9] = 'B';
                    Spielfeld[Standort - 1] = 'B';
                }

                //Ein Schuss ausgehend vom Spieler welche sich nach oben vom Spielfeld bewegen
                else if (Knopfdruck =='f')
                {

                    //Ein Schuss wird nur aktiviert wenn der Betrag dieser größer wie 200 (als wenn dieser Schuss sich nicht im Spielfeld befindet) beträgt
                    if (SpielerSchussA > 200)
                    {
                        //Spielerschuss soll von der Schnauze des Raumschiffes ausgehen
                        SpielerSchussA = Standort - 20;
                        Spielfeld[SpielerSchussA] = 'A';

                    }

                    else if (SpielerSchussB > 200)
                    {
                        SpielerSchussB = Standort - 20;
                        Spielfeld[SpielerSchussB] = 'B';
                    }

                    else if (SpielerSchussC > 200)
                    {
                        SpielerSchussC = Standort - 20;
                        Spielfeld[SpielerSchussC] = 'C';
                    }

                    else
                    {
                        continue;
                    }


                }

            }
        }
        //Wenn der Schuss ganz oben angelangt soll er verschwinden
        if (SpielerSchussA < 10)
        {
            int x = SpielerSchussA;
            Spielfeld[x] = 'S';
            SpielerSchussA = 300;

        }
        //Wenn er sich im Spielfeld befindet soll er sich nach oben bewegen
        else if (SpielerSchussA > 9 && SpielerSchussA < 200)
        {
            int x = SpielerSchussA;
            SpielerSchussA = SpielerSchussA - 10;
            Spielfeld[SpielerSchussA] = 'A';
            Spielfeld[x] = 'S';
        }

        if (SpielerSchussB < 10)
        {
            int y = SpielerSchussB;
            Spielfeld[y] = 'S';
            SpielerSchussB = 300;
        }
        else if (SpielerSchussB > 9 && SpielerSchussB < 200)
        {
            int y = SpielerSchussB;
            SpielerSchussB = SpielerSchussB - 10;
            Spielfeld[SpielerSchussB] = 'B';
            Spielfeld[y] = 'S';
        }

        if (SpielerSchussC < 10)
        {
            int z = SpielerSchussC;
            Spielfeld[z] = 'S';
            SpielerSchussC = 300;
        }
        else if (SpielerSchussC > 9 && SpielerSchussC < 200)
        {
            int z = SpielerSchussC;
            SpielerSchussC = SpielerSchussC - 10;
            Spielfeld[SpielerSchussC] = 'C';
            Spielfeld[z] = 'S';
        }
        //erneuerungsverzögerung des Spielfeldes nach 1 sek damit es schöner im cmd fenster aussieht
        sleep(1);

        //Die Position der Gegner wird mittles einer Zufallszahl in einer Funktion bestimmt

            if (Gegner1Position == 300)
            {
                Gegner1Position = Gegnerpositionierung(Score, Gegner2Position, Gegner3Position, Gegner4Position, Gegner5Position);

                Spielfeld[Gegner1Position] = 'R';
                Spielfeld[Gegner1Position + 1] = 'R';
                Spielfeld[Gegner1Position + 10] = 'R';
                Spielfeld[Gegner1Position - 11] = 'R';
                Spielfeld[Gegner1Position - 9] = 'R';
                Spielfeld[Gegner1Position - 1] = 'R';
            }

            else if (Gegner2Position == 300){
                Gegner2Position = Gegnerpositionierung(Score, Gegner1Position, Gegner3Position, Gegner4Position, Gegner5Position);

                Spielfeld[Gegner2Position] = 'R';
                Spielfeld[Gegner2Position + 1] = 'R';
                Spielfeld[Gegner2Position + 10] = 'R';
                Spielfeld[Gegner2Position - 11] = 'R';
                Spielfeld[Gegner2Position - 9] = 'R';
                Spielfeld[Gegner2Position - 1] = 'R';
            }

        int Abschuss1 = Abschusskontrolle (SpielerSchussA, SpielerSchussB, SpielerSchussC, Gegner1Position);
        int Abschuss2 = Abschusskontrolle (SpielerSchussA, SpielerSchussB, SpielerSchussC, Gegner2Position);

        if (Abschuss1 == 1 || Abschuss1 == 2 || Abschuss1 == 3){
            Score = Score + 13;

            if (Abschuss1 == 1){
            int x = SpielerSchussA;
            Spielfeld[x] = 'S';
            SpielerSchussA = 300;
            }

            else if (Abschuss1 == 2){
            int x = SpielerSchussB;
            Spielfeld[x] = 'S';
            SpielerSchussB = 300;
            }

            else if (Abschuss1 == 3){
            int x = SpielerSchussC;
            Spielfeld[x] = 'S';
            SpielerSchussC = 300;
            }

            Spielfeld[Gegner1Position] = 'S';
            Spielfeld[Gegner1Position + 1] = 'S';
            Spielfeld[Gegner1Position + 10] = 'S';
            Spielfeld[Gegner1Position - 11] = 'S';
            Spielfeld[Gegner1Position - 9] = 'S';
            Spielfeld[Gegner1Position - 1] = 'S';
            Gegner1Position = 300;
        }

else if (Abschuss2 == 1 || Abschuss2 == 2 || Abschuss2 == 3){
            Score = Score + 13;

            if (Abschuss2 == 1){
            int x = SpielerSchussA;
            Spielfeld[x] = 'S';
            SpielerSchussA = 300;
            }

            else if (Abschuss2 == 2){
            int x = SpielerSchussB;
            Spielfeld[x] = 'S';
            SpielerSchussB = 300;
            }

            else if (Abschuss2 == 3){
            int x = SpielerSchussC;
            Spielfeld[x] = 'S';
            SpielerSchussC = 300;
            }

            Spielfeld[Gegner2Position] = 'S';
            Spielfeld[Gegner2Position + 1] = 'S';
            Spielfeld[Gegner2Position + 10] = 'S';
            Spielfeld[Gegner2Position - 11] = 'S';
            Spielfeld[Gegner2Position - 9] = 'S';
            Spielfeld[Gegner2Position - 1] = 'S';
            Gegner2Position = 300;
}
        else {continue;
        }
    }

    return 0;
}^^