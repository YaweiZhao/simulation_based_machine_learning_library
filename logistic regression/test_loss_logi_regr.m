%ridge regression
clear;
%load data: computer_hardware
data = load('../dataset/covtype/covtype.txt');
data = transpose(mapstd(data'));
[n,d] = size(data);
training_data = data(:,1:d-1);
training_data = [training_data ones(n,1)];% add 1-offset
label = data(:,d);
%initialize parameters
[n,d] = size(training_data);
eta = 1e-3;%learning rate
gamma = 1e-3;% regularization coefficient
T = 3;%total number of iterations
x = zeros(d,1);%the initial parameter
loss = zeros(n,1);
%define an auxiliary matrix Q
Q = zeros(d);
for i=1:d-1
    Q(i,i+1) = -1;
end
Q = Q + eye(d);

for t=1:T
    i = randi(n);
    nabla_x = -1/n *(transpose(training_data(i,:))*label(i,:))/(1+exp(label(i,:)*training_data(i,:)*x));
    cvx_begin
        variable x_unknown(d,1)
        temp1 = norm(Q*x_unknown,1);
        temp2 = x_unknown' * x_unknown;
        minimize (transpose(nabla_x)*(x_unknown-x) + 1/eta*(   temp2  ));
        x = x_unknown;
    cvx_end
    %evaluate the loss
    loss(t,1) = 1/n*sum(ln(1+exp(-1*label .* (training_data*x))));
end
save('loss3n.txt','loss','-ascii');











