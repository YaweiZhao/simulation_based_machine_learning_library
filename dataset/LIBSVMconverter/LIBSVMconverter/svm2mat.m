function [data, label] =svm2mat(s,n,d)
% Usage: y=svm2mat ('filename',number, dimension)
fid = fopen(s);
data = zeros(n,d);
label=zeros(n,1);
i=1;
while ~feof(fid) % not end of the file 
       s = fgetl(fid); % get a line 
       data_char=[];  j=1;
       data_values=[];
       index_char=[];
       index_values=[];
       while (j<=length(s))
             while( s(j)~=' ')    
                   data_char=[data_char s(j)];
                   j=j+1;   
             end  
             j=j+1;   
             data_char=[data_char ' '];
             while ( (j<length(s)) && (s(j)~=':') )  
                    index_char = [index_char s(j)];
                    j=j+1;   
             end 
             index_char = [index_char ' '];
             j=j+1;   
       end
        index_values=str2num(index_char);%the array of index values for a line
        data_values=str2num(data_char) ;%the array of data values for a line
        label(i,:) = data_values(1);
        data(i, index_values) =  data_values(:,2:length(data_values));
        i=i+1; 
end

data = [label data];
fn_dest = 'covtype.mat';
save(fn_dest, 'data');
end

