%%----------------------------------------------------------------------
%
% Script to plot and store the gradiometer data aquired during the field
% experiment
%
%%----------------------------------------------------------------------
%
% 2018/05/09  V2.0  update by Andreas Brotzer 
%
%  
%  - data file and header file must be in the working directory. 
%  - seis_color.txt must be located in the same directory as the data.
%%%----------------------------------------------------------------------


clear all; close all; clc;

%----------------------------------------------------------------------
% user settings

data_file1 = 'rietheim_a59-15.dat'; % change name string to your data
data_file2 = 'rietheim_a59-15.dat'; % possible second data grid
header_file='rietheim_a59-15.hdr'; % change name string to your header file name

align = 'off'; % 'ontop' (default) or 'nextto' or 'off'

contoursteps = 30;  % defines the step size of the contour lines (default 30)

outputfilename='test'; % name of the output files (e.g. figures). Not same as data_file


% ###############################################
% There should not be changed anything hereafter! 
% ###############################################


%----------------------------------------------------------------------
% load data:

%------- first Grid ---------------------

kartierung=load(data_file1);

%------- second Grid ---------------------

kartierung2=load(data_file2);
kartierung2=kartierung2(1,:);

%------- header file ---------------------

% read header information
file=fopen(header_file,'r');
header=textscan(file,'Time = %s Date = %s %s %s Grid Size = %f x %f Method of collection = %s Starting Direction =%s Data Range =%f nT Line Spacing =%f m Sampling =%f samples / m  Sensor Spacing =%f m %s Mean =%f Max =%f Min =%f','Delimiter','\n');
fclose(file);

%----------------------------------------------------------------------
% align multiple dataset grids

if strcmp(align,'ontop')
    %----- on top of each other ---------
    kartierung=[kartierung ; kartierung2 ];
elseif strcmp(align,'off')
    kartierung=kartierung;
elseif strcmp(align,'nextto')
    %-----next to each other ----------
    kartierung=[kartierung  kartierung2 ];
end

%----------------------------------------------------------------------
% automaticParameter setting

[zeilen,spalten]=size(kartierung);

dy=header{10}; % Abstand der Profile in m (default 1 m)
dx=1/header{11}; % Abstand der Messpunkte in einem Profil (default 1/8)
clip1=max(abs(header{15}),abs(header{16})); %clip für die Darstellung (default 1000)
clip2=-clip1;

%dx_new=1; %gewünschter Gridpunktabstand in  Profilrichtung nach interpolation

%----------------------------------------------------------------------
% set coordinate parameters
xend=spalten*dx-dx;
yend=zeilen*dy-dy;  
xnew = 0:dx:xend;
ynew= 0:dx:yend;

%----------------------------------------------------------------------
% interpolation in y direction (by default 1 m profile spacing is
% interpolated)
for n=1:spalten
    v=kartierung(:,n);
    %vv=interp1(v,v(1):dx:v(end),'PCHIP');
    vv=interp1(v,1:dx:yend+1,'linear');
    kartierung_intp(:,n) = vv;
    
end

%----------------------------------------------------------------------
%---Bearbeitungen

%----Spiegeln x Achse---------------
%kartierung_intp=fliplr(kartierung_intp);
%---Spiegeln y Achse----------------
% temp=kartierung_intp;
% for ii=1:zeilen     
%     kartierung_intp(ii,:)=temp(zeilen-ii+1,:);
% end

%----------------------------------------------------------------------
%---rotate clockwise 90° ----------
%kartierung_intp=fliplr(kartierung_intp');
%kartierung_intp=rot90(fliplr(kartierung_intp'));

%----------------------------------------------------------------------
% build mesh
[X,Y] = meshgrid(0:dx:yend,xnew);

%----------------------------------------------------------------------
% plotting

for i=1:2

fig=figure();
%set(fig, 'position',[200 200 580 600]);

if i == 1
    contourf(xnew,ynew,(kartierung_intp),contoursteps);
elseif i == 2
    imagesc(xnew,ynew,(kartierung_intp));
end
%surf(X,Y,kartierung_intp);

%----------------------------------------------------------------------
% colorbar settings

colorbar2=load('seis_color.txt');

h=colorbar;
colormap(colorbar2(1:2:end,:));
c=get(h,'YLabel');
set(c,'String','Gradient der Vertikalkomponente in nT/m','fontsize',20);
caxis([clip2 clip1]);
set(gca,'fontsize',20);
set(0,'defaultTextInterpreter','latex');
set(c,'Interpreter','latex')
set(fig,'color','white')

%----------------------------------------------------------------------
% axes settings

axis equal tight;

if strcmp(strjoin(header{8}),'North-West')
    xlabel('Profilkoordinate nach Ost in m','Interpreter','latex');
    ylabel('Profilkoordinate nach Sued in m','Interpreter','latex');
else
    error('Wrong starting direction! Should be North-West.');
end
%title({'Kartierung'; 'Gradient B_z in nT/m'},'fontsize',16);

%----------------------------------------------------------------------
% additional settings

%set(gca,'XTick', tick,'YDir','reverse','XAxisLocation','top')
set(gca,'YDir','reverse','XAxisLocation','top');
%set(gca,'fontsize',20);
%set(fig, 'Position', get(0, 'Screensize'));
set(gcf,'Units','Normalized','OuterPosition',[0 0 1 1]);

%----------------------------------------------------------------------
% save created plot

% saveas(fig,outputfilename,'png')
% saveas(fig,outputfilename,'pdf')
% saveas(fig,outputfilename,'eps')


% --------- alternative method to print figures -----------
[fpath,fname,fext] = fileparts(data_file1);
if i==1; fname=[fname '_contour']; elseif i ==2; fname=[fname '_imagesc']; end
%print(fig, '-depsc', '-r0', [fname '.eps']);
print(fig, [fname '.png'], '-dpng','-r0');

orient(fig,'landscape');
print(fig, [fname '.pdf'],'-dpdf', '-Pmy printer');

end
%----------------------------------------------------------------------
% Linux commandos zum beschndeiden der Abbildungen
%eval(['!pdfcrop ' fname '.pdf ' fname '.pdf --margins 1']);
%eval(['!convert -trim ' fname '.png ' fname '.png']);


%----------------------------------------------------------------------
% End of file
%----------------------------------------------------------------------