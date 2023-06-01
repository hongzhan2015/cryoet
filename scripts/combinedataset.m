%%% Substitute the input to the filename, using 'FILENAME.mat' %%%
function Myoutput = combinedataset(input) 

% Load variable into matlab working environment
load(input);
% Make a point to the variable
file = subTomoMeta.cycle004.ClusterClsGeom;
% Import all tilt names
filename = fieldnames(file);
% Number of tilts
tiltnum=numel(filename);
% Create an empty matrix
Myoutput = [];
% Append all data to one dataframe
for i = 1:tiltnum
    var = file.(filename{i});
    [m,n] = size(var);
    textcol = cell(m,1);
    textcol(:) = {filename(i)};
    var = [num2cell(var),textcol];
    Myoutput = [Myoutput; var];
end

%% to save files %%
% dataframe = cell2table(data);
% writetable(dataframe,'cycle004_classification.csv');