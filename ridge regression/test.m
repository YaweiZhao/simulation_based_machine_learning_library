%ridge regression
clear;
%load data: computer_hardware
data = load('../dataset/Yacht/training_data.txt');
%data = transpose(mapstd(data'));
[n,d] = size(data);
training_data = data(:,1:d-1);
training_data = [training_data ones(n,1)];% add 1-offset
label = data(:,d);
%initialize parameters
[n,d] = size(training_data);
eta = 1e-3;%learning rate
gamma = 1e-3;% regularization coefficient
T = 3*n;%total number of iterations
x = zeros(d,1);%the initial parameter
loss = zeros(n,1);
%define an auxiliary matrix Q
Q = zeros(d);
for i=1:d-1
    Q(i,i+1) = -1;
end
Q = Q + eye(d);

    %evaluate the loss
    loss_an_instance = sum(training_data .* repmat(x', n,1),2)-label;
    loss_init = 1/2*1/n*(loss_an_instance' * loss_an_instance) + gamma/2*(x'*x);

for t=1:T
    i = randi(n);
    nabla_x = 1/n*(training_data(i,:)*x - label(i,:))*transpose(training_data(i,:)) + gamma*x;
    cvx_begin
        variable x_unknown(d,1)
        temp1 = norm(Q*x_unknown,1);
        temp2 = x_unknown' * x_unknown;
        minimize (transpose(nabla_x)*(x_unknown-x) + 1/eta*(   temp1  ));
        x = x_unknown;
    cvx_end
    %evaluate the loss
    loss_an_instance = sum(training_data .* repmat(x', n,1),2)-label;
    loss(t,1) = 1/2*1/n*(loss_an_instance' * loss_an_instance) + gamma/2*(x'*x);
end
save('loss3n.txt','loss','-ascii');











