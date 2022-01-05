

% ==========================
% Filename: Perceptron_XOR.m
% ==========================

echo on ;
%
%
%
% ====================================================================
% The perceptron: an attempt to learn linearly non-separable functions
% ====================================================================

% ===========================================================================
% Reference: Negnevitsky, M., "Artificial Intelligence: A Guide to Intelligent  
%            Systems", 3rd edn. Addison Wesley, Harlow, England, 2011.
%            Sec. 6.3 The perceptron
% ===========================================================================
%Two witnesses that I Francis Denton(18024097) I ran the program and considered the output of the code. 
%   Demonstrated to Eli Grealish(student id 18035194) 18 Feb 2020
%   Demonstrated to Ben Eaton (student id 18018782) 18 Feb 2020
% ===========================================================================
% Performing the logical operation XOR is not possible unless
% incorportating a multi-layer perceptron. This is because when plotting the points, 
% it is required to draw a straight line seperating the different values, 
% which is not possible when working with an Xor operator. A perceptron is only able
% to represent a function when there is a line that sepates the 0 and 1 values on the plot.
% When running the program, I expect to see the points plotted but the straight line just
% cutting through one of the points, attempting to perform the seperation.
% ===========================================================================
% Problem: Two-input perceptron is required to perform logical operation XOR.
% ===========================================================================

% Hit any key to define four 2-element input vectors denoted by "p". 
pause 

p=[0 0 1 1;0 1 0 1]

% Hit any key to define four 1-element target vectors denoted by "t". 
pause 

t=[0 1 1 0]

% Hit any key to plot the input and target vectors.
v=[-2 3 -2 3];

plotpv(p,t,v);

% Hit any key to create the perceptron and set its initial weights to random 
% numbers in the range [0, 1]. The perceptron's threshold is set to zero.
pause

net=newp([0 1;0 1],1);
w=(rands(2))';
b=[0];
net.IW{1,1}=w;
net.b{1}=b;

plotpv(p,t,v);
linehandle=plotpc(net.IW{1},net.b{1});

% Hit any key to train the perceptron for one pass and plot the classification line. 
% The training will be stoped after 10 passes.
pause

for a=1:10;
   [net,Y,E]=adapt(net,p,t);
   linehandle=plotpc(net.IW{1},net.b{1},linehandle);
   pause
end;

% Hit any key to see that the perceptron has not learned the XOR operation.
pause

p=[1;1]
a=sim(net,p)

% Hit any key to continue.
pause

p=[0;1]
a=sim(net,p)

% Hit any key to continue.
pause

p=[1;0]
a=sim(net,p)

% Hit any key to continue.
pause

p=[0;0]
a=sim(net,p)
   
echo off
disp('end of Perceptron_XOR')