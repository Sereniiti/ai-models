# ai-models

This is the graduation project as part of the master's degree at DSTI.  The idea was to develop an AI to detect agressive forms of written communication, based on criteria developed by psychologists.  For example, a sentence like "you are always like this," is considered agressive and likely to provoke a hostile reaction from the recipient, and should therefore be avoided.  The AI was to be deployed as an API for companies to install on their email clients and internal discussion boards.  

These are the AI models developed by Hazem Eseifan, starting from a dataset of 11,000 phrases, classified on a 5-level scale of aggressiveness.  We used NTKL and keras.  After cleaning up the text, we simplified the classification into binary, aggressive or non-aggressive, because this is really all that mattered.   We built a neural network with two hidden layers, 20 units each with relu activation, and an output layer with sigmoid activation; plus adam optimiser and binary cross-entropy loss function.  

The results achieved were excellent.  The model training took only a few seconds, and the predictions on the test set achieved 89% overall accuracy and 90% accuracy in detecting agressive phrases.  We got 80% grade for the project.
