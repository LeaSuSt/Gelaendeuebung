clear all, close all, clc;

% Kartierung Parkplatz 2016

data_file = 'rietheim_a59-15.dat';
kartierung=load(data_file);

%-------Mehrere Grids---------------------
% data_file = 'parkplatz_elabor.dat';
% kartierung2=load(data_file);

%-----   Untereinanderanordnen---------
%kartierung=[kartierung ; kartierung2 ];
%-----Nebeneinander Anodrdnen----------
%kartierung=[kartierung  kartierung2 ];

[zeilen,spalten]=size(kartierung);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Parameter
dy=1; % Abstand der Profile in m
dx=1/8; % Abstand der Messpunkte in einem Profil
dx_new=1; %gewünschter Gridpunktabstand in  Profilrichtung nach interpolation
clip1=-1000; %clip für die Darstellung
clip2=1000;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

xend=spalten*dx-dx; % Ende eines Profils in m
yend=zeilen*dy-dy;  % letztes Profil in m
xnew = 0:dx_new:xend;
ynew= 0:dy:yend;

for n=1:zeilen
    v=kartierung(n,:);
    vv=interp1(0:dx:xend,v,xnew,'PCHIP');
    kartierung_intp(n,:) = vv;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%---Bearbeitungen

%----Spiegeln x Achse---------------
%kartierung_intp=fliplr(kartierung_intp);
%---Spiegeln y Achse----------------
% temp=kartierung_intp;
% for ii=1:zeilen     
%     kartierung_intp(ii,:)=temp(zeilen-ii+1,:);
% end
%---rotieren 90° Uhrzeigersinn----------
%kartierung_intp=fliplr(kartierung_intp');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[X,Y] = meshgrid(xnew,0:9);

figure(1)
set(1, 'position',[200 200 580 600]);
%contourf(X,Y,kartierung_intp,10);
imagesc(xnew,ynew,kartierung_intp);

colorbar2=load('seis_color.txt');

h=colorbar;
colormap(colorbar2(1:2:end,:));
c=get(h,'YLabel');
set(c,'String','Gradient der Vertikalkomponente in nT/m','fontsize',14)

%tick=[5:5:35];
%set(gca,'XTick', tick,'YDir','reverse','XAxisLocation','top')
set(gca,'YDir','reverse','XAxisLocation','top');

axis square;
caxis([clip1 clip2]);

xlabel('Profilmeter in Ostrichtung','fontsize',14);
ylabel('Profilmeter in Suedrichtung','fontsize',14);
% title({'Kartierung '; 'Gradient B_z in nT/m'},'fontsize',14)

[fpath,fname,fext] = fileparts(data_file);
print(1, '-depsc', '-r300', [fname '.eps']);
print(1, '-dpdf', '-r300', [fname '.pdf']);
set(get(gca,'xlabel'),'Interpreter','tex');
set(get(gca,'ylabel'),'Interpreter','tex');
set(c,'Interpreter','tex')
print(1, '-dpng', '-r300', [fname '.png']);
% Linux commandos zum beschndeiden der Abbildungen
%eval(['!pdfcrop ' fname '.pdf ' fname '.pdf --margins 1']);
%eval(['!convert -trim ' fname '.png ' fname '.png']);
