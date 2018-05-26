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

data_file1 = 'traktortest7.dat'; % change name string to your data
data_file2 = 'traktortest7.dat'; % possible second data grid
header_file='traktortest7.hdr'; % change name string to your header file name

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

%------- plot series ---------------------


fig=figure();

plot(0:1/8:30-1/8,kartierung(1,:),'linewidth',2)

set(gca,'fontsize',22);
set(0,'defaultTextInterpreter','latex');
set(gcf,'Units','Normalized','OuterPosition',[0 0 1 1]);
set(fig,'color','white');


title('Störkörper: Traktor mit Anhänger (fahrend)');
xlabel('Zeit in s');
ylabel('Gradient der Vertikalkomponente in nT/m');

grid on;

%------- print plot ---------------------

[fpath,fname,fext] = fileparts(data_file1);
print(fig, [fname '.pdf'], '-dpdf','-r0');



%----------------------------------------------------------------------
% End of file
%----------------------------------------------------------------------
