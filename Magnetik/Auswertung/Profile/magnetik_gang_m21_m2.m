clear all, clc;

%%
% #########################################################################
% Programm zur Modellierung des Magnetfeldes
% Modell: schraeger Gang, der in horizontale unendlich und vertikale Richtung endlich ausgedehnt ist
% Anomaliefeld berechnet mit Formel 3.44 aus Telford et al. (1990)
% #########################################################################
% Übernahme aus dem Gnuplot-Skript Gang.gpt
% #########################################################################
% Anhand Telford et al. (1976) gibt es bei der Nutzung dieses Skriptes folgendes zu beachten:
% 
% 1. Profilrichtung
% - Annahme: immer senkrecht zum Streichen des Gangs
% 
% 2. Streichrichtung
% - immer bzgl. magnetisch Nord
% - Der Winkel kann hierbei in math. positiver oder negativer Richtung abgetragen
%   werden, allerdings in beiden Fällen mit positivem Vorzeichen.
% - z.B.: beta_rad = 20 Grad oder beta_rad = 160 Grad
% 
% 3. Neigung
% - Auf die Blickrichtung wird nicht im Detail eingegangen. Anhand der
%   Geometrie-Abbildung können folgende Punkte abgeleitet werden.
% - Wenn die Profilrichtung z.B. W->E ist, dann ist die Blickrichtung entlang des
%   Streichens gen Nord. Generell werden Profilrichtungen "westlich"->"östlich"
%   angenommen.
% - Dann wird der Neigungswinkel entgegen dem Uhrzeigersinn bezüglich der
%   Horizontalen abgetragen.
% - z.B.: Gang fällt mit 30 Grad nach Westen ein: xi_rad = 30 Grad
% - z.B.: Gang fällt mit 30 Grad nach Osten ein: xi_rad = 150 Grad
% #########################################################################
% 
% ###############################
% ##### Variablenerklaerung #####
% ###############################
% 
% ### Elemente der Magnetfelder  ###
% 
%  gesetzte Variablen:
%   IH_rad: Inklination des Hintergrundfeldes (in °)
%   TH: Totalintensitaet des Hintergrundfeldes (in nT)
% 
%  berechnete Variablen:
%   ZH: Vertikalkomponente des Hintergrundfeldes (in nT)
%   HH: Horizontalkomponente des Hintergrundfeldes (in nT)
%   FSG: Naeherung der Anomalie der Totalintensitaet (Da das Anomaliefeld meist viel schwaecher ist als das Hintergrundfeld,
%        betrachtet man hier die Komponente des Anomaliefeldes in Richtung des Hintergrundfeldes.)
%   ZSG: Vertikalkomponente des Anomaliefeldes (Modell schraeger Gang)
%   HSG: Horizontalkomponente des Anomaliefeldes (Modell schraeger Gang)
%   TG: Totalintensitaet des resultierenden Gesamtfeldes
%   ZG: Vertikalkomponente des resultierenden Gesamtfeldes
%   HG: Horizontalkomponente des resultierenden Gesamtfeldes
%   TA: Anomalie der Totalintensitaet
% 
% 
% ### Messwerte ###
% 
%  Format der einzulesenden Datei: 
%   Spalte 1: Profilkoordinate in m
%   Spalte 2: Messwerte in nT, mit Punkte als Trennzeichen der Dezimalzahlen
%   Die Spalten werden durch Leerzeichen getrennt.
%   Bsp: 0 47655.78
% 
%  XPOS: Auf XPOS wird der Ursprung des Koordinatensystems der Modellierung gelegt.
%  DATASHIFT: Offset der Messung (Messwert an der Basis); 
%  Betrachtet man die Abweichung der Totalintensitaet oder der Vertikalkomponente vom Hintergrundfeld, so setzt man DATASHIFT auf 0.
% 
%  
% ### Modellierung ###
% 
%  gesetzte Variablen:
%   beta_rad: Streichwinkel des Gangs relativ zur Feldrichtung (in °)
%   xi_rad: Neigung des Gangs zur Horizontalen (in °)
%   kappa: magnetische Suszeptibilitaet
%   d: Tiefe Gangoberkante Gang (in m)
%   D: Tiefe Gangunterkante Gang (in m)
%   b: horizontale Breite des Ganges (in m)
% 
%  berechnete Variablen:
%   r1: Abstand Gangoberkante (linke Ecke) - Aufpunkt (in m)
%   r2: Abstand Gangunterkante (linke Ecke) - Aufpunkt (in m)
%   r3: Abstand Gangoberkante (rechte Ecke) - Aufpunkt (in m)
%   r4: Abstand Gangunterkante (rechte Ecke) - Aufpunkt (in m)
%   teta1: Winkel r1 zu Oberflaeche (in °)
%   teta2: Winkel r2 zu Oberflaeche (in °)
%   teta3: Winkel r3 zu Oberflaeche (in °)
%   teta4: Winkel r4 zu Oberflaeche (in °)
% 
%  Laufvariable:
%   x: Abstand zum Aufpunkt (in m)


%% INPUT

% =================================
% Messdaten
% =================================
% Textdatei mit 2 Spalten: 1 = Koordinate, 2 = Messwert
% data_file = 'Riedheim_Profil_D_2013.txt';
data_file = 'm21_m2_mean.txt';

% =================================
% Variablendefinition (Winkel in ° angeben!)
% =================================
% --- 2013 ---
% IH        = 63.75;   % Inklination des Hintergrundfeldes (in °)
% TH        = 47000;   % Totalintansitaet des Hintergrundfeldes (in nT)
% D         = 50;     % Tiefe Gangunterkante (in m)
% beta = 0;       % Streichwinkel des Gangs (abgetragen im Uhrzeigersinn, in °, 0°=N-S-Richtung)
% xi   = 90;     % Neigung des Gangs (abgetragen im Gegenuhrzeigersinn, in °, 90°=vertikal)
% kappa         = 0.0025;  % magnetische Suszeptibilitaet
% d         = 4.5;     % Tiefe Gangoberkante (in m)
% b         = 9.5;     % Gangbreite (in m)
% XPOS      = 27;      % Verschiebung des Ursprungs des Koordinatensystems der Modellierung
% DATASHIFT = 47900;   % Offset der Messung (Messwert an der Basis)
% --- 2003 ---
IH        = 63.75;   % Inklination des Hintergrundfeldes (in °)
TH        = 47000;   % Totalintansitaet des Hintergrundfeldes (in nT)
D         = 350;     % Tiefe Gangunterkante (in m)
beta      = 0;       % Streichwinkel des Gangs (abgetragen im Uhrzeigersinn, in °, 0°=N-S-Richtung)
xi        = 90;      % Neigung des Gangs (abgetragen im Gegenuhrzeigersinn, in °, 90°=vertikal)
kappa     = 0.008;  % magnetische Suszeptibilitaet
d         = 2.0;     % Tiefe Gangoberkante (in m)
b         = 9.5;     % Gangbreite (in m)
XPOS      = 20;      % Verschiebung des Ursprungs des Koordinatensystems der Modellierung
DATASHIFT = 47700;   % Offset der Messung (Messwert an der Basis)

% =================================
% Einstellungen der Abbildung
% =================================
xrange        = [-20 30];      % x-Achsen-Begrenzung
datarange     = [-200 1500];   % y-Achsen-Begrenzung
infoxy        = [15 1200];     % Koordinaten (x,y) für Infobox mit Gangparametern
Legende_Daten = 'Messwerte 2003, Messgebiet A59/1';   % Legendeneintrag der Messwerte

% =================================
% Plotzeug
% =================================
dx            = 1;             % Spacing des x-Vektors zur Generierung der Modelldaten
fig           = 1;             % Nr. der Matlab-Figure


% =========================================================================
% =========================================================================
%% Winkel in Bogenmaß umrechnen
IH_rad = IH*pi/180;
beta_rad = beta*pi/180;
xi_rad = xi*pi/180;


%% Vektoren
x = xrange(1):dx:xrange(2);


%% Berechnung der Elemente der Magnetfelder
% =================================
% Komponenten des Hintergrundfeldes
ZH=sin(IH_rad)*TH;
HH=cos(IH_rad)*TH;
TH=sqrt(ZH^2+HH^2);

% =================================
% Komponenten des Anomaliefeldes fuer die Modellierung eines schraegen Gangs
r1 = sqrt(d^2+(x+d/tan(xi_rad)).^2);
teta1 = atan2(d,(x+d/tan(xi_rad)));
r2 = sqrt(D^2+(x+D/tan(xi_rad)).^2);
teta2 = atan2(D,(x+D/tan(xi_rad)));
r3 = sqrt(d^2+(x+d/tan(xi_rad)-b).^2);
teta3 = atan2(d,(x+d/tan(xi_rad)-b));
r4 = sqrt(D^2+(x+D/tan(xi_rad)-b).^2);
teta4 = atan2(D,(x+D/tan(xi_rad)-b));

% =================================
% Vertikalkomponente des schraegen Gangs nach Gl. 3.44a (Telford et al., 1990)
ZSG = (2*kappa*TH*sin(xi_rad))*((cos(IH_rad)*sin(xi_rad)*sin(beta_rad)+sin(IH_rad)*cos(xi_rad))*log(r3.*r2./r4./r1)+...
                        (cos(IH_rad)*cos(xi_rad)*sin(beta_rad)-sin(IH_rad)*sin(xi_rad))*(teta1-teta3-teta2+teta4));

% =================================
% Horizontalkomponente des schraegen Gangs nach Gl. 3.44b (Telford et al., 1990)
HSG = (2*kappa*TH*sin(xi_rad)*sin(beta_rad))*((sin(IH_rad)*sin(xi_rad)-cos(IH_rad)*cos(xi_rad)*sin(beta_rad))*log(r3.*r2./r4./r1)+...
                                  (cos(IH_rad)*sin(xi_rad)*sin(beta_rad)+sin(IH_rad)*cos(xi_rad))*(teta1-teta3-teta2+teta4));

% =================================
% Naeherung der Anomalie der Totalintensitaet nach Gl. 3.44c (Telford et al., 1990)
FSG = (2*kappa*TH*sin(xi_rad))*((sin(2*IH_rad)*sin(xi_rad)*sin(beta_rad)-cos(xi_rad)*(cos(IH_rad)^2*sin(beta_rad)^2-sin(IH_rad)^2))*log(r3.*r2./r4./r1)+...
                        (sin(2*IH_rad)*cos(xi_rad)*sin(beta_rad)+sin(xi_rad)*(cos(IH_rad)^2*sin(beta_rad)^2-sin(IH_rad)^2))*(teta1-teta3-teta2+teta4));


%% Komponenten des resultierenden Gesamtfeldes
ZG = ZH+ZSG;
HG = HH+HSG;
TG = sqrt(ZG.^2+HG.^2);


%% Anomalie der Totalintensitaet
TA = TG-TH;


%% Daten laden
fp = fopen(data_file);
A=textscan(fp, '%f %f', 'delimiter','\t', 'commentstyle','#');
fclose(fp);
profil = A{1};
daten = A{2};


%% Erstellung der Abbildung
set(0,'DefaultTextInterpreter','latex');
figure(fig);
clf;
set(fig, 'position',[100 100 800 600], 'renderer','painters');

ax1 = axes('position',[0.1 0.15 0.8 0.75]);
plot(x, TA, 'color',[1 1 1]*0.3, 'linewidth',1);
hold on;
box on;
grid on;
plot(profil-XPOS,daten-DATASHIFT, 'color',[0 0 0], 'linestyle','none',...
     'marker','o', 'markerfacecolor',[0 0 0], 'markersize',4);
legend('modellierte Anomalie (schraeger Gang)', Legende_Daten);
xlim(xrange);
ylim(datarange);
xlabel('\bf Profilkoordinate in m', 'fontsize',12);
ylabel('\bf Flussdichte in nT', 'fontsize',12);

title('Anomalie der Totalintensit\"at (Annahme: Gang)', 'fontsize',14, 'visible','on');

t1 = ['$I_\mathrm{H}$ = ' num2str(IH,'%3.2f') ' $^\circ$'];
% t1 = ['$I_\mathrm{H}$ = ' num2str(IH,'%3.2f') ' Grad'];
lh = legend(['modellierte Anomalie (' t1 ')'], Legende_Daten);
set(lh, 'location','southoutside', 'interpreter','latex', 'orientation','horizontal');
lpos = get(lh,'position');
lpos(2) = 0.02;
lpos(3) = lpos(3)+0.06;
lpos(1) = lpos(1)-0.03;
set(lh,'position',lpos);


t2 = {['\bf Gang: $\qquad\qquad$']...
      ['$\beta$ = ' num2str(beta,'%3.1f') ' $^\circ$']...
      ['$\xi$ = ' num2str(xi,'%3.1f') ' $^\circ$']...
      ['$d$ = ' num2str(d,'%2.1f') ' m']...
      ['$b$ = ' num2str(b,'%2.1f') ' m']...
      ['$\kappa$ = ' num2str(kappa,'%1.5f')]};
th = text(infoxy(1), infoxy(2), t2,...
     'horizontalalignment','left',...
     'verticalalignment','top',...
     'edgecolor',[0 0 0],...
     'fontsize',12);
set(th, 'backgroundcolor', [1 1 1]);

set(ax1, 'position',[0.1 0.15 0.8 0.75]);


%%
return
[fpath,fname,fext] = fileparts(data_file);
print(fig, '-depsc', '-r300', [fname '.eps']);
print(fig, '-dpdf', '-r300', [fname '.pdf']);
set(get(ax1,'xlabel'),'Interpreter','tex');
set(get(ax1,'ylabel'),'Interpreter','tex');
print(fig, '-dpng', '-r300', [fname '.png']);

