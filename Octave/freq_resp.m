pkg load control
clear all
close all
clc

num = [1]
den = [1 2 3]

% find freqency response
[h, w] = freqz(num, den)

%plot freqency response
freqz_plot(w,h)
