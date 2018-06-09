%% ========================================================================
%
% Programm zur Modellierung des Magnetfeldes
%
% Modell: schraeger Gang, der in horizontale unendlich und vertikale
% Richtung endlich ausgedehnt ist. Das Anomaliefeld berechnet sich mit 
% der Formel 3.44 aus Telford et al. (1990).
%
%% ========================================================================
%
%             V 1.0  UNKOWN
% 2018/05/29  V 2.0  update by Andreas Brotzer 
%
%
%% ========================================================================
% #### Uebernahme aus dem Gnuplot-Skript Gang.gpt ####

% Anhand Telford et al. (1976) gibt es bei der Nutzung dieses Skriptes 
% folgendes zu beachten:
% 
% 1. Profilrichtung
% - Annahme: immer senkrecht zum Streichen des Gangs
% 
% 2. Streichrichtung
% - immer bzgl. magnetisch Nord
% - Der Winkel kann hierbei in math. positiver oder negativer Richtung 
%   abgetragen werden, allerdings in beiden Faellen mit positivem
%   Vorzeichen:
%   z.B.: beta_rad = 20 Grad oder beta_rad = 160 Grad
% 
% 3. Neigung
% - Auf die Blickrichtung wird nicht im Detail eingegangen. Anhand der
%   Geometrie-Abbildung koennen folgende Punkte abgeleitet werden.
% - Wenn die Profilrichtung z.B. W->E ist, dann ist die Blickrichtung 
%   entlang des Streichens gen Nord. Generell werden Profilrichtungen 
%   "westlich"->"oestlich" angenommen.
% - Dann wird der Neigungswinkel entgegen dem Uhrzeigersinn bezüglich der
%   Horizontalen abgetragen:
%   z.B.: Gang faelt mit 30 Grad nach Westen ein: xi_rad = 30 Grad
%   z.B.: Gang faellt mit 30 Grad nach Osten ein: xi_rad = 150 Grad
%
%
%% ========================================================================
% ##### Variablenerklaerung #####
%
% =========================================================================
% ### Elemente der Magnetfelder  ###
% 
% 1. gesetzte Variablen:
%
%   IH_rad: Inklination des Hintergrundfeldes (in �)
%   TH:     Totalintensitaet des Hintergrundfeldes (in nT)
% 
%
% 2. berechnete Variablen:
%
%   ZH:  Vertikalkomponente des Hintergrundfeldes (in nT)
%   HH:  Horizontalkomponente des Hintergrundfeldes (in nT)
%   FSG: Naeherung der Anomalie der Totalintensitaet 
%        (Da das Anomaliefeld meist viel schwaecher ist als das 
%        Hintergrundfeld, betrachtet man hier die Komponente des 
%        Anomaliefeldes in Richtung de Hintergrundfeldes.)
%   ZSG: Vertikalkomponente des Anomaliefeldes (Modell schraeger Gang)
%   HSG: Horizontalkomponente des Anomaliefeldes (Modell schraeger Gang)
%   TG:  Totalintensitaet des resultierenden Gesamtfeldes
%   ZG:  Vertikalkomponente des resultierenden Gesamtfeldes
%   HG:  Horizontalkomponente des resultierenden Gesamtfeldes
%   TA:  Anomalie der Totalintensitaet
% 
% 
% =========================================================================
% ### Messwerte ###
% 
%  Format der einzulesenden Datei: 
%       Spalte 1: Profilkoordinate in m
%       Spalte 2: Messwerte in nT, mit Punkte als Trennzeichen der 
%                 Dezimalzahlen
%       Die Spalten werden durch Leerzeichen getrennt.
%       Bsp: 0 47655.78
% 
%  XPOS:        Auf XPOS wird der Ursprung des Koordinatensystems 
%               der Modellierung gelegt.
%  DATASHIFT:   Offset der Messung (Messwert an der Basis) 
%  Betrachtet   man die Abweichung der Totalintensitaet oder der 
%               Vertikalkomponente vom Hintergrundfeld, so setzt man 
%               DATASHIFT auf 0.
% 
%  
% =========================================================================
% ### Modellierung ###
% 
% 1. gesetzte Variablen:
%
%   beta_rad:   Streichwinkel des Gangs relativ zur Feldrichtung (in �)
%   xi_rad:     Neigung des Gangs zur Horizontalen (in �)
%   kappa:      magnetische Suszeptibilitaet
%   d:          Tiefe Gangoberkante Gang (in m)
%   D:          Tiefe Gangunterkante Gang (in m)
%   b:          horizontale Breite des Ganges (in m)
%   h_stange:   H�he der Stange d. Protonen-Praezessions-Magnetometer (in m)
%
% 2. berechnete Variablen:
%
%   r1:         Abstand Gangoberkante (linke Ecke) - Aufpunkt (in m)
%   r2:         Abstand Gangunterkante (linke Ecke) - Aufpunkt (in m)
%   r3:         Abstand Gangoberkante (rechte Ecke) - Aufpunkt (in m)
%   r4:         Abstand Gangunterkante (rechte Ecke) - Aufpunkt (in m)
%   teta1:      Winkel r1 zu Oberflaeche (in �)
%   teta2:      Winkel r2 zu Oberflaeche (in �)
%   teta3:      Winkel r3 zu Oberflaeche (in �)
%   teta4:      Winkel r4 zu Oberflaeche (in �)
%   rms:        Root-mean-square error ist ein Ma� f�r die Diskrepanz der
%               modellierten und gemessenen Kurve.
%
% 3. Laufvariable:
%
%   x:          Abstand zum Aufpunkt (in m)

% #########################################################################




% =========================================================================
%% #### INPUT ####
% =========================================================================

clear all; clc; 

% =========================================================================
% ### Messdaten ###

% Input Textdatei mit 2 Spalten: 1 = Koordinate, 2 = Messwert

data_file = 'M26_M27_Nr2_mean.txt';

% Delimiter f�r die Eingabe Datei angegeben (z.B. , oder \t [f�r Tab] usw.)
delim     = ',';

% =========================================================================
% ### Variablendefinition (Winkel in � angeben!) ###

% --- 2018 ---

% Inklination des Hintergrundfeldes (in �)
IH        = 63.75;  
% Totalintansitaet des Hintergrundfeldes (in nT)
TH        = 48000;  
% Offset der Messung (Messwert an der Basis)
DATASHIFT = 48073.5;  % Nr 1: 48102, Nr 2: 48073.5
% Streichwinkel des Gangs (abgetragen im Uhrzeigersinn, in �, 0�=N-S-Richtung)
beta      = 29;  
% Neigung des Gangs (abgetragen im Gegenuhrzeigersinn, in �, 90�=vertikal)
xi        = 100; 
% magnetische Suszeptibilitaet
kappa     = 0.017;   
% Tiefe Gangoberkante (in m)
d         = 2;    
% Tiefe Gangunterkante (in m)
D         = 1000;     
% Gangbreite (in m)
b         = 5;
% Verschiebung des Ursprungs des Koordinatensystems der Modellierung
XPOS      = 8;    
% L�nge der Stange des Protonen-Pr�zessions-Magnetometers in m 
h_stange  = 2.0;      


% =========================================================================
% Konfiguration der Abbildung


% Legendeneintrag
Legende_Daten = 'Messwerte 2018, Messgebiet A59/1'; 


% =========================================================================
% #### END INPUT ####
% =========================================================================



% =========================================================================
% load data 

fp = fopen(data_file);
A=textscan(fp, '%f %f', 'delimiter',delim, 'commentstyle','#');
fclose(fp);

profil = A{1};
daten = A{2};

% combining depth d and pole height h_stange
d = d + h_stange;


%% =========================================================================
% #### Berechnungen ####
% =========================================================================

%% Winkel in Bogenmass umrechnen

IH_rad = IH*pi/180;
beta_rad = beta*pi/180;
xi_rad = xi*pi/180;

% =========================================================================
%% Vektoren erzeugen

korr = b/2;
x = profil-XPOS+korr; 

% =========================================================================
%% Berechnung der Elemente der Magnetfelder

% =========================================================================
% Komponenten des Hintergrundfeldes

ZH=sin(IH_rad)*TH;
HH=cos(IH_rad)*TH;
TH=sqrt(ZH^2+HH^2);

% =========================================================================
% Komponenten des Anomaliefeldes fuer die Modellierung eines schraegen Gangs

r1 = sqrt(d^2+(x+d/tan(xi_rad)).^2);
teta1 = atan2(d,(x+d/tan(xi_rad)));
r2 = sqrt(D^2+(x+D/tan(xi_rad)).^2);
teta2 = atan2(D,(x+D/tan(xi_rad)));
r3 = sqrt(d^2+(x+d/tan(xi_rad)-b).^2);
teta3 = atan2(d,(x+d/tan(xi_rad)-b));
r4 = sqrt(D^2+(x+D/tan(xi_rad)-b).^2);
teta4 = atan2(D,(x+D/tan(xi_rad)-b));

% =========================================================================
% Vertikalkomponente des schraegen Gangs nach Gl. 3.44a (Telford et al., 1990)

ZSG = (2*kappa*TH*sin(xi_rad))*((cos(IH_rad)*sin(xi_rad)*sin(beta_rad)...
       +sin(IH_rad)*cos(xi_rad))*log(r3.*r2./r4./r1)+(cos(IH_rad)*...
       cos(xi_rad)*sin(beta_rad)-sin(IH_rad)*sin(xi_rad))*...
       (teta1-teta3-teta2+teta4));

% =========================================================================
% Horizontalkomponente des schraegen Gangs nach Gl. 3.44b (Telford et al., 1990)

HSG = (2*kappa*TH*sin(xi_rad)*sin(beta_rad))*((sin(IH_rad)*sin(xi_rad)...
       -cos(IH_rad)*cos(xi_rad)*sin(beta_rad))*log(r3.*r2./r4./r1)+...
      (cos(IH_rad)*sin(xi_rad)*sin(beta_rad)+sin(IH_rad)*cos(xi_rad))*...
      (teta1-teta3-teta2+teta4));

% =========================================================================
% Naeherung der Anomalie der Totalintensitaet nach Gl. 3.44c (Telford et al., 1990)

FSG = (2*kappa*TH*sin(xi_rad))*((sin(2*IH_rad)*sin(xi_rad)*sin(beta_rad)...
      -cos(xi_rad)*(cos(IH_rad)^2*sin(beta_rad)^2-sin(IH_rad)^2))*...
      log(r3.*r2./r4./r1)+(sin(2*IH_rad)*cos(xi_rad)*sin(beta_rad)+...
      sin(xi_rad)*(cos(IH_rad)^2*sin(beta_rad)^2-sin(IH_rad)^2))*...
      (teta1-teta3-teta2+teta4));

% =========================================================================
%% Komponenten des resultierenden Gesamtfeldes

ZG = ZH+ZSG;
HG = HH+HSG;
TG = sqrt(ZG.^2+HG.^2);

% =========================================================================
%% Anomalie der Totalintensitaet

TA = TG-TH;

% =========================================================================
%% Fehler zwischen den Kurven

datred=daten-DATASHIFT;
diff = datred-TA;

% rms 
rms = sqrt((diff'*diff)/length(diff));


% =========================================================================
%% Erstellung der Abbildung

% defining parameters for the figure 
xrange    = [min(profil) max(profil)]; % x-Achsen-Begrenzung


fac=0.35;
mini=min([(daten-DATASHIFT)' TA']); 
maxi=max([(daten-DATASHIFT)' TA']);
datarange = [mini-fac*mini maxi+fac*maxi]; % y-Achsen-Begrenzung


fonts = 14; % fontsize for labels


% -------------------------------------------------------------------------
% create figure
fig=figure(); 

% figure settings
set(gcf, 'position',[100 100 800 600], 'renderer','painters');
set(gcf,'color','white')
set(0,'DefaultTextInterpreter','latex');


% ----------------------------------
% first subplot
subplot(2,1,1);

plot(x+XPOS-korr, TA, 'color','r', 'linewidth',1.5);
hold on; box on; grid on;

plot(profil,daten-DATASHIFT, 'color',[0 0 0], 'linestyle','none',...
     'marker','o', 'markerfacecolor',[0 0 0], 'markersize',4);

posf1=get(gca,'position'); posf1(1)=posf1(1)+0.005;set(gca,'position',posf1);
 

% ----------------------------------
% set labels
legend('modellierte Anomalie (schraeger Gang)', Legende_Daten);
xlabel('\bf Profilkoordinate in m', 'fontsize',fonts);
ylabel('\bf Flussdichte in nT', 'fontsize',fonts);
title('\bf Anomalie der Totalintensit\"at (Annahme: Gang)', 'fontsize',fonts+2, 'visible','on');

xlim(xrange);
ylim(datarange);


% ----------------------------------
% configure and plot legend box 
t1 = ['I_H = ' num2str(IH,'%3.2f') '^\circ'];
%t1 = ['$I_\mathrm{H}$ = ' num2str(IH,'%3.2f') ' Grad'];
lh = legend(['modellierte Anomalie (' t1 ')'], Legende_Daten);
set(lh, 'location','southoutside', 'fontsize',fonts-2, 'orientation','horizontal');
lpos = get(lh,'position');
lpos(2) = 0.46;
lpos(3) = lpos(3)-0.6;
lpos(1) = lpos(1)+0.3;
set(lh,'position',lpos);


% ----------------------------------
% configure and plot info box 1
t2 = {['\bf Gang: $\qquad$']...
      ['$\beta$ = ' num2str(beta,'%3.1f') ' $^\circ$']...
      ['$\xi$ = ' num2str(xi,'%3.1f') ' $^\circ$']...
      ['$d$ = ' num2str(d-h_stange,'%2.1f') ' m']...
      ['$b$ = ' num2str(b,'%2.1f') ' m']...
      ['$\kappa$ =   ' num2str(kappa,'%1.5f')]};

  
% defining if the infobox is at the right or left side according to the
% maximum of the data 
[val,ind]=max(daten);
if ind <= length(profil)*2/3; 
    loc1 = [max(profil)-0.005*max(profil) datarange(2)-0.01*datarange(2)]; corner1 = 'right';
    loc2 = [min(profil)+0.005*max(profil) datarange(2)-0.01*datarange(2)]; corner2 = 'left';
else 
    loc1 = [min(profil)+0.01*max(profil) datarange(2)-0.03*datarange(2)]; corner1 = 'left';
    loc2 = [max(profil)-0.01*max(profil) datarange(2)-0.03*datarange(2)]; corner2 = 'right';
end


th1 = text(loc1(1),loc1(2), t2,...
     'horizontalalignment',corner1,...
     'verticalalignment','top',...
     'edgecolor',[0 0 0],...
     'fontsize',fonts-2);
set(th1, 'backgroundcolor', [0.98 0.98 0.98]);


% ----------------------------------
% configure and plot info box 2
t2 = {['$rms$ = ' num2str(rms, '%2.2f') ' nT']};

th2 = text(loc2(1),loc2(2), t2,...
     'horizontalalignment',corner2,...
     'verticalalignment','top',...
     'edgecolor',[0 0 0],...
     'fontsize',fonts-2);
set(th2, 'backgroundcolor', [0.98 0.98 0.98]);


% ----------------------------------
% second subplot (dike) is defined
subplot(2,1,2);

% parameters
if D >= 40; ymin=round(D*0.1); yl=ymin; else ymin=round(D); yl=ymin+1.1*D; end
dx = cosd(xi)*ymin;
d = d-h_stange;

% vectors for the patch
xxx = [XPOS-b/2-dx; XPOS-b/2; XPOS+b/2; XPOS+b/2-dx];
yyy = [ymin; d; d; ymin];

% plots 
plot([XPOS-b/2 XPOS+b/2], [d d],'color','k', 'linewidth',1.5)
hold on 
plot([XPOS-b/2 XPOS-b/2-dx], [d ymin],'color','k', 'linewidth',1.5)
plot([XPOS+b/2 XPOS+b/2-dx], [d ymin],'color','k', 'linewidth',1.5)

patch(xxx,yyy,[.7 .7 .7])

xlim(xrange);
ylim([0 yl]);

% settings
set(gca,'xTickLabel',[],'YDir','reverse')
posf2=get(gca,'position'); posf2(1)=posf2(1)+0.005; set(gca,'position',posf2);
ylabel('\bf Tiefe in m', 'fontsize',fonts)


% =========================================================================
%% Drucken der Abbildung in verschiedene Dateien

[fpath,fname,fext] = fileparts(data_file);
print(gcf, '-depsc', '-r300', [fname '.eps']);
print(fig, '-dpdf', '-r300',  [fname '.pdf']);
%print(gcf, '-dpng', '-r300', [fname '.png']);



% =========================================================================
% END OF FILE
% =========================================================================
