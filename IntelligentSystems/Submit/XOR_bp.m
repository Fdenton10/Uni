
% ==================
% Filename: XOR_bp.m
% ==================

rand('seed',8353);

echo on ;

% ==========================
% Back-propagation algorithm
% ==========================
%Two witnesses that I Francis Denton(18024097) I ran the program and considered the output of the code. 
%   Demonstrated to Eli Grealish(student id 18035194) 18 Feb 2020
%   Demonstrated to Ben Eaton (student id 18018782) 18 Feb 2020
% ============================================================================
% Reference: Negnevitsky, M., "Artificial Intelligence: A Guide to Intelligent  
%            Systems", 3rd edn. Addison Wesley, Harlow, England, 2011.
%            Sec. 6.4 Multilayer neural networks
% ============================================================================
% Despite the ambiguity, I believe the meaning of improving the performance
% is to lower the amount of iterations achieved upon testing. This is
% because I believe that having a faster program is improving the
% performance. Therefore the tests i conduct will be to end up getting to
% that goal.
% ============================================================================
% 1st Test Default Program
% 291 Iterations
%
% I first decided to change the learning rate parameter to 1 to see what effect this
% had on the program.
% Result - 29 Iterations
%
% I then decided to change the performance goal paremeter from 0.001 to
% 0.01 to see what effect this had on the number of iterations
% Result - 20 Iterations
%
%
% The next test I performed was to increase the learning rate rather
% sharply - from 1 to 10.
% Result - 190 iterations
% Conclusion - learning rate too high
%
% The next test i performed was to lower the learning rate back down from 10 to
% 1.5 to see if this gave me a lower number of iterations from when I had it
% set to 1.
% Result - 13 iterations - Success!
%
% I then opted to increase the performance goal again - This time from 0.01
% to 0.05.
% Result - 9 Iterations
%
% The next test was to inrease the performance goal slightly, I opted to try
% 0.20 as an increase from 0.05
% Result - 2 iterations
%
% Based on my last few tests, increasing the performance rate slightly
% decreases the number of iterations requires. Therefore I tested increase
% it to 0.25 from 0.05
% =============================================================
% Problem: The three-layer back-propagation network is required  
%          to perform logical operation Exclusive-OR.
% =============================================================

% Hit any key to define four 2-element input vectors denoted by "p". 
pause 

p=[1 0 1 0;1 1 0 0]

% Hit any key to define four 1-element target vectors denoted by "t". 
pause

t=[0 1 1 0];

% Hit any key to plot the input and target vectors
pause

figure
plotpv(p,t);
hold on;

% Hit any key to define the network architecture.
pause 

s1=2; %Two neurons in the hidden layer
s2=1; %One neuron in the output layer

% Hit any key to create the network and initialise its weights and biases.
pause 

net = newff(p,t,s1,{'tansig','purelin'},'traingd');
net.divideFcn = '';

% Hit any key to set up the frequency of the training progress to be displayed, 
% maximum number of epochs, acceptable error, and learning rate. 
pause

net.trainParam.show=1;      % Number of epochs between showing the progress
net.trainParam.epochs=1000; % Maximum number of epochs
net.trainParam.goal= 0.25;  % Performance goal
net.trainParam.lr= 1.5;      % Learning rate

% Hit any key to train the back-propagation network. 
pause 

[net,tr]=train(net,p,t);

% Hit any key to see whether the network has learned the XOR operation.
pause 

p
t
a=sim(net,p)

echo off
disp('end of XOR_bp')


