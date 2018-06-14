
clear
close all

disp ' '
disp '   ++++++++++++++++++++++++++++++++++++++++++++++++++++'
disp '   +  Geophysikalisches Feldpraktikum                 +'
disp '   +                                                  +'
disp '   +  R I E D H E I M E R  G A N G                    +'
disp '   +                                                  +'
disp '   +  Model 1: thin sheet of infinite strike length   +'
disp '   +  Model 2: mass line                              +'
disp '   ++++++++++++++++++++++++++++++++++++++++++++++++++++'
disp ' '
disp ' '
%------------------------------------------------------------------------- 

% Stand: 10.05.2014  MW
% Stand: 22.05.2014  MW; Winkelangabe in Ausgabeplot

blahblahblah={' TRENDS: Die Bougueranomalie in Riedheim enthaelt moeglicherweise '...
              ' einen linearen Trend, der in den Modellen (1) "schmales Blatt" '...
              ' und (2) "liegender Zylinder" nicht enthalten ist. Deshalb kann '...
              ' in der Ausgleichung ein linearer Trend mitgeschaetzt werden. '...
              ' Bei MODELL 1 kann der Trend allerdigs nur schwer von einer '...
              ' Asymmetrie der Anomalie auf Grund eines von 90 Grad abweichenden '... 
              ' Einfallens der Schicht separiert werden. Deshalb kann die Schaetzung '...
              ' des Trends für dieses Modell ein-/ausgeschaltet werden. Bei der '...
              ' Variante "A priori Trend" werden die Daten vor der Ausgleichung '...
              ' trendbefreit (MATLAB-Befehl detrend)'...
              '   ',...
              ' WINKEL: fuer 2-D Strukturen haengt der Schwereeffekt nur vom Abstand ',...
              ' des Messpunktes von der Struktur ab; bei schraegem Profilverlauf ',...
              ' kann das Profil daher auf ein senkrechtes Profil projiziert werden. ',...
              ' Dies gilt zumindest für die Massenlinie. ',...
              '   ',...
              ' 1-D INTEGRATION der Schwerewerte zur Berechnung der gesamten ',...
              ' Stoermasse ist ungenau, da das Nullniveau der Schwereanomalie ',...
              ' nicht bekannt ist. Die "Extension" von Duerrbaum/Fritsch gilt ',...
              ' nur für Modell 2 (Massenlinie). Tests mit Daten aus Riedheim zeigen, '...
              ' dass 1-D Integration und Modellierung nur dann etwa uebereinstimmen, '...
              ' wenn ein Winkel zwischen Profilverlauf und Streichrichtung der ',...
              ' Massenlinie angenommen wird. Die o.g. Extension muesste dahingehend ',...
              ' noch weiter ueberprueft werden. Zur Ausgabe des derzeitigen Ergebnisses ',...
              ' die Variable "vergleich" anzeigen lassen.'...
              '   ',...
              ' STOCHASTISCHES MODELL: alle Beobachtungen gleichgenau. Der Varianz-',...
              ' faktor entspricht der Varianz des Residuums dividiert durch Anzahl der ',...
              ' Freiheitsgrade'};
words_of_wisdom=textwrap(blahblahblah,80);

% colordef black

% -------- Default-Einstellungen --------------------

  G = 6.6726e-11;  % Gravitationskonstante
  numlines=1;      % Optionen für Input-Dialog-Fenster      
  prompt=('Name des Datenfiles:');
  namedatfile=('INPUT DATEN'); 
  options.Resize='on';
  options.WindowStyle='modal';
  options.Interpreter='none';
  defaultfile={'riedheim2012.txt'};
   
% ----- Einlesen und Darstellung der Daten ----------
  [datfile,pathname,findex]=uigetfile('*.*', 'Select an Inputfile');
  fid = fopen([pathname,datfile],'rt');   % Datenfile
  
  [was,wert,einheit]=textread([pathname,datfile],'%s%f%s',1);
  for i=1:4 fgets(fid); end
  D1=str2num(fgetl(fid));   %Anzahl der Datenspalten
  m=length(D1);
  
  [D2]=fscanf(fid,'%f',[m,inf]); 
  fclose(fid);
  D=[D1',D2]';
  
  sigma_def=wert(1);    %Messfehler
  sobs = D(:,1);
  hobs = D(:,2);
  gobs = D(:,3);        %*1e-5, falls Umrechnung [mgal -> m/s^2]
  n=length(gobs);

  for i=1:n c(i)=1; end    % konstanter Vektor fuer Ausgleichung
  c=c';
  
% ---------------- Plot der Schwereanomalie  ----------------------
% Figures anordnen
  set(0,'Units','pixels')
  scnsize = get(0,'ScreenSize');
  fig1=figure;
  position=get(fig1,'Position');
  outerpos=get(fig1,'OuterPosition');
  borders=outerpos-position;
  edge=-borders(1)/2;
  pos1=[edge,scnsize(4)*(1/2),scnsize(3)/2-edge,scnsize(4)/2];
  pos2=[scnsize(3)/2+edge,pos1(2),pos1(3),pos1(4)];
  set(fig1,'OuterPosition',pos1)
  
  plot(sobs,gobs,'-o');
  xlabel('Profilpunkte / m');
  ylabel('Bougueranomalie / mgal');
  title('Riedheimer Gang: Bougueranomalie');
  
% ---------------- Modell und Modellparameter ---------------------
  disp ' '  
  ButtonName = questdlg('Welches Modell darf es denn sein:', ...
                         'Schweremodellierung', ...
                         'Spaltenintrusion','Basaltfluss','Spaltenintrusion');
   switch ButtonName,
     case 'Spaltenintrusion',
       modnr=1;
       disp 'Spaltenintrusion: es wird das Modell 1 "Schraeges Blatt" verwendet';
     case 'Basaltfluss',
       modnr=0;
       disp 'Basaltfluss: es wird das Modell 2 "Massenlinie" verwendet';
   end % switch
  
% ------ Vorgabe für Einlesen der Modellparameter ----------------
  nameinput='Eingabe der Modellparameter';    
  if modnr == 1
      modname='Spaltenintrusion (Modellkörper: schräges Blatt)'
      prompt={'MODELL 1: Profillage des Schweremaximums (in meter):',...
              'MODELL 1: Tiefe des Scheitelpunktes des Störkörpers (in meter):'...
              'MODELL 1: Tiefenerstreckung des Störkörpers (in meter)',...
              'MODELL 1: Einfallen [Grad, W+, E-]'...
              'MODELL 1: Winkel zw. Messprofil und Streichrichtung des Störkörpers'...
              'Optional: linearen Trend schaetzen [Ja=1, Nein=0]'...
              'Optional: a priori Trend abziehen [Ja=1, Nein=0]'...
              'Optional: mittlerer Fehler der Beobachtungen (in mgal):'...
              'Optional: a priori Dichteunterschied Basalt/Umgebungsmaterial (in kg/m^3);'};
      defaultvalues={num2str(50),num2str(8),num2str(200),num2str(90),num2str(90)...
                     num2str(0),num2str(0),num2str(sigma_def),num2str(750)};
  else
      modname='Basaltgang (Modellkörper: Massenlinie)'
      prompt={'MODELL 2: Profillage dg-Maximum (in meter):'...
              'MODELL 2: Profillage dg-Halbwert (in meter):'...
              'MODELL 2: Winkel zw. Messprofil und Streichrichtung der Massenlinie'...
              'Optional: mittlerer Fehler der Beobachtungen (in mgal):'...
              'Optional: a priori Dichteunterschied Basalt/Umgebungsmaterial (in kg/m^3)};'};
      defaultvalues={num2str(50),num2str(25),num2str(90),num2str(sigma_def),num2str(750)};
  end
  
%% -------- Berechnung der Schwereanomalie -----------
  weiter=1;
  while weiter > 0
      
  % -------- Eingabe der Modellparameter
  %
    if modnr == 1
        newvalues=inputdlg(prompt,nameinput,numlines,defaultvalues,options);      
        smax=str2num(newvalues{1});
        dep=str2num(newvalues{2});
        z=hobs+dep;
        l=str2num(newvalues{3});
        a=str2num(newvalues{4})/180*pi;
        aplot=a;                         %fuer Ausgabe im Plot
        if a<0 a=a+pi; end
        azi=str2num(newvalues{5})/180*pi;
        trd=str2num(newvalues{6});
        out=trd+2;
        aprioritrd=str2num(newvalues{7});
        if and(trd,aprioritrd)
            hinweis='linearer Trend wird ausgeglichen, nicht a priori entfernt!';
            msgbox(hinweis,'Achtung: beides geht nicht!','warn')     
            aprioritrend=0;
        end
        sigma_g=str2num(newvalues{8});
        drho=str2num(newvalues{9});
        erg1='Breite';
        erg2='(oberflächennächster Punkt)';
        erg3=erg1;
        
  % Korrektur Profilverlauf
        s=sobs*sin(azi);
        smax=smax*sin(azi);
         
  % Berechnung der Schwerewirkung des Ganges fuer Breite*Dichteunterschied brho=1
        ta=0.5*sin(a)*log(((z+l*sin(a)).^2+((s-smax)+l*cos(a)).^2)./(z.^2+(s-smax).^2));
        tb=cos(a)*atan((z*sin(a)+l+(s-smax).*cos(a))./((s-smax).*sin(a)-z*cos(a)));
        tc=cos(a)*atan((z*sin(a)+(s-smax).*cos(a))./((s-smax).*sin(a)-z*cos(a)));
        mod=2*G*(ta-tb+tc);
        mod=mod*1e5;          %Umrechnung in mgal
        mod=mod-mean(mod);       
    else
        newvalues=inputdlg(prompt,nameinput,numlines,defaultvalues,options);      
        smax=str2num(newvalues{1});
        shalb=str2num(newvalues{2});
        azi=str2num(newvalues{3})/180*pi;
        sigma_g=str2num(newvalues{4});
        drho=str2num(newvalues{5});
        dep=abs(smax-shalb);  
        disp 'Tiefenlage der Massenlinie = g_max - g_halbmax'
        
  % Korrektur Profilverlauf
        s=sobs*sin(azi);
        smax=smax*sin(azi);
        shalb=shalb*sin(azi);
        
  % Berechnung der Schwerewirkung des Zylinders für Radius r=1
        mod=2*G*pi*dep./((s-smax).^2+dep^2);
        modmax=2*G*pi/dep*1e5;
        mod=mod*1e5;          %Umrechnung in mgal
        mod=mod-mean(mod);
        erg1='Radius^2';
        erg2='(Oberkante)';
        erg3='Radius';
        trd=1;                %Trend immer mitschätzen
        aprioritrd=0;         %Daten nicht trend-befreien 
        out=trd+2;       
    end

  % -------------Alternative 1: Regression Messung - Modell-------------------------------
  % Durch Regression Messung - Modell kann das Produkt b*drho bestimmt werden:
  % hier als Test mitberechnet
  % b = Breite des Ganges
  % drho = Dichtedifferenz zwischen Basalt und umliegendem Gestein
  % Regressionskoeffizient <=> b*drho 
  %  greg=detrend(gobs);
  %  brhoreg = sum(greg.*mod)./sum(mod.*mod);
  %  ereg=greg-brhoreg*mod;                           % Residuum
  %  sigma=sqrt(sum(ereg.*ereg)/sum(mod.*mod)/(n-1)); % Standardabweichung

  % -------------Alternative 2:  Ausgleichung---------------------------------------------
  %
  % modelliert werden: 
  % (1) ein Offset zwischen Modell und gemessener Schwere
  % (2) ein linearer Trend 
  % (3) das Modell fuer den Tunnel (siehe dazu Skript)
  % Ergebnis: koeff(3) enthaelt den gesuchten Parameter, naemlich das Produkt aus
  % Dichteunterschied und Breite des Ganges 
  
  % Optionale Korrekturen an den Messdaten
    g=gobs;
    if aprioritrd==1 g=detrend(g); end     % apriori Trendkorrektur
    
  % Ausgleichung
    if trd == 1
        A=[c,s,mod];  %Komma fuer Spaltenvektoren; Semikolon fuer Zeilenvektoren
    else
        A=[c,mod];        
    end
    koeff=(A'*A)\(A'*g);   %alternative Formulierung in MATLAB 
    
  % Residuum 
    e = g - A*koeff;
    
  % Anzahl Freiheitsgrade
    liberte=n-length(koeff);
  
  % Fehlerrechnung
    q=diag(inv(A'*A));
    ete=e'*e;
    m0=sqrt(ete/liberte);  
    mx=m0*sqrt(q);  
    
  % Berechnung Ausgabevariable und gesamte Stoermasse/m
    if modnr == 1
        v=l;                                  %ell!
        kout=koeff(out)/drho;
        mxout=mx(out)/drho;                   %linear
        dout=dep-kout/2*abs(cos(a));
        dxout=mxout/2*abs(cos(a));
    else
        v=pi;
        kout=sqrt(koeff(out)/drho);
        mxout=mx(out)/(sqrt(2)*kout*drho);    %quadratisch
        dout=dep-kout;
        dxout=mxout;
    end
  
  % Berechnung der CHI-Quadrat Variablen:
    chiq = sum(e.^2./(sigma_g.^2));
    chiqn = chiq/liberte;
    str3=[' Chi-Quadrat:   ',num2str(chiq)];
    str4=[' Chi-Quadrat normalized:   ',num2str(chiqn)];
  
    disp '   '
    disp ' Modellparameter und Ergebnisse'
    disp '================================'
    if modnr==1
        tm1=[' Fallwinkel [W+, E-]:',' ',num2str(aplot*180/pi),' Grad',];
        tm3=[' Tiefenerstreckung des Störkörpers:',' ',num2str(l),' m',];
        t3=[' ',erg3,' fuer Dichteunterschied ',num2str(drho),' kg/m^3: ',num2str(kout),' +/- ',num2str(mxout),' m'];
    end        
    tm2=[' Profilkoordinate des Maximums:',' ',num2str(smax),' m',];
    tm4=[' Winkel zw. Messprofil und Streichrichtung des Störkörpers;',' ',num2str(azi*180/pi),'  Grad',];
    t1=[' Tiefe des Störkörpers ',erg2,':  ',num2str(dout),' +/- ',num2str(dxout),' m'];
    t2=[' ',erg1,'*Dichteunterschied Basalt/Hostrock: ',num2str(koeff(out)),' +/- ',num2str(mx(out)),' m*kg/m^3'];
    t4=[' Stoermasse/m: ',num2str(v*koeff(out)),' +/- ',num2str(v*mx(out)),' kg/m'];
    t5=[' Stoermasse/m: ',num2str(v*koeff(out)),' +/- ',num2str(v*mx(out)),' kg/m'];
    t6=[' Varianzfaktor: ',num2str(ete/liberte),' mgal^2'];
    t7=[' Standardabweichung a priori: ',num2str(sigma_g),' mgal']; 
    t8=[' Standardabweichung a posteriori: ',num2str(round(m0*1000)/1000),' mgal']; 
    disp(tm2)
    if modnr==1
         disp(tm3)
         disp(tm1)
    end
    disp(tm4)
    disp(t1)
    disp(t2)
    if modnr==1 disp(t3); end
    disp(t4)
    disp(t6)
    disp(str4)
    disp(t7)
    disp(t8)
    disp ' ' 
    
% Zum Vergleich: Berechnung der Gesamt-Störmasse aus Messwerten.
% Problem: Nullniveau der Schwere wird nicht erreicht. Für Massenlinie
% gibt es eine "Extension" nach Dürrbaum/Fritsch ("Angewandte
% Geowissenschaften, die aber (wenn überhaupt) nur für die Massenlinie
% gültig ist. 
% #Mai 2012: Ausgabe auskommentiert#
    sint=diff(sobs*sin(azi));
    sint(n)=sint(1);
    gdet=detrend(gobs)*1e-5;          %mgal -> m/s^2
    gint=(gdet-min(gdet));      
    sgint=sum(sint.*gint)/(2*pi*G);   %1-D Integration (Grundlage: Gauss Theorem)
  if modnr == 0
      total=modmax*koeff(out)*1e-5;
      extension=acos(sqrt((total-(max(gdet)-min(gdet)))/total))*2/pi;  %2-D Erweiterung lt. Dürrbaum/Fritsch
      vergleich= [' 1-D Integration der Schwerewerte ergibt eine Störmasse: ',num2str(sgint/extension),' kg/m'];
  else
      vergleich= [' 1-D Integration der Schwerewerte ergibt eine Störmasse: ',num2str(sgint),' kg/m'];
  end
%      disp(vergleich)
%      disp ' '

  % Darstellung des Ergebnisses
    lintrend=0;
    if trd == 1; lintrend=koeff(2); end
    gred = g-s*lintrend-koeff(1);       % Abziehen des Offsets und des ausgeglichenen linearen Trends
    gmod = koeff(out)*mod;              % das Modell mit ausgeglichenem Dichteunterschied Delta_rho
    fig2=figure;
    set(fig2,'OuterPosition',pos1)

    plot(sobs,gred,'o',sobs,gmod,'r');
    xlabel('Profilpunkte / m');
    ylabel('Bougueranomalie / mgal');
    title('Riedheimer Gang : Beobachtung (blau), Modell (rot)');
    H1=gcf;
  % disp 'hit any key'
  % pause
        
  % Plot des Residuums 
    fig3=figure;
    set(fig3,'OuterPosition',pos2)

    plot(sobs,e,'*');
    xmin=sobs(1)-5;
    xmax=sobs(n)+5;
    if max(e)>sigma_g
        ymin=max(e)*(-3.5);
        ymax=max(e)*2.5;
        axis([xmin xmax ymin ymax])
    else
        ymin=sigma_g*(-1.2);
        ymax=sigma_g*0.8;
        axis([xmin xmax ymin ymax])
    end
    xlabel('Profilpunkte / m');
    ylabel('Residuum / mgal');
    title('Riedheimer Gang : Schwereresiduum');
    ydf=(ymax-ymin)/20;
    if modnr==1 
        text(xmin+1,ymin+ydf*18.5,[modname,',  ','Einfallswinkel [W+,E-]:',' ',num2str(aplot*180/pi),'  Grad']); 
    else
        text(xmin+1,ymin+ydf*18.5,[modname]); 
    end
    text(xmin+1,ymin+ydf*6,[' Tiefe des Störkörpers ',erg2,':  ',num2str(dout),' +/- ',num2str(dxout),' m']);
    text(xmin+1,ymin+ydf*5,[' ',erg1,'*Dichteunterschied Basalt/Hostrock: ',num2str(koeff(out)),' +/- ',num2str(mx(out)),' m*kg/m^3']);
    if modnr==1 text(xmin+1,ymin+ydf*4,[' ',erg3,' fuer Dichteunterschied ',num2str(drho),' kg/m^3: ',num2str(kout),' +/- ',num2str(mxout),' m']); end
    text(xmin+1,ymin+ydf*3,[' Stoermasse/m: ',num2str(v*koeff(out)),' +/- ',num2str(v*mx(out)),' kg/m']);
    text(xmin+1,ymin+ydf*2,[' Standardabweichung des Residuums: ',num2str(round(m0*1000)/1000),' mgal']);
    text(xmin+1,ymin+ydf*1,[' Chi-Quadrat normalized:   ',num2str(chiqn)]);
    H2=gcf;
% ---------------------------------------------------

    disp '   '
    Schulz = questdlg('Das Ergebnis ist:', ...
                      'War`s das?', ...
                      'koestlich','nicht koestlich','koestlich');
    switch Schulz,
      case 'koestlich',
        weiter=0;
      case 'nicht koestlich',
        weiter=1;
    end % switch

    if weiter == 1
        clear defaultvalues
        defaultvalues=newvalues;
        clear newvalues
        close gcf
        close gcf
    end %(if)
  end %while 
 
% Ausgabe in File
  [outname,pathout,fid]=uiputfile('*.*',' Select an Outputfile');
  outfile=[pathout,outname];
  fid = fopen(outfile,'w');   % Datenfile
  result=[sobs'; g'; (gmod+g-gred)'];
  for i=1 : length(newvalues)
      fprintf(fid,'%s%s%s\r\n',cell2mat(prompt(i)),'   ',cell2mat(newvalues(i)));
  end
  fprintf(fid,'%s\r\n',' ');
  fprintf(fid,'%s\r\n',' ERGEBNISSE');
  fprintf(fid,'============================\r\n');
  fprintf(fid,'%s\r\n',t1);
  fprintf(fid,'%s\r\n',t2);
  if modnr==1 fprintf(fid,'%s\r\n',t3); end
  fprintf(fid,'%s\r\n',t4);
  fprintf(fid,'%s\r\n',t6);
  fprintf(fid,'%s\r\n',str4);
  fprintf(fid, '%s\r\n',' ');
  fprintf(fid,'      x      g-obs.     g-mod.\r\n');
  fprintf(fid,'     [m]     [mgal]     [mgal]\r\n');
  fprintf(fid,'===============================\r\n');
  fprintf(fid,'%8.1f%11.4f%11.4f\r\n',result);
  
% Abspeichern der Matlab-Figures
  pointloc=strfind(outfile,'.')-1;
  namebody=strread(outfile,(['%',num2str(pointloc),'s']));
  saveas((H1),[namebody{1},'_figure_model'],'png')
  saveas((H2),[namebody{1},'_figure_residuum'],'png')

  status=fclose('all');
 
% Ausgabe auf Bildschirm
  str1=['      x       g-obs.    g-mod.'];
  result'
  disp(str1)
  
%  close all
 
 
  