A Convolutional Neural Network (CNN) is a type of deep learning algorithm specifically designed for image processing and recognition tasks. Compared to other classification models, CNNs require less preprocessing as they can automatically learn features from input by filters. 

Architecture
Convolutional Neural Networks specialized for applications in image & video recognition. CNN is mainly used in image analysis tasks like Image recognition, Object detection and segmentation.

There are three types of layers in Convolutional Neural Networks:
1) Convolutional Layer: This layer will extract features by sliding filters/kernels over the input image for creating feature maps

2) Pooling Layer: The pooling layer is used to reduce the dimensionality of the feature map. There will be multiple activation & pooling layers inside the hidden layer of the CNN.

   Average pooling: The filter calculates the receptive field’s average value when it scans the input.
   Max pooling: The filter sends the pixel with the maximum value to populate the output array. This approach is more common than average pooling. 

4) Fully-Connected layer: The input to the fully connected layer is the output from the final Pooling or Convolutional Layer, which is flattened and then fed into the fully connected layer.

(Flatten: This will flatten the feature map or convert 2-dimensional feature maps into a 1-dimensional vector)
