Machine learning exploded in popularity over the last 10 years. Looking back
here's a list of my favourite machine learning papers of 2010-2019.

1. Smith S., Kindermans P., Le Q., (2017).
   *Don't Decay the Learning Rate, Increase the Batch Size*.

   The takeaway from this short paper is that by increasing the batch size, you
   can train to higher accuracy with fewer parameter updates, and hence in less
   time. As a proof of concept they trained ResNet-50 on ImageNet to 76.1%
   validation accuracy in under 30 minutes.

   I came across this paper while working on
   [minesweeper]({{ site.baseurl }}{% link _posts/2019-12-31-beating-minesweeper-with-neural-networks.markdown %}).
   Applying this technique dramatically the training performance, getting a
   53.8% win rate on beginner boards in under 30mins.

2. Silver et al. (2016). *Mastering the game of Go with deep neural networks
   and tree search*.

   This is the first AlphaGo paper. It describes the architecture they used to
   combine deep neural networks (DNN) with Monte-Carlo tree search (MCTS).

   I tried to adapt some ideas of this to the simpler game of 2048, however I
   had trouble training the policy network in a reasonable time and ultimately
   abandoned it.

3. Krizhevsky A., Sutskever I., Hinton G., (2014). *ImageNet Classification
   with Deep Convolutional Neural Networks*.

   This paper covers the AlexNet architecture which famously won the ImageNet
   competition by a large margin in 2012. In some ways it was ahead of its time,
   using several concepts we now take for granted.

   They used ReLU over TanH, which at the time was an unconventional choice,
   but provides better performance due to the linearity. Even still, training
   this model with 2 GPUs in parallel it still took 6 days.

   An architecture of 60 million parameters is easy to overfit. They used
   dropout and data augmentation to combat this.

   Although many of the ideas here are not new, this paper is a great
   demonstration of how to apply them in practise.
