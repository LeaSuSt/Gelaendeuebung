clear all, close all, clc;

%%
% #########################################################################
% Übernahme aus dem Gnuplot-Skript Zylinder.gpt
% #########################################################################
% Modell: horizontal liegender Zylinder, der in horizontale Richtung unendlich ausgedehnt ist
% Vertikalkomponente berechnet mit Formel 3.34 aud Telford et al. (1976)
% #########################################################################
% Es kann ein Zylinder entlang des Messprofils ber�cksichtigt werden.
% #########################################################################
% % Programm zur Modellierung des Magnetfeldes

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
%   ZZ: Vertikalkomponente des Anomaliefeldes (Modell horizontaler Zylinder), (in nT)
%   ZG: Vertikalkomponente des resultierenden Gesamtfeldes (in nT)
% 
% 
% ### Modellierung ###
% 
%  gesetzte Variablen:
%   beta ...... Streichwinkel des Zylinders relativ zur Feldrichtung (in °)
%   kappa ..... magnetische Suszeptibilitaet
%   rz ........ Radius des Zylinders (in m)
%   z ......... Tiefe des Mittelpunktes der Querschnittsflaeche (in m)
% 
%  berechnete Variablen:
%   S: Querschnittsflaeche (S=r**2*pi) (in m^2)
%   r: Abstand Aufpunkt - Mittelpunkt Querschnittsflaeche (in m)
% 
%  Laufvariable:
%   x: Abstand zum Aufpunkt (in m)


%% INPUT

% =================================
% Messdaten
% =================================
% Textdatei mit 2 Spalten: 1 = Koordinate, 2 = Messwert
% data_file = 'Fluxgate_M2_2013.txt';
data_file = 'Proto.txt';

% =================================
% Variablendefinition (Winkel in ° angeben!)
% =================================
% --- 2013 ---
% IH   = 63.75;            % Inklination des Hintergrundfeldes (in °)
% TH        = 47000;       % Totalintensitaet des Hintergrundfeldes (in nT)
% beta = -70;         % Streichwinkel des Zylinders (abgetragen im Uhrzeigersinn, in °, 0°=N-S-Richtung)
% z         = 14;          % Tiefe des Mittelpunktes der Querschnittsflaeche (in m)
% rz        = 7;           % Radius der Zylinderroehre (in m)
% kappa         = 0.01750;     % magnetische Suszeptibilitaet
% XPOS      = 67.7;        % Position des Zylinders (in m)
% DATASHIFT = 120.0;       % Offset der Messwerte (Wert der außerhalb der Anomalie gemessen wird)
% --- 2007 ---
IH        = 63.75;       % Inklination des Hintergrundfeldes (in °)
TH        = 47000;       % Totalintensitaet des Hintergrundfeldes (in nT)
beta      = 60;          % Streichwinkel des Zylinders (abgetragen im Uhrzeigersinn, in °, 0°=N-S-Richtung)
z         = 15;          % Tiefe des Mittelpunktes der Querschnittsflaeche (in m)
rz        = 15;          % Radius der Zylinderroehre (in m)
kappa     = 0.0037;      % magnetische Suszeptibilitaet
XPOS      = 10;          % Position des Zylinders (in m)
DATASHIFT = 115.0;       % Offset der Messwerte (Wert der außerhalb der Anomalie gemessen wird)

% =================================
% Einstellungen der Abbildung
% =================================
xrange        = [-5 30];      % x-Achsen-Begrenzung
datarange     = [-200 1200];  % y-Achsen-Begrenzung
infoxy        = [10 250];     % Koordinaten (x,y) für Infobox mit Zylinderparametern
Legende_Daten = 'Fluxgate-Messwerte 2007, Messgebiet A81, Profil M1';  % Legendeneintrag der Messwerte

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
% Komponenten des Anomaliefeldes fuer die Modellierung eines horizontalen Zylinders
r = sqrt(z^2+x.^2);
S = pi*rz^2;
% Vertikalkomponente des horizontalen Zylinders nach Gl. 3.3.34 (Telford et al., 1976)
ZZ = ((2*kappa*S)./r.^4).*(2*HH*x*z*sin(beta_rad)+ZH*(z^2-x.^2));

%% Komponenten des resultierenden Gesamtfeldes
ZG = ZH+ZZ;
ZZ1 = ZZ;
% ZZ1 = ZZ+ZZ(x+40)


%% Daten laden
fp = fopen(data_file);
A=textscan(fp, '%f %f', 'delimiter','\t', 'commentstyle','#');
fclose(fp);
profil = A{1};
daten = A{2};


%% Erstellung der Abbildung
set(0,'DefaultTextInterpreter','latex');
figure(fig);
set(fig, 'position',[100 100 800 600]);

ax1 = axes('position',[0.1 0.15 0.8 0.8]);
plot(x0, ZZ1, 'color',[1 1 1]*0.3, 'linewidth',1);
hold on;
box on;
grid on;
plot(profil,daten-DATASHIFT, 'color',[0 0 0], 'linestyle','none',...
     'marker','o', 'markerfacecolor',[0 0 0], 'markersize',4);
xlim(xrange);
ylim(datarange);
xlabel('\bf Profilkoordinate in m', 'fontsize',12);
ylabel('\bf Flussdichte der z-Komponente in nT', 'fontsize',12);

t1 = 'Anomalie der Vertikalkomponente (Annahme: 1 horizontaler Zylinder)';
title(t1, 'fontsize',14, 'visible','on');

t2 = ['$I_\mathrm{H}$ = ' num2str(IH,'%3.2f') ' $^\circ$'];
% t2 = ['$I_\mathrm{H}$ = ' num2str(IH,'%3.2f') ' Grad'];
lh = legend(['modellierte Anomalie (' t2 ')'], Legende_Daten);
set(lh, 'location','southoutside', 'interpreter','latex', 'orientation','horizontal');
lpos = get(lh,'position');
lpos(2) = 0.02;
lpos(3) = lpos(3)+0.06;
lpos(1) = lpos(1)-0.03;
set(lh,'position',lpos);

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
 
set(ax1, 'position',[0.1 0.15 0.8 0.75]);


%%

[fpath,fname,fext] = fileparts(data_file);
print(fig, '-depsc', '-r300', [fname '.eps']);
print(fig, '-dpdf', '-r300', [fname '.pdf']);
set(get(ax1,'xlabel'),'Interpreter','tex');
set(get(ax1,'ylabel'),'Interpreter','tex');
print(fig, '-dpng', '-r300', [fname '.png']);
return