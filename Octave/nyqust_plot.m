pkg load control
clear all
close all
clc

num = [1]
den = [1 2 3]

% Create the transfer function
sys = tf(num, den)

% Plot the nyquist plot
nyquist(sys)
