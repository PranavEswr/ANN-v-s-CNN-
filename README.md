A Convolutional Neural Network (CNN) is a type of deep learning algorithm specifically designed for image processing and recognition tasks. Compared to other classification models, CNNs require less preprocessing as they can automatically learn features from input by filters. 

![1-4](https://github.com/PranavEswr/ANN-v-s-CNN-/assets/91025454/f8446de2-3be7-4fcf-8b98-a4731aff84e2)


Architecture
Convolutional Neural Networks specialized for applications in image & video recognition. CNN is mainly used in image analysis tasks like Image recognition, Object detection and segmentation.

There are three types of layers in Convolutional Neural Networks:
1) Convolutional Layer: This layer will extract features by sliding filters/kernels over the input image for creating feature maps
   ![cnn](https://github.com/PranavEswr/ANN-v-s-CNN-/assets/91025454/f3b3f3f8-0536-4ec2-87a8-176a2ab8dc8d)


3) Pooling Layer: The pooling layer is used to reduce the dimensionality of the feature map. There will be multiple activation & pooling layers inside the hidden layer of the CNN.

   a) Average pooling: The filter calculates the receptive field’s average value when it scans the input.

   b) Max pooling: The filter sends the pixel with the maximum value to populate the output array. This approach is more common than average pooling.

   ![MaxpoolSample2](https://github.com/PranavEswr/ANN-v-s-CNN-/assets/91025454/77ca6d06-ca09-48f4-8e21-b04d299eb4ea)


5) Fully-Connected layer: The input to the fully connected layer is the output from the final Pooling or Convolutional Layer, which is flattened and then fed into the fully connected layer.

(Flatten: This will flatten the feature map or convert 2-dimensional feature maps into a 1-dimensional vector)
