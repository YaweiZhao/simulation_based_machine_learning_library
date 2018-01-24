clear;
%% logistic regression
%plot loss
loss = load('loss.mat');
loss_data = loss.loss;
num_iter = 1:100;%number of iterations
plot(num_iter,loss_data);
xlabel('# of iterations');
ylabel('loss');
%hold on;


%plot the change of x
% delta_x = load('delta_x');
% delta_x_data = delta_x.delta_x;
% plot(delta_x_data);
% xlabel('dimensions');
% ylabel('change of x');


%% ridge regression
