% ==========================
% Filename: Perceptron_XOR.m
% ==========================
%
% Two witnesses that I, Francis Denton (id 18024097) considered, ran and examined the output of the code.  
%   Demonstrated to Eli Grealish (student id 18035194) - 18 Feb 2020  
%   Demonstrated to Carl Beeston (student id 9999999) - 18 Feb 2020 
%
%   My comments: Upon testing the initial program, we could see that the
%   points were plotted correctly, but the line was cutting through one of
%   the points. I tried to play around with some of the values to see what
%   happened to the program.
%
%   I changed the bias or b variable to -1 which changed all of the outputs
%   to 0, no matter what combination for 1 or 0 we tested for. This clearly
%   wasnt effective so I reverted it. 
%
%   After discussing with some people, we came up with the idea to try and
%   alter the plot, changing it into 3-Dimensiona. By altering the
%   angle of view of the figure. We were able to seperate the points,
%   albiet it not seperated with a straight line as we already know this
%   isnt possible using an XOR.
%
echo on;
%
%
% ====================================================================
% The perceptron: an attempt to learn linearly non-separable functions
% ====================================================================

% ============================================================================
% Reference: Negnevitsky, M., "Artificial Intelligence: A Guide to Intelligent  
%            Systems", 3rd edn. Addison Wesley, Harlow, England, 2011.
%            Sec. 6.3 The perceptron
% ============================================================================

% ===========================================================================
% Problem: Two-input perceptron is required to perform logical operation XOR.
% ===========================================================================

% Hit any key to define four 2-element input vectors denoted by "p". 
pause 

p=[0 0 1 1;0 1 0 1;0 0 0 1]

% Hit any key to define four 1-element target vectors denoted by "t". 
pause 

t=[0 1 1 0]

% Hit any key to plot the input and target vectors.
v=[-2 3 -2 3];

plotpv(p,t,v);

% Hit any key to create the perceptron and set its initial weights to random 
% numbers in the range [0, 1]. The perceptron's threshold is set to zero.
pause

net=newp([0 1;0 1;0 1],1);
w=(rands(3))';
b=[0];
net.IW{1,1}=w;
net.b{1}=b;

plotpv(p,t,v);
linehandle=plotpc(net.IW{1},net.b{1});

% Hit any key to train the perceptron for one pass and plot the classification line. 
% The training will be stoped after 20 passes.
pause

for a=1:20;
   [net,Y,E]=adapt(net,p,t);
   linehandle=plotpc(net.IW{1},net.b{1},linehandle);
   pause
end;

% Hit any key to see that the perceptron has not learned the XOR operation.
pause

p=[1;1;1]
a=sim(net,p)

% Hit any key to continue.
pause

p=[0;1;0]
a=sim(net,p)

% Hit any key to continue.
pause

p=[1;0;0]
a=sim(net,p)

% Hit any key to continue.
pause

p=[0;0;0]
a=sim(net,p)
   
echo off
disp('end of Perceptron_XOR')