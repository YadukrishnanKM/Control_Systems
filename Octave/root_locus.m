pkg load control
clear all
close all
clc

numerator   =   [1]
denominator =   [1 7 24 9]

% Create the transfer function
system = tf(numerator, denominator)

% Plot the root locus
rlocus(system)
line ([0,0],[-10, 10], "linewidth", 2, "color", 'k')
