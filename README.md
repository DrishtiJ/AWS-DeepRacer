# AWS-DeepRacer
AWS DeepRacer is an autonomous 1/18th scale racing car. Reinforcement Learning is used to train and race the car on various tracks.

Reinforcement Learning is a Machine Learning technique where the learning process aims to maximize the sum of rewards. It enables the learning of complex behaviours without any labelled training data. It makes short term decisions while optimizing for the long term goal. 
AWS DeepRacer uses this and makes it fun and intriguing to apply this knowledge for the use case of the autonomous 1/18th scale racing car!


![Reward Graph of Model And Simualation Video Snapshot](https://miro.medium.com/max/700/1*4bXQUNrcmpu84zsQo7NugQ.png)

Using Tensorflow as the framework and Proximal Policy Optimization (PPO) as the reinforcement learning algorithm, made me see how with each iteration I was able to move towards better rewards and eventually a convergence of the model. Working around with 23 parameters to decide the state and reward during training the model and tuning hyper-parameters like learning rate, discount factor, entropy made it a great learning experience.

Here is a the video of successful lap by the AWS DeepRacer.

[![AWS Successful Lap](https://img.youtube.com/vi/egrYHkng7tE/maxresdefault.jpg)](https://youtu.be/egrYHkng7tE)


Details about the Reinforcement Model:


Framework : Tensorflow

Reinforcement Learning Algorithm : Proximal Policy Optimization

Hyperparameters and their values used:

Gradient Descent Batch Size : 64

Entropy : 0.01

Discount Factor : 0.999

Loss type : Huber

Learning Rate : 0.003

Number of epochs : 10
