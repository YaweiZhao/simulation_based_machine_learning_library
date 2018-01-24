%ridge regression
clear;
%load data: computer_hardware
data = load('../dataset/covtype/covtype.mat');
data = data.data;
[n,d] = size(data);
label = data(:,1);
label(label==2) = -1;% all the labels are +1 or -1.
training_data = data(:,2:d);
%training_data = transpose(mapstd(training_data'));
training_data = [training_data ones(n,1)];% add 1-offset
[n,d] = size(training_data);
%initialize parameters
eta = 1e-3;%learning rate
gamma = 1e-3;% regularization coefficient
T = 100;%total number of iterations
x = zeros(d,1);%the initial parameter
loss = zeros(T,1);
%define an auxiliary matrix Q
Q = zeros(d,d);
for i=1:d-1
    Q(i,i+1) = -1;
end
Q = Q + eye(d);

loss_init = 1/n*sum(log(1+exp(-1*label .* (training_data*x))));

b = fix(0.01*n);%mini-batch
for t=1:T
    stoc_nabla_x = zeros(d,1);
    for j=1:b
        i = randi(n);
        stoc_nabla_x_temp = -(transpose(training_data(i,:))*label(i,:))/(1+exp(label(i,:)*training_data(i,:)*x));
        stoc_nabla_x = stoc_nabla_x + stoc_nabla_x_temp;
    end
    stoc_nabla_x = 1/b*stoc_nabla_x;
    cvx_begin
        variable x_unknown(d,1)
        temp1 = norm(Q*(x_unknown-x),1);
        temp2 = (x_unknown-x)' * (x_unknown-x);
        minimize (transpose(nabla_x)*(x_unknown-x) + (1/eta)*(   temp1  ));
        x = x_unknown;
    cvx_end
    %evaluate the loss
    loss(t,1) = 1/n*sum(log(1+exp(-1*label .* (training_data*x))));
end
save('loss3n_logi_ress_l2norm.mat','loss');











