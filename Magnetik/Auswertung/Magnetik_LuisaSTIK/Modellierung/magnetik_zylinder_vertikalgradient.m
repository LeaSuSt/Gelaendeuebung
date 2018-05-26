clear all, close all, clc;

%%
% #########################################################################
% Programm zur Modellierung des Magnetfeldes
% Modell: horizontal liegender Zylinder, der in horizontale Richtung unendlich ausgedehnt ist
% Vertikalgradient der Vertikalkomponente berechnet mit Formel 3.34 aud Telford et al. (1976)
% #########################################################################
% Es kann ein Zylinder entlang des Messprofils berücksichtigt werden.
% #########################################################################
%
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
%   ZZ_GRAD: Vertikalgradient der Vertikalkomponente des Anomaliefeldes (Modell horizontaler Zylinder), (in nT)
% 
% 
% ### Messwerte ###
% 
%  Format der einzulesenden Datei: 
%   Spalte 1: Profilkoordinate in m
%   Spalte 2: Messwerte in nT, mit Punkte als Trennzeichen der Dezimalzahlen;
%   Die Spalten werden durch Leerzeichen getrennt.
%   Bsp: 0 47655.78
% 
%  XSHIFT: Auf XSHIFT wird der Ursprung des Koordinatensystems der Modellierung gelegt. (in m)
% 
% 
% ### Modellierung ###
% 
%  gesetzte Variablen:
%   beta ...... Streichwinkel des Zylinders relativ zur Feldrichtung (in °)
%   kappa ..... magnetische Suszeptibilitaet
%   rz ........ Radius des Zylinders (in m)
%   z ......... Tiefe des Mittelpunktes der Querschnittsflaeche (in m)
%               bzgl. des Mittelpunktes des Gradiometers
%   d_sonde ... Sondenabstand
% 
%  berechnete Variablen:
%   S: Querschnittsflaeche (S=r**2*pi) (in m^2)
%   r: Abstand Aufpunkt - Mittelpunkt Querschnittsflaeche (in m)
% 
%  Laufvariable:
%   x: Abstand zum Aufpunkt (in m)


%% INPUT

% =================================
% Gradiometer-Messdaten
% =================================
% Textdatei mit 2 Spalten: 1 = Koordinate, 2 = Messwert
data_file   = 'A81_2016_Weg_out.txt';
profil_spiegeln = 1;       % Profil soll in der Darstellung von West nach Ost verlaufen

% =================================
% Variablendefinition (Winkel in ° angeben!)
% =================================
IH        = 63.75;       % Inklination des Hintergrundfeldes (in °)
TH        = 47000;       % Totalintensitaet des Hintergrundfeldes (in nT)
beta      = 45;          % Streichwinkel des Zylinders (abgetragen im Uhrzeigersinn, in °, 0°=N-S-Richtung)
z         = 13;          % Tiefe des Mittelpunktes der Querschnittsflaeche (in m)
                         % Tiefe bezieht sich auf Gradiometermittelpunkt
rz        = 4.5;          % Radius der Zylinderroehre (in m)
kappa     = 0.0337;      % magnetische Suszeptibilitaet
XPOS      = 14.5;           % Position des Zylinders (in m)
DATASHIFT = -40.0;       % Offset der Messwerte (Wert der außerhalb der Anomalie gemessen wird)
d_sonde   = 1;           % Sondenabstand des Gradiometers

% =================================
% Einstellungen der Abbildung
% =================================
xrange        = [-20 50];      % x-Achsen-Begrenzung
datarange     = [-500 1500];  % y-Achsen-Begrenzung
datarange_grad     = [-100 200];  % y-Achsen-Begrenzung
infoxy        = [25 1200];     % Koordinaten (x,y) für Infobox mit Zylinderparametern

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


%% Vektoren
x0 = xrange(1):dx:xrange(2);
x = x0 - XPOS;


%% Berechnung der Elemente der Magnetfelder
% =================================
% Komponenten des Hintergrundfeldes
ZH = sin(IH_rad)*TH;
HH = cos(IH_rad)*TH;

% =================================
% Hier wird eine Gradiometermessung simuliert.
% Berechnung des Anomalienfeldes für die vorgegebene Tiefe z und (z + Sondenabstand)
% =================================
% Komponenten des Anomaliefeldes fuer die Modellierung eines horizontalen Zylinders
r_bottom = sqrt((z-d_sonde/2)^2+x.^2);
r_top = sqrt((z+d_sonde/2)^2+x.^2);
S = pi*rz^2;
% Vertikalkomponente des horizontalen Zylinders nach Gl. 3.3.34 (Telford et al., 1976)
ZZ_bottom = ((2*kappa*S)./r_bottom.^4).*(2*HH*x*(z-d_sonde/2)*sin(beta_rad)+ZH*((z-d_sonde/2)^2-x.^2));
ZZ_top = ((2*kappa*S)./r_top.^4).*(2*HH*x*(z+d_sonde/2)*sin(beta_rad)+ZH*((z+d_sonde/2)^2-x.^2));

ZZ_GRAD = ZZ_bottom - ZZ_top;

%% Daten laden
fp = fopen(data_file);
A=textscan(fp, '%f %f', 'delimiter','\t', 'commentstyle','#');
fclose(fp);
profil = A{1};
daten = A{2};

if profil_spiegeln
    daten=fliplr(daten');
end

%% Erstellung der Abbildung
set(0,'DefaultTextInterpreter','latex');
figure(fig);
set(fig, 'position',[100 50 1000 450]);

ax1 = axes('position',[0.1 0.1 0.35 0.75]);
plot(x0, ZZ_bottom, 'color',[0.8 0 0], 'linewidth',1);
hold on;
box on;
grid on;
plot(x0, ZZ_top, 'color',[0 0 0.8], 'linewidth',1);
xlim(xrange);
ylim(datarange);
xlabel('\bf Profilkoordinate in m', 'fontsize',12);
ylabel('\bf Flussdichte der z-Komponente in nT', 'fontsize',12);
t1 = sprintf(['Anomalie der Vertikalkomponente\n(Annahme: 1 horizontaler Zylinder)']);
title(t1, 'fontsize',14, 'visible','on');

t2 = ['$I_\mathrm{H}$ = ' num2str(IH,'%3.2f') ' $^\circ$'];
% t2 = ['$I_\mathrm{H}$ = ' num2str(IH,'%3.2f') ' Grad'];
lh = legend('untere Sonde', sprintf(['obere Sonde\n(Sondenabstand = ' num2str(d_sonde,'%1.1f') ' m)']));
set(lh, 'location','southeast', 'interpreter','latex');

t3 = {'\bf Zylinder:'...
      ['$\beta$ = ' num2str(beta,'%3.1f') ' $^\circ$']...
      ['$z$ = ' num2str(z,'%2.1f') ' m']...
      ['$r$ = ' num2str(rz,'%2.1f') ' m']...
      ['$\kappa$ = ' num2str(kappa,'%1.5f')]};
th = text(infoxy(1), infoxy(2), t3,...
     'horizontalalignment','left',...
     'verticalalignment','top',...
     'edgecolor',[0 0 0],...
     'fontsize',12);
set(th, 'backgroundcolor', [1 1 1]);
 
set(ax1, 'position',[0.1 0.1 0.35 0.75]);

% ===

ax2 = axes('position',[0.55 0.1 0.35 0.75]);
plot(x0, ZZ_GRAD, 'color',[1 1 1]*0.3, 'linewidth',1);
hold on;
box on;
grid on;
plot(profil-XPOS,daten-DATASHIFT, 'color',[0 0 0], 'linestyle','none',...
     'marker','o', 'markerfacecolor',[0 0 0], 'markersize',4);
 legend('modellierte Daten', 'Messdaten');
xlim(xrange);
ylim(datarange_grad);
xlabel('\bf Profilkoordinate in m', 'fontsize',12);
ylabel(['\hspace{6em} \bf ' sprintf('Vertikalgradient \n') '\bf der z-Komponente der Flussdichte in nT/m'],...
       'fontsize',12, 'fontweight','bold');
t1 = sprintf(['Anomalie des Vertikalgradienten\n(Annahme: 1 horizontaler Zylinder)']);
title(t1, 'fontsize',14, 'visible','on');

set(ax2, 'position',[0.55 0.1 0.35 0.75]);

%%
return
[fpath,fname,fext] = fileparts(data_file);
print(fig, '-depsc', '-r300', [fname '.eps']);
print(fig, '-dpdf', '-r300', [fname '.pdf']);
set(get(ax1,'xlabel'),'Interpreter','tex');
set(get(ax1,'ylabel'),'Interpreter','tex');
print(fig, '-dpng', '-r300', [fname '.png']);
